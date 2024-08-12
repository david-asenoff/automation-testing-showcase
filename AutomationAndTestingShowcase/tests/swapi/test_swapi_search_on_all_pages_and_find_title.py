from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start in full-screen mode
chrome_options.add_argument('--disable-search-engine-choice-screen')

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the SWAPI main page (replace with the actual URL)
    driver.get("https://swapi.dev/")  # Replace with the URL of the main page

    # Wait for the page to fully load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Locate menu items that lead to different pages (update this to the actual selector)
    menu_links = driver.find_elements(By.CSS_SELECTOR, ".navbar-nav > li > a")  # Replace with actual selector for menu links

    # Store URLs of the menu items
    menu_urls = [link.get_attribute("href") for link in menu_links]

    # Define the specific text to search for in header elements
    specific_texts = ["Films", "Species", "Starships"]  # Example texts to search for

    # Visit each menu item page and search header elements
    for url in menu_urls:
        # Open the menu item page

        current_url = driver.current_url
        absolute_url = urljoin(current_url, url)

        print(f"Search in: {absolute_url}")
        driver.get(absolute_url)

        time.sleep(2)

        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Find all header elements on the page
        headers = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")

        # Search for specific text in headers
        for header in headers:
            header_text = header.text
            if any(text in header_text for text in specific_texts):
                print(f"Found '{header_text}' in {url}")

                    # Get the element's location
                location = header.location
                x = location['x']
                y = location['y']

                # Get the element's size
                size = header.size
                width = size['width']
                height = size['height']

                # Print the element's coordinates and size
                print(f"Element coordinates: (x: {x}, y: {y})")
                print(f"Element size: (width: {width}, height: {height})\n")

finally:
    # Close the browser
    driver.quit()