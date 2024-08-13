import requests  # Importing the requests library to handle HTTP requests
import json  # Importing the json library to work with JSON data
from selenium import webdriver  # Importing the selenium webdriver for browser automation
from selenium.webdriver.chrome.options import Options  # Importing Options to configure the Chrome browser
import time  # Importing the time library to add delay

# Function to make an API request
def make_api_request(url, params=None):
    try:
        # Sending a GET request to the given URL with optional parameters
        response = requests.get(url, params=params)
        # Raise an exception if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        # Convert the response to JSON format
        data = response.json()
        return data  # Return the JSON data
    except requests.exceptions.RequestException as e:
        # Print an error message if an exception occurs
        print(f"An error occurred: {e}")
        return None  # Return None if the request fails

# API URL to fetch data from Star Wars API
api_url = 'https://swapi.dev/api/people/'

# Call the function to make the API request and store the response
json_data = make_api_request(api_url)
# Convert the JSON data to a formatted string for better readability
json_data_format = json.dumps(json_data, indent=2)

# Check if data was successfully fetched
if json_data:
    # Parse the formatted JSON string back to a dictionary
    data = json.loads(json_data_format)
    # Count the number of items in the 'results' key of the JSON response
    num_items = len(data['results'])
    # Print the count of people results
    print(f"People results count: {num_items}")

# Set up Chrome browser options
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen') # Disable the search engine choice screen in Chrome
chrome_options.add_argument("--start-maximized")  # Start in full-screen mode

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the given URL in the browser
    driver.get('https://swapi.dev/api/people/')
    # Wait for 3 seconds to ensure the page loads completely
    time.sleep(3)
finally:
    # Close the browser to free up resources
    driver.quit()