import unittest
from unittest.mock import patch, MagicMock
from database_utils import count_products, delete_product_by_name

class TestDatabaseUtils(unittest.TestCase):

    @patch('database_utils.get_db_connection')
    def test_count_and_delete_product(self, mock_get_db_connection):
        # Setup mock connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        # Configure the mock connection to return the mock cursor
        mock_get_db_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Simulate the product count before deletion
        mock_cursor.fetchone.side_effect = [(10,), (9,)]  # First count 10, after delete count 9

        # Count products before deletion
        initial_count = count_products()
        self.assertEqual(initial_count, 10)

        # Simulate the deletion of the "Banana" product
        delete_product_by_name("Banana")

        # Count products after deletion
        final_count = count_products()
        self.assertEqual(final_count, 9)

        # Check that the correct queries were executed
        mock_cursor.execute.assert_any_call("SELECT COUNT(*) FROM products")
        mock_cursor.execute.assert_any_call("DELETE FROM products WHERE name = ?", ("Banana",))

        # Ensure the connection was closed after operations
        self.assertEqual(mock_connection.close.call_count, 3)  # Once after each DB interaction

if __name__ == '__main__':
    unittest.main()