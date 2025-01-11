import unittest

import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import analyze_password  # Import the function from main.py



class TestPasswordAnalysis(unittest.TestCase):
    def test_password_weak_due_to_length(self):
        """Test that passwords shorter than 6 characters are classified as Weak."""
        result = analyze_password("123")
        self.assertEqual(result['strength'], 'Weak')

    def test_password_weak_due_to_content(self):
        """Test that passwords with only numbers or letters are classified as Weak."""
        result = analyze_password("123456")
        self.assertEqual(result['strength'], 'Weak')

    def test_password_medium(self):
        """Test that passwords with at least 6 characters and a mix of numbers and letters are Medium."""
        result = analyze_password("abc123")
        self.assertEqual(result['strength'], 'Medium')

    def test_password_strong(self):
        """Test that passwords with at least 8 characters, including special characters, are Strong."""
        result = analyze_password("Strong@123")
        self.assertEqual(result['strength'], 'Strong')

    def test_password_medium_with_alnum(self):
        """Test Medium password with mixed alphanumeric characters."""
        result = analyze_password("abc12345")
        self.assertEqual(result['strength'], 'Medium')

    def test_password_empty(self):
        """Test that empty passwords return Weak."""
        result = analyze_password("")
        self.assertEqual(result['strength'], 'Weak')

    def test_password_with_special_characters(self):
        """Test that passwords with special characters but fewer than 8 characters are not Strong."""
        result = analyze_password("abc@12")
        self.assertEqual(result['strength'], 'Medium')

if __name__ == "__main__":
    unittest.main()

