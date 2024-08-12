import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests

# Define a fixture to set up the WebDriver
@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)
    chrome_options.add_argument('--disable-gpu')  # Optional: Disable GPU acceleration

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    yield driver
    driver.quit()

# Test function to check page response code and title
def test_swapi_response_and_title(driver):
    url = 'https://swapi.dev/'

    # Check page response code
    response = requests.get(url)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Navigate to the URL with Selenium
    driver.get(url)

    # Check if the page title contains 'swapi'
    page_title = driver.title
    assert 'swapi' in page_title.lower(), f"Expected title to contain 'SWAPI', but got '{page_title}'"