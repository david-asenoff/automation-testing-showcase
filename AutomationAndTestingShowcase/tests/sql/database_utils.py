import pyodbc

def get_db_connection():
    """
    Establishes a connection to the SQL Server database using Windows Authentication.
    """
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-HCHRRQ0\\SQLEXPRESS02;"
        "DATABASE=ProductDB;"
        "Trusted_Connection=yes;"
    )
    return connection

def get_most_expensive_product():
    """
    Fetches the most expensive product from the products table.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT TOP 1 name, description, price FROM products ORDER BY price DESC"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

# Function to update product price
def update_product_price(product_name, new_price):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE products SET price = ? WHERE name = ?"
    cursor.execute(query, (new_price, product_name))
    connection.commit()
    cursor.close()
    connection.close()