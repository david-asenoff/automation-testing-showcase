# src/math_operations/math_operations.py

def add(a, b):
    """
    Returns the sum of two numbers.
    
    Args:
        a (int/float): The first number.
        b (int/float): The second number.
    
    Returns:
        int/float: The sum of a and b.
    """
    return a + b

def multiply(a, b):
    """
    Returns the product of two numbers.
    
    Args:
        a (int/float): The first number.
        b (int/float): The second number.
    
    Returns:
        int/float: The product of a and b.
    """
    return a * b

if __name__ == "__main__":
    print(f"3 + 5 = {add(3, 5)}")
    print(f"3 * 5 = {multiply(3, 5)}")
