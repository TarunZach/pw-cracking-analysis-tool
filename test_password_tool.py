import os
import sys
import unittest
from unittest.mock import patch, mock_open, MagicMock
import tkinter as tk
import time
import logging


# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


try:
    from main import PasswordAnalysisTool
except ImportError:
    print("Error: Cannot import PasswordAnalysisTool. Ensure 'main.py' is in the same directory.")
    sys.exit(1)

class TestPasswordAnalysisTool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures before all tests"""
        # Create mock files that the main application expects
        cls.create_mock_files()

    @classmethod
    def create_mock_files(cls):
        pass
        
        
        

    def setUp(self):
        """Set up test environment before each test"""
        self.root = tk.Tk()
        self.app = PasswordAnalysisTool(self.root)

    def tearDown(self):
        """Clean up after each test"""
        self.root.destroy()

    def test_password_strength_empty(self):
        """Test password strength calculation for empty password"""
        logging.info("Test password strength calculation for empty password")
        strength = self.app.calculate_password_strength("")
        self.assertEqual(strength, 0)

    def test_password_strength_weak(self):
        """Test password strength calculation for weak password"""
        logging.info("Test password strength calculation for weak password")
        strength = self.app.calculate_password_strength("password123")
        self.assertLess(strength, 60)

    def test_password_strength_strong(self):
        """Test password strength calculation for strong password"""
        logging.info("Test password strength calculation for strong password")
        strength = self.app.calculate_password_strength("P@ssw0rd!2023Complex")
        self.assertGreaterEqual(strength, 80)

    def test_password_common_patterns(self):
        """Test password strength calculation with common patterns"""
        logging.info("Test password strength calculation with common patterns")
        strength = self.app.calculate_password_strength("qwerty123")
        self.assertLess(strength, 50)

    def test_password_repeated_chars(self):
        """Test password strength calculation with repeated characters"""
        logging.info("Test password strength calculation with repeated characters")
        strength = self.app.calculate_password_strength("aaa123")
        self.assertLess(strength, 50)







    @patch('tkinter.messagebox.showinfo')
    @patch('time.sleep')
    def test_dictionary_attack(self, mock_sleep, mock_showinfo):
        """Test dictionary attack functionality with performance checks"""
        # Setup test data
        logging.info("Starting test_dictionary_attack")
        text_widget = tk.Text(self.root)
        test_password = "password"
        text_widget.insert("1.0", test_password)
        logging.info(f"Test password set to: {test_password}")
        
        # Track start time
        start_time = time.time()
        logging.info("Performing dictionary attack")
        
        # Perform the attack
        self.app.perform_dictionary_attack_action(text_widget)
        
        # Track end time
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Dictionary attack completed in {execution_time:.2f} seconds")

        
        # Get the result text
        result = text_widget.get("1.0", tk.END)
        
        # Verify test cases
        self.assertIn("Trying password:", result)
        logging.info(f"Result text: {result}")
        #self.assertIn("Password not found in the wordlist", result)  # Updated assertion
        
        # Verify performance
        self.assertLess(execution_time, 5.0, "Dictionary attack took too long")
        
        # Verify attack progress
        mock_showinfo.assert_called()
        
        # Verify proper cleanup
        self.assertNotIn("error", result.lower())
        self.assertNotIn("exception", result.lower())
        
        # Test with empty password
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", "")
        self.app.perform_dictionary_attack_action(text_widget)
        empty_result = text_widget.get("1.0", tk.END)
        self.assertIn("Trying password:", empty_result)
        
        # Test with common password
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", "password")  # Using a common password that should be in the list
        self.app.perform_dictionary_attack_action(text_widget)
        common_result = text_widget.get("1.0", tk.END)
        self.assertIn("Trying password:", common_result)
        
        # Verify UI updates
        self.assertTrue(mock_showinfo.call_count >= 3)
        mock_sleep.assert_called()






    @patch('tkinter.messagebox.showinfo')
    @patch('time.sleep')
    def test_rainbow_attack(self, mock_sleep, mock_showinfo):
        """Test dictionary attack functionality with performance checks"""
        # Setup test data
        logging.info("Starting test_rainbow_table_attack")

        text_widget = tk.Text(self.root)
        test_password = "password"
        text_widget.insert("1.0", test_password)
        logging.info(f"Test password set to: {test_password}")
        
        
        # Track start time
        start_time = time.time()
        
        # Perform the attack
        self.app.perform_rainbow_table_action(text_widget)
        logging.info("Performing rainbow table attack")
        
        # Track end time
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Rainbow table attack completed in {execution_time:.2f} seconds")
        
        # Get the result text
        result = text_widget.get("1.0", tk.END)
        logging.info(f"Result text: {result}")
        
        # Verify test cases
        self.assertIn("Table operation completed.", result)
        logging.info("Verified that 'Table operation completed.' is in the result")
        #self.assertIn("Password not found in the wordlist", result)  # Updated assertion
        
        # Verify performance
        self.assertLess(execution_time, 5.0, "Dictionary attack took too long")
        logging.info("Verified that showinfo was called")
        
        # Verify attack progress
        mock_showinfo.assert_called()
        
        # Verify proper cleanup
        self.assertNotIn("error", result.lower())
        self.assertNotIn("exception", result.lower())
        
        # Test with empty password
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", "")
        self.app.perform_dictionary_attack_action(text_widget)
        empty_result = text_widget.get("1.0", tk.END)
        self.assertIn("Trying password:", empty_result)
        
        # Test with common password
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", "password")  # Using a common password that should be in the list
        self.app.perform_dictionary_attack_action(text_widget)
        common_result = text_widget.get("1.0", tk.END)
        self.assertIn("Trying password:", common_result)
        
        # Verify UI updates
        self.assertTrue(mock_showinfo.call_count >= 3)
        mock_sleep.assert_called()



    
    @patch('tkinter.messagebox.showinfo')
    @patch('time.sleep')
    def test_brute_force_attack(self, mock_sleep, mock_showinfo):
        """Test brute force attack functionality with performance checks"""
        # Setup test data
        logging.info("Starting test_brute_force_attack")
        text_widget = tk.Text(self.root)
        test_password = "1"
        text_widget.insert("1.0", test_password)
        logging.info(f"Test password set to: {test_password}")
        
        # Track start time
        start_time = time.time()
        
        # Perform the attack
        self.app.perform_brute_force_action(text_widget)
        logging.info("Performing brute force attack")
        
        # Track end time
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Brute force attack completed in {execution_time:.2f} seconds")
        
        # Get the result text
        result = text_widget.get("1.0", tk.END)
        logging.info(f"Result text: {result}")
        
        # Verify test cases
        self.assertIn("Simulating Brute Force Attack", result)
        self.assertIn("Completed!", result)
        self.assertTrue("Password Found:" in result)
        logging.info("Verified that brute force attack simulation messages are in the result")
        
        # Verify performance
        self.assertLess(execution_time, 5.0, "Brute force attack took too long")
        logging.info("Verified that execution time is within acceptable limits")
        
        # Verify attack progress
        mock_showinfo.assert_called()
        logging.info("Verified that showinfo was called")
        
        # Verify proper cleanup
        self.assertNotIn("error", result.lower())
        self.assertNotIn("exception", result.lower())
        logging.info("Verified that no errors or exceptions are present in the result")
        
        # Test with empty password
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", "")
        self.app.perform_brute_force_action(text_widget)
        empty_result = text_widget.get("1.0", tk.END)
        self.assertIn("Simulating", empty_result)
        
        # Test with special characters
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", "1")
        self.app.perform_brute_force_action(text_widget)
        special_result = text_widget.get("1.0", tk.END)
        self.assertIn("Simulating", special_result)
        
        # Verify UI updates
        self.assertTrue(mock_showinfo.call_count >= 3)
        mock_sleep.assert_called()
        




    def test_password_character_diversity(self):
        """Test password strength calculation based on character diversity"""
        # Test with only lowercase
        strength_lower = self.app.calculate_password_strength("abcdef")
        
        # Test with lower and upper
        strength_mixed = self.app.calculate_password_strength("abcDEF")
        
        # Test with lower, upper, and numbers
        strength_complex = self.app.calculate_password_strength("abcDEF123")
        
        # Test with all character types
        strength_full = self.app.calculate_password_strength("abcDEF123!@#")
        
        self.assertLess(strength_lower, strength_mixed)
        self.assertLess(strength_mixed, strength_complex)
        self.assertLess(strength_complex, strength_full)



if __name__ == '__main__':
    unittest.main()
