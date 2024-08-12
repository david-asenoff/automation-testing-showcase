import requests
import json
from selenium import webdriver
import time  # Importing the time library to add delay

# Function to make an API request and handle errors
def make_api_request(url, params=None):
    try:
        # Send a GET request to the specified URL with optional parameters
        response = requests.get(url, params=params)
        # Raise an exception for HTTP errors (status codes 4xx or 5xx)
        response.raise_for_status()
        # Parse the response JSON data
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Print an error message if the request fails
        print(f"An error occurred: {e}")
        return None
    
# Define the API URL and optional parameters
api_url = 'https://jsonplaceholder.typicode.com/todos/'
params = {'key': 'value'}

# Call the function to make the API request and get the JSON data
json_data = make_api_request(api_url, params)
# Format the JSON data with indentation for readability
json_data_format = json.dumps(json_data, indent=2)

# If the API request was successful and data was returned
if json_data:
    print(json.dumps(json_data, indent=2))
    # Convert the formatted JSON string back to a Python object
    data = json.loads(json_data_format)
    # Count the number of entries in the data
    num_items = len(data)
    # Print the number of data entries
    print(f"Number of data entries: {num_items}")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the specified URL
    driver.get('https://jsonplaceholder.typicode.com/todos/1')
    time.sleep(3)
finally:
    # Ensure the WebDriver is closed and the browser session is ended
    driver.quit()