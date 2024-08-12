import requests
from bs4 import BeautifulSoup

# Define the URL to be scraped
url = 'https://github.com/login'

# Send a GET request to the specified URL
resp = requests.get(url)

# Parse the response content using BeautifulSoup with 'html.parser'
soup = BeautifulSoup(resp.text, 'html.parser')

# Check if the request was successful by verifying the status code (200 indicates success)
if resp.status_code == 200:
    # Extract the CSRF token from the HTML input field with name 'authenticity_token'
    csrf_token = soup.find("input", {"name": "authenticity_token"}).get("value")
    # Extract the timestamp from the HTML input field with name 'timestamp'
    timestamp = soup.find("input", {"name": "timestamp"}).get("value")
    # Extract the timestamp secret from the HTML input field with name 'timestamp_secret'
    timestamp_secret = soup.find("input", {"name": "timestamp_secret"}).get("value")
else:
    # Print an error message if the request was not successful
    print(f'Authentication failed. Status code: {resp.status_code}')

# Print the extracted values
print("Csrf token is:", csrf_token)
print("Timestamp is:", timestamp)
print("Timestamp secret is:", timestamp_secret)