# pip install beautifulsoup4

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Function to clean HTML content by removing tags and returning plain text
def clean_html(html_string):
    # Parse the HTML string with BeautifulSoup
    soup = BeautifulSoup(html_string, 'html.parser')
    # Extract and return the text content
    return soup.get_text()

# Set up Chrome options
chrome_options = Options()
# Disable the search engine choice screen in Chrome
chrome_options.add_argument('--disable-search-engine-choice-screen')
chrome_options.add_argument("--start-maximized")  # Start in full-screen mode

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the target URL
driver.get("https://sandbox.oxylabs.io/products/category/nintendo/wii")

# Pause execution to allow the page to fully load
time.sleep(5)

# Find the element containing the result count and clean its HTML content
search_box = driver.find_element(By.CLASS_NAME, "result-count")
search_box_cleaned = clean_html(search_box.get_attribute('innerHTML'))

# Print the cleaned result count
print(f"Total results (unclean) : {search_box_cleaned}")

search_box_total = search_box.find_elements(By.TAG_NAME, "span")
span_text_total = search_box_total[0].text
print(f"Total results :{span_text_total}")

current_page = driver.find_elements(By.CSS_SELECTOR, 'a[rel="canonical"]')[0].get_attribute('innerHTML')

# Loop through pages until the page number is less than 4
while int(current_page) * 32 < int(span_text_total):
    # Find all product card elements on the page
    products = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

    # Extract and concatenate product titles
    title_texts = [product.find_element(By.CSS_SELECTOR, "h4.title").get_attribute('innerHTML') for product in products]
    concatinated_titles = "; ".join(title_texts)

    # Print the current page number and all product titles
    current_page = driver.find_elements(By.CSS_SELECTOR, 'a[rel="canonical"]')[0].get_attribute('innerHTML')
    print(f"Current page: {current_page}")
    print(f"All product names: {concatinated_titles}")

    # Find the 'next' page link and click it to go to the next page
    link = driver.find_element(By.CSS_SELECTOR, 'a[rel="next"]')  # Update with the actual CSS selector for the link

    if not link:
        break

    link.click()

    # Wait for the next page to load before proceeding
    time.sleep(5)