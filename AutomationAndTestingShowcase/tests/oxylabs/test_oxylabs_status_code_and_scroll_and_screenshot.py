from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time
from datetime import datetime

# Function to fetch the HTTP status code of a given URL
def get_status_code(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
     
# Function to open a website using Selenium, take a screenshot, and print an element's HTML
def open_site_and_make_screenshoot(url, screenshot_path):
    # Set up Chrome options to disable certain features
    chrome_options = Options()
    chrome_options.add_argument('--disable-search-engine-choice-screen')

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    try:
        # Open the specified URL
        driver.get(url)
        # Wait for 3 seconds to allow the page to load
        time.sleep(3)

        # Define a CSS selector to find the desired element
        css_selector = 'div#crbn'
        element = driver.find_element(By.ID, "crbn")

        if element:
            # Print the outer HTML of the element if found
            print(f"Scroll to : {element.get_attribute('outerHTML')}")
        else:
            # Print 'none' if the element is not found
            print('none')

        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView()", element)
        # Wait for 5 seconds to ensure the element is in view
        time.sleep(5)

        # Save a screenshot of the current page
        driver.save_screenshot(screenshot_path)
        print(f"Saved at: {screenshot_path}")
    finally:
        # Quit the WebDriver and close the browser
        driver.quit()

# URL to be tested
url = 'https://jsonplaceholder.typicode.com/guide/'
# Get the status code of the URL
status_code = get_status_code(url)

if status_code:
    # Print the status code if the URL is successfully fetched
    print(f"Status code: {status_code}")

# Get the current time to create a timestamp for the screenshot file
current_time = datetime.now()
timestamp = current_time.strftime("%Y%m%d_%H%M%S")

# Define the path for saving the screenshot with a timestamp
screenshot_path = f"screenshoots/oxylabs_screenshot_{timestamp}.png"
# Open the site and take a screenshot
open_site_and_make_screenshoot(url, screenshot_path)