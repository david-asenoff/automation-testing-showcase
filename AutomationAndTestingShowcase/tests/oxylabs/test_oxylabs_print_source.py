from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Initialize Chrome options to customize the browser's behavior
chrome_options = Options()
# Disable the search engine choice screen in Chrome
chrome_options.add_argument('--disable-search-engine-choice-screen')
# Run Chrome in headless mode (without a GUI) to run tests in the background
chrome_options.add_argument('--headless=new')

# Create a new instance of the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the specified URL
driver.get("https://www.oxylabs.io/")
# Print the page source (HTML content) of the current page to the console
print(driver.page_source)
# Close the WebDriver and end the browser session
driver.quit()