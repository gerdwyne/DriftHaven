# test_drifthaven.py
"""
Tests for DriftHaven module.
"""

import unittest
from drifthaven import DriftHaven

class TestDriftHaven(unittest.TestCase):
    """Test cases for DriftHaven class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DriftHaven()
        self.assertIsInstance(instance, DriftHaven)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DriftHaven()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
