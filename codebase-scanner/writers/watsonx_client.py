"""watsonx.ai API client for generating docstrings using urllib.request only."""

import json
import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from typing import Dict, Any, Optional


class WatsonxClient:
    """Client for interacting with watsonx.ai text generation API."""
    
    def __init__(self, dry_run: bool = False):
        """Initialize watsonx.ai client with credentials from environment."""
        self.dry_run = dry_run
        self.api_key = os.environ.get('WATSONX_API_KEY')
        self.project_id = os.environ.get('WATSONX_PROJECT_ID')
        self.url = os.environ.get('WATSONX_URL', 'https://us-south.ml.cloud.ibm.com')
        
        # IAM token caching
        self._cached_token = None
        self._token_expiration = None
        self._token_buffer = 60  # Refresh token 60 seconds before expiration
        
        if not dry_run:
            if not self.api_key or not self.project_id:
                print("\n" + "="*60)
                print("ERROR: Missing watsonx.ai credentials")
                print("="*60)
                print("Set WATSONX_API_KEY, WATSONX_PROJECT_ID, and WATSONX_URL")
                print("environment variables — see .env.example in project root")
                print("="*60 + "\n")
                sys.exit(1)
        
        self.endpoint = f"{self.url}/ml/v1/text/generation"
        self.model_id = "ibm/granite-3-8b-instruct"
    
    def generate_docstring(self, function_signature: str, function_body: str) -> Optional[str]:
        """Generate a Google-style docstring for a Python function."""
        if self.dry_run:
            return "[DRY RUN] Docstring would be generated here"
        
        prompt = f"""Generate a Google-style Python docstring for this function.
Include Args, Returns, and Raises sections as appropriate.
Do not include placeholder text, TODO comments, or triple quotes.

Function signature:
{function_signature}

Function body:
{function_body}

Generate ONLY the docstring content:"""
        
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self._call_api(prompt)
                docstring = self._extract_docstring(response)
                return docstring if docstring and self._validate_docstring(docstring) else None
            except Exception as e:
                error_msg = str(e)
                if '429' in error_msg or 'rate limit' in error_msg.lower():
                    if attempt < max_retries - 1:
                        print(f"Rate limit hit, retrying in 1 second... (attempt {attempt + 1}/{max_retries})")
                        time.sleep(1)
                        continue
                print(f"Error generating docstring: {e}")
                return None
        return None
    
    def _get_iam_token(self) -> str:
        """Obtain IBM Cloud IAM access token using API key.
        
        Exchanges the API key for an IAM access token via IBM Cloud IAM service.
        Caches the token and tracks expiration for automatic refresh.
        
        Returns:
            str: Valid IAM access token
            
        Raises:
            Exception: If token acquisition fails or API key is invalid
        """
        # Check if cached token is still valid
        if self._is_token_valid():
            return self._cached_token  # type: ignore[return-value]
        
        # Request new token from IBM Cloud IAM
        iam_url = 'https://iam.cloud.ibm.com/identity/token'
        
        # Prepare form data for token request
        form_data = {
            'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
            'apikey': self.api_key
        }
        data = urllib.parse.urlencode(form_data).encode('utf-8')
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        req = urllib.request.Request(iam_url, data=data, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                token_response = json.loads(response.read().decode('utf-8'))
                
                # Extract and cache token information
                self._cached_token = token_response['access_token']
                self._token_expiration = token_response['expiration']
                
                return self._cached_token
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            raise Exception(f"IAM token acquisition failed (HTTP {e.code}): {error_body}")
        except urllib.error.URLError as e:
            raise Exception(f"IAM token acquisition failed (URL Error): {e.reason}")
        except (KeyError, json.JSONDecodeError) as e:
            raise Exception(f"IAM token response parsing failed: {e}")
    
    def _is_token_valid(self) -> bool:
        """Check if cached IAM token is still valid.
        
        Returns:
            bool: True if token exists and hasn't expired (with buffer), False otherwise
        """
        if not self._cached_token or not self._token_expiration:
            return False
        
        current_time = int(time.time())
        # Token is valid if current time is before (expiration - buffer)
        return current_time < (self._token_expiration - self._token_buffer)
    
    def _call_api(self, prompt: str) -> Dict[str, Any]:
        """Call watsonx.ai API using urllib.request with IAM token authentication.
        
        Args:
            prompt (str): The prompt text to send to the API
            
        Returns:
            Dict[str, Any]: API response containing generated text
            
        Raises:
            Exception: If API call fails or authentication fails
        """
        payload = {
            "model_id": self.model_id,
            "input": prompt,
            "parameters": {
                "max_new_tokens": 500,
                "temperature": 0.3,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
                "stop_sequences": ["```", "def ", "class "]
            },
            "project_id": self.project_id
        }
        
        data = json.dumps(payload).encode('utf-8')
        
        # Get valid IAM token (will refresh if expired)
        iam_token = self._get_iam_token()
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {iam_token}',
            'Accept': 'application/json'
        }
        
        req = urllib.request.Request(self.endpoint, data=data, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            raise Exception(f"HTTP {e.code}: {e.read().decode('utf-8')}")
        except urllib.error.URLError as e:
            raise Exception(f"URL Error: {e.reason}")
    
    def _extract_docstring(self, response: Dict[str, Any]) -> Optional[str]:
        """Extract docstring text from API response."""
        try:
            results = response.get('results', [])
            if not results:
                return None
            
            generated_text = results[0].get('generated_text', '').strip()
            lines = []
            for line in generated_text.split('\n'):
                if line.strip() or lines:
                    lines.append(line)
            return '\n'.join(lines) if lines else None
        except (KeyError, IndexError):
            return None
    
    def _validate_docstring(self, docstring: str) -> bool:
        """Validate that docstring doesn't contain placeholders."""
        if not docstring or len(docstring.strip()) < 10:
            return False
        
        invalid = ['todo', 'fixme', 'placeholder', 'fill this in', 'description here']
        return not any(pattern in docstring.lower() for pattern in invalid)

# Made with Bob
