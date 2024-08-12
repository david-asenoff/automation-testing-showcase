import requests
import json
from selenium import webdriver
import time  # Importing the time library to add delay

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Define the URL for the POST request
    url = 'https://jsonplaceholder.typicode.com/posts'
    # Define the data to be sent in the POST request
    data = {
        'title': 'title_test',  # Title of the post
        'body': 'body_test',    # Body content of the post
        'userId': 1,            # User ID associated with the post
    }

    # Define custom headers for the POST request
    headers_custom = {
        'Content-type': 'application/json; charset=UTF-8',  # Specify that the content type is JSON
    }
    
    # Send a POST request to the specified URL with the data and custom headers
    response = requests.post(url, json=data, headers=headers_custom)

    # Check if the response status code indicates success (200 OK)
    if response.status_code == 200:
        # Print the JSON response content if the request was successful
        print(f"Response: {response.json()}")
    else:
        # Print the response text if the request failed
        print(f"Response: {response.text}")
        
finally:
    # Ensure the WebDriver is closed and the browser session is ended
    driver.quit()