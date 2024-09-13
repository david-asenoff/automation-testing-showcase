#python test_script_check_results.py

# Import the function from the other file
from database_utils import get_most_expensive_product

def main():
    # Call the function and store the result
    result = get_most_expensive_product()
    
    # Print the result
    if result:
        print(f"Most Expensive Product: {result[0]}")
        print(f"Description: {result[1]}")
        print(f"Price: {result[2]}")
    else:
        print("No products found.")

if __name__ == '__main__':
    main()