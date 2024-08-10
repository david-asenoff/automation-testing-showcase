#pip install beautifulsoup4

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def clean_html(html_string):
  soup = BeautifulSoup(html_string, 'html.parser')
  return soup.get_text()

chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://sandbox.oxylabs.io/products")

time.sleep(5)

search_box = driver.find_element(By.CLASS_NAME, "result-count")
search_box_cleaned = clean_html(search_box.get_attribute('innerHTML'))
print(f"total: {search_box_cleaned}")

current_page = driver.find_elements(By.CSS_SELECTOR, 'a[rel="canonical"]')[0].get_attribute('innerHTML')

while int(current_page) < 4:
  products = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

  # for product in products:
  #   title = product.find_element(By.CSS_SELECTOR, "h4.title").get_attribute('innerHTML')
  #   print(f"title: {title}")

  title_texts = [title.find_element(By.CSS_SELECTOR, "h4.title").get_attribute('innerHTML') for title in products]
  concatinated_titles = "; ".join(title_texts)

  current_page = driver.find_elements(By.CSS_SELECTOR, 'a[rel="canonical"]')[0].get_attribute('innerHTML')
  print(f"Currenct page: {current_page}")

  print(f"All product names: {concatinated_titles}")

  link = driver.find_element(By.CSS_SELECTOR, 'a[rel="next"]')  # Update with the actual CSS selector for the link
  link.click()

  # Wait for the page to load after clicking the link (adjust time as needed)
  time.sleep(5)

# products = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

# title_texts = [title.find_element(By.CSS_SELECTOR, "h4.title").get_attribute('innerHTML') for title in products]
# concatinated_titles = "; ".join(title_texts)

# current_page = driver.find_elements(By.CSS_SELECTOR, 'a[rel="canonical"]')[0].get_attribute('innerHTML')
# print(f"Currenct page: {current_page}")

# print(f"All product names: {concatinated_titles}")

