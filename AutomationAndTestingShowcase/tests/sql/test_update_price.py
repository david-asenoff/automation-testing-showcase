import unittest
from unittest.mock import patch, MagicMock
import pyodbc
from database_utils import update_product_price

class TestDatabaseOperations(unittest.TestCase):
    @patch('pyodbc.connect')
    def test_update_product_price(self, mock_connect):
        # Mock the connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Simulate updating price
        update_product_price('Banana', 2.99)

        # Check that the correct query was executed
        mock_cursor.execute.assert_called_with(
            "UPDATE products SET price = ? WHERE name = ?", (2.99, 'Banana')
        )

        print("UPDATE products SET price = 2.99 WHERE name = Banana")
        # Check if the changes were committed
        mock_connection.commit.assert_called_once()

        # Ensure the connection is closed
        mock_connection.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()