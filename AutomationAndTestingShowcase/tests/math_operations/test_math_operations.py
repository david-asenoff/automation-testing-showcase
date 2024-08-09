# tests/math_operations/test_math_operations.py

# Import the unittest module, which is a built-in Python module for creating and running tests
import unittest

# Import the functions to be tested from the src.math_operations.math_operations module
# These imports are essential to ensure the functions 'add' and 'multiply' can be accessed and tested
from src.math_operations.math_operations import add, multiply

# Define a test class that inherits from unittest.TestCase
# This class contains the test methods that will verify the behavior of the 'add' and 'multiply' functions
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        """
        Test the add function with different inputs.
        This test case verifies that the add function returns the correct sum
        for both positive and negative integers.
        """
        # Assert that the addition of 3 and 5 equals 8
        self.assertEqual(add(3, 5), 8)
        
        # Assert that the addition of -1 and 1 equals 0
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        """
        Test the multiply function with different inputs.
        This test case verifies that the multiply function returns the correct product
        for both positive and negative integers.
        """
        # Assert that the multiplication of 3 and 5 equals 15
        self.assertEqual(multiply(3, 5), 15)
        
        # Assert that the multiplication of -1 and -1 equals 1
        self.assertEqual(multiply(-1, -1), 1)

# This block checks if the script is being run directly (as opposed to being imported as a module)
# If the script is being run directly, it calls unittest.main(), which runs all the test cases
if __name__ == "__main__":
    unittest.main()
