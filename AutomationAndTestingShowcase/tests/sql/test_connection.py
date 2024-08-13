#python test_connection.py

import pyodbc

def test_connection():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-HCHRRQ0\\SQLEXPRESS02;"
            "DATABASE=ProductDB;"
            "Trusted_Connection=yes;"
        )
        print("Connection successful")
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()