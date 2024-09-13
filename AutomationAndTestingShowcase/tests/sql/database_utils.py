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

def count_products():
    """
    Returns the number of products in the database.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM products"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count

def delete_product_by_name(name):
    """
    Deletes a product by name from the database.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE name = ?"
    cursor.execute(query, (name,))
    connection.commit()
    cursor.close()
    connection.close()


def create_cars_table():
    """
    Creates a table named 'cars' if it doesn't exist.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS cars (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        model VARCHAR(50)
    )
    """
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

def insert_car(id, name, model):
    """
    Inserts a car record into the 'cars' table.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO cars (id, name, model) VALUES (?, ?, ?)"
    cursor.execute(query, (id, name, model))
    connection.commit()
    cursor.close()
    connection.close()

def count_cars():
    """
    Returns the number of cars in the 'cars' table.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM cars"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count

def get_all_car_names():
    """
    Retrieves the 'name' field of all records from the 'cars' table.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM cars")
    car_names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return car_names