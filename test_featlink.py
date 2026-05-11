# test_featlink.py
"""
Tests for FeatLink module.
"""

import unittest
from featlink import FeatLink

class TestFeatLink(unittest.TestCase):
    """Test cases for FeatLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FeatLink()
        self.assertIsInstance(instance, FeatLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FeatLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
