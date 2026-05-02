#!/usr/bin/env python3
"""Integration test for watsonx.ai API with IAM token authentication.

This script verifies that:
1. IAM token can be obtained from IBM Cloud
2. watsonx.ai API accepts the IAM token
3. Docstring generation works end-to-end

Run with: python test_watsonx_integration.py
Requires: WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_URL environment variables
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import WatsonxClient
sys.path.insert(0, str(Path(__file__).parent))

from writers.watsonx_client import WatsonxClient


def test_watsonx_integration():
    """Test watsonx.ai API integration with IAM authentication."""
    
    print("=" * 70)
    print("WATSONX.AI INTEGRATION TEST")
    print("=" * 70)
    print()
    
    # Check environment variables
    print("1. Checking environment variables...")
    api_key = os.environ.get('WATSONX_API_KEY')
    project_id = os.environ.get('WATSONX_PROJECT_ID')
    url = os.environ.get('WATSONX_URL', 'https://us-south.ml.cloud.ibm.com')
    
    if not api_key or not project_id:
        print("   ❌ FAIL: Missing required environment variables")
        print("   Required: WATSONX_API_KEY, WATSONX_PROJECT_ID")
        print("   Optional: WATSONX_URL (defaults to us-south)")
        return False
    
    print(f"   ✓ API Key: {'*' * 8}{api_key[-4:]}")
    print(f"   ✓ Project ID: {project_id[:8]}...{project_id[-4:]}")
    print(f"   ✓ URL: {url}")
    print()
    
    # Initialize client
    print("2. Initializing WatsonxClient...")
    try:
        client = WatsonxClient(dry_run=False)
        print("   ✓ Client initialized successfully")
    except Exception as e:
        print(f"   ❌ FAIL: Client initialization failed: {e}")
        return False
    print()
    
    # Test IAM token acquisition
    print("3. Testing IAM token acquisition...")
    try:
        token = client._get_iam_token()
        print(f"   ✓ IAM token obtained: {token[:20]}...{token[-10:]}")
        print(f"   ✓ Token expiration: {client._token_expiration}")
        print(f"   ✓ Token cached: {client._cached_token is not None}")
    except Exception as e:
        print(f"   ❌ FAIL: IAM token acquisition failed: {e}")
        return False
    print()
    
    # Test docstring generation with a simple function
    print("4. Testing docstring generation...")
    test_function_signature = "def calculate_total(items, tax_rate=0.1):"
    test_function_body = """    total = sum(items)
    return total * (1 + tax_rate)"""
    
    print(f"   Test function:")
    print(f"   {test_function_signature}")
    for line in test_function_body.split('\n'):
        print(f"   {line}")
    print()
    
    try:
        docstring = client.generate_docstring(test_function_signature, test_function_body)
        
        if docstring:
            print("   ✓ Docstring generated successfully:")
            print("   " + "-" * 66)
            for line in docstring.split('\n'):
                print(f"   {line}")
            print("   " + "-" * 66)
            
            # Validate docstring content
            if len(docstring.strip()) < 10:
                print("   ⚠ WARNING: Docstring seems too short")
                return False
            
            invalid_patterns = ['todo', 'fixme', 'placeholder', 'fill this in']
            if any(pattern in docstring.lower() for pattern in invalid_patterns):
                print("   ⚠ WARNING: Docstring contains placeholder text")
                return False
            
            print("   ✓ Docstring validation passed")
        else:
            print("   ❌ FAIL: No docstring generated (returned None)")
            return False
            
    except Exception as e:
        print(f"   ❌ FAIL: Docstring generation failed: {e}")
        return False
    print()
    
    # Test token caching (second call should use cached token)
    print("5. Testing token caching...")
    try:
        initial_token = client._cached_token
        token2 = client._get_iam_token()
        
        if token2 == initial_token:
            print("   ✓ Token cache working (same token returned)")
        else:
            print("   ⚠ WARNING: Different token returned (cache may not be working)")
            
    except Exception as e:
        print(f"   ❌ FAIL: Token caching test failed: {e}")
        return False
    print()
    
    return True


def main():
    """Run the integration test and print final result."""
    try:
        success = test_watsonx_integration()
        
        print("=" * 70)
        if success:
            print("✅ PASS: All integration tests passed successfully!")
            print("=" * 70)
            print()
            print("The watsonx.ai API connection is working correctly.")
            print("IAM token authentication is functioning as expected.")
            print("You can now run the documentation scanner on your codebase.")
            sys.exit(0)
        else:
            print("❌ FAIL: Integration test failed")
            print("=" * 70)
            print()
            print("Please check:")
            print("1. Environment variables are set correctly")
            print("2. API key has required permissions")
            print("3. Project ID is valid")
            print("4. Network connection to IBM Cloud is available")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠ Test interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n\n❌ FAIL: Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

# Made with Bob
