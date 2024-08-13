import requests  # Importing the requests library for handling HTTP requests
import json  # Importing the json library to work with JSON data
from selenium import webdriver  # Importing Selenium's webdriver for browser automation
from selenium.webdriver.chrome.options import Options  # Importing Options to configure Chrome browser
import time  # Importing the time library to add delay

# Function to make an API request to a given URL
def make_api_request(url, params=None):
    try:
        # Sending a GET request to the specified URL with optional parameters
        response = requests.get(url, params=params)
        # Raise an exception if the response contains an unsuccessful status code
        response.raise_for_status()
        # Parse the response content as JSON
        data = response.json()
        return data  # Return the parsed JSON data
    except requests.exceptions.RequestException as e:
        # Print an error message if an exception occurs during the request
        print(f"An error occurred: {e}")
        return None  # Return None if the request fails

# URL for the Star Wars API endpoint to get information about planets
api_url = 'https://swapi.dev/api/planets/'

# The name of the planet we want to search for in the API response
search_name = 'Coruscant'

# Make an API request to the planets endpoint and store the response
json_data = make_api_request(api_url)
# Convert the JSON response to a formatted string for easier reading
json_data_format = json.dumps(json_data, indent=2)

# Check if the API request was successful and data was returned
if json_data:
    # Parse the formatted JSON string back to a Python dictionary
    data = json.loads(json_data_format)
    # Extract the list of planets from the 'results' key of the JSON data
    results_for_planets = data['results']

    # Initialize a flag to track if the planet is found
    name_found = False

    # Iterate over the list of planets
    for planet in results_for_planets:
        # Check if the current planet's name matches the search name
        if planet['name'] == search_name:
            # Print the details of the found planet in a formatted JSON string
            print(json.dumps(planet, indent=2))
            # Set the flag to True as the planet is found
            name_found = True
            break  # Exit the loop once the planet is found

    # If the planet was not found, print a message indicating this
    if not name_found:
        print(f"Planet {search_name} not found!")

# Set up Chrome browser options
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen') # Disable the search engine choice screen in Chrome
chrome_options.add_argument("--start-maximized")  # Start in full-screen mode

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the planets API URL in the browser
    driver.get('https://swapi.dev/api/planets/')
    # Wait for 3 seconds to ensure the page loads completely
    time.sleep(3)
finally:
    # Ensure the browser is closed to free up resources
    driver.quit()