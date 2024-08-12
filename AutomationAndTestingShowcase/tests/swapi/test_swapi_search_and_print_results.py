from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen') # Disable the search engine choice screen in Chrome
chrome_options.add_argument("--start-maximized")  # Start in full-screen mode

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the SWAPI website (Replace with actual URL)
    driver.get("https://swapi.dev/")  # This is a placeholder URL, update it as needed

    # Locate the input field and send keys
    input_field = driver.find_element(By.ID, "interactive")  # Update with the actual ID of the input field
    input_field.clear()  # Clear any existing text in the input field
    input_field.send_keys("people/77/")  # Example input, replace with desired query

    # Locate and click the request button
    request_button = driver.find_element(By.CLASS_NAME, "btn-primary")  # Update with the actual ID of the button
    request_button.click()

    # Wait for the results to load and display
    time.sleep(2)  # Simple wait for demo purposes; replace with WebDriverWait for a more robust solution

    # Retrieve and print the results
    results_element = driver.find_element(By.ID, "interactive_output")  # Update with the actual ID of the results container
    print("Results:", results_element.text)
finally:
    # Close the browser
    driver.quit()