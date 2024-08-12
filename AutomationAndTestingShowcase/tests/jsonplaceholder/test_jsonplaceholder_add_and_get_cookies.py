from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time  # Importing the time library to add delay

# Set up Chrome options to customize browser behavior
chrome_options = Options()
# Disable the search engine choice screen in Chrome
chrome_options.add_argument('--disable-search-engine-choice-screen')

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the specified URL
driver.get("https://jsonplaceholder.typicode.com/")

# Add a new cookie to the browser session
driver.add_cookie({"name": "test1", "value": "cookie1"})

time.sleep(3)

# Retrieve and print all cookies associated with the current domain
print(driver.get_cookies())