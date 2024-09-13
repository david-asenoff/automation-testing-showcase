import unittest
from unittest.mock import patch, MagicMock
from database_utils import create_cars_table, insert_car, count_cars, get_all_car_names

class TestDatabaseUtils(unittest.TestCase):

    @patch('database_utils.get_db_connection')
    def test_create_insert_and_count_cars(self, mock_get_db_connection):
        # Setup mock connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        # Configure the mock connection to return the mock cursor
        mock_get_db_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Simulate the table creation
        create_cars_table()
        mock_cursor.execute.assert_called_with("""
    CREATE TABLE IF NOT EXISTS cars (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        model VARCHAR(50)
    )
    """)

        # Simulate inserting 11 car records
        for i in range(1, 12):
            insert_car(i, f"Car{i}", f"Model{i}")
            mock_cursor.execute.assert_called_with(
                "INSERT INTO cars (id, name, model) VALUES (?, ?, ?)",
                (i, f"Car{i}", f"Model{i}")
            )

        # Simulate counting the number of cars
        mock_cursor.fetchone.return_value = (11,)
        car_count = count_cars()
        self.assertEqual(car_count, 11)
        mock_cursor.execute.assert_called_with("SELECT COUNT(*) FROM cars")

        # Ensure the connection was closed after each operation
        self.assertEqual(mock_connection.close.call_count, 13)  # 1 for create, 11 for insert, 1 for count

        # Simulate data to be returned by the mocked fetchall call
        mock_cursor.fetchall.return_value = [
            ("Car1",),
            ("Car2",),
            ("Car3",),
            ("Car4",),
            ("Car5",),
            ("Car6",),
            ("Car7",),
            ("Car8",),
            ("Car9",),
            ("Car10",),
            ("Car11",),
        ]

        # Call the function to retrieve all car names
        result = get_all_car_names()

        # Assert that the result matches the mocked data
        expected_names = ["Car1", "Car2", "Car3", "Car4", "Car5", "Car6", "Car7", "Car8", "Car9", "Car10", "Car11"]
        self.assertEqual(result, expected_names)

        # Print all car names
        print("Car Names:")
        for name in result:
            print(name)

if __name__ == '__main__':
    unittest.main()