import unittest
from unittest.mock import patch, MagicMock
from database_utils import get_most_expensive_product

class TestGetMostExpensiveProduct(unittest.TestCase):

    @patch('pyodbc.connect')
    def test_get_most_expensive_product(self, mock_connect):
        # Setup mock connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        # Define what the cursor's fetchone() method should return
        # Simulate the most expensive product
        mock_cursor.fetchone.return_value = ('Blueberry', 'Juicy blueberries', 6.00)

        # Configure the mock connection to return the mock cursor
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Call the function to test
        result = get_most_expensive_product()

        # Assertions to validate the result
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 'Blueberry')
        self.assertEqual(result[1], 'Juicy blueberries')
        self.assertEqual(result[2], 6.00)

        # Check that the correct query was executed
        mock_cursor.execute.assert_called_with("SELECT TOP 1 name, description, price FROM products ORDER BY price DESC")

        # Ensure the connection was closed
        mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()