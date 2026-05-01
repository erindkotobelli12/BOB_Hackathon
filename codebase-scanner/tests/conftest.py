"""Pytest configuration for test discovery."""

import sys
from pathlib import Path

# Add parent directory to sys.path so imports work correctly
sys.path.insert(0, str(Path(__file__).parent.parent))

# Made with Bob
