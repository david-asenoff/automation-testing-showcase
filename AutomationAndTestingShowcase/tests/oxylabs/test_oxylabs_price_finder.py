from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import time

# Function to read data from JSON file
def read_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to search for a product on a website and get its price
def search_and_get_price(url, search_box, product, price_text):
    
    driver.get(url)
    time.sleep(3)

    search_box = driver.find_element(By.CSS_SELECTOR, search_box)
    search_box.send_keys(product)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for the search results to load
    try:
        price_element = driver.find_element(By.CSS_SELECTOR, price_text)
        price_text = price_element.text
        print(f"Price found: {price_text}")
        price = float(price_text.replace("€", "").replace(".", "").replace(",", ".").replace(" ", ""))  # Convert price to a float
        return price
    except Exception as e:
        print(f"Error getting price on {url}: {e}")
        return float('inf')  # Return infinity if there's an issue

chrome_options = Options()
# Disable the search engine choice screen in Chrome
chrome_options.add_argument('--disable-search-engine-choice-screen')
chrome_options.add_argument("--start-maximized")  # Start in full-screen mode

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Read the data from the JSON file
file_path = 'text_files/data.json'
data = read_data_from_json(file_path)

# Store the prices for comparison
prices = []

# Loop through each entry in the JSON file
for record in data:
    url = record['url']
    search_box = record['search_box']
    product = record['product']
    price_text = record['price_text']
    price = search_and_get_price(url, search_box, product, price_text)
    prices.append((url, price))


lowest_price_site, lowest_price = min(prices, key=lambda x: x[1])
highest_price_site, highest_price = max(prices, key=lambda x: x[1])

# Output the result
if lowest_price != float('inf'):
    print(f"The lowest price is {lowest_price} on {lowest_price_site}")
else:
    print("Could not find prices for the products.")

# Output the result
if highest_price_site != float('inf'):
    print(f"The highest price is {highest_price} on {highest_price_site}")
else:
    print("Could not find prices for the products.")

# Close the browser
driver.quit()
