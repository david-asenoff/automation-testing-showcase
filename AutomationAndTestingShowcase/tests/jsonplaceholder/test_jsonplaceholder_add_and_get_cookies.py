from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

driver = webdriver.Chrome(options=chrome_options)

# Navigate to url
driver.get("https://jsonplaceholder.typicode.com/")

driver.add_cookie({"name": "test1", "value": "cookie1"})

# Get all available cookies
print(driver.get_cookies())