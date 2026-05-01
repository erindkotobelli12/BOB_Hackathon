"""Run all unit tests for the codebase scanner."""

import unittest
import sys
from pathlib import Path

# Add current directory to sys.path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Discover and run all tests
loader = unittest.TestLoader()
suite = loader.discover('tests', pattern='test_*.py')
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Exit with appropriate code
sys.exit(0 if result.wasSuccessful() else 1)

# Made with Bob
