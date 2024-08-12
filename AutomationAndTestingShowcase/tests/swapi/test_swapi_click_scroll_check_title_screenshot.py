from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# Configure options for ChromeDriver (optional)
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen') # Disable the search engine choice screen in Chrome
chrome_options.add_argument("--start-maximized")  # Start in full-screen mode

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the desired webpage
    driver.get('https://swapi.dev/')  # Replace with your target URL

    # Find the link using a CSS selector and click it
    link = driver.find_element(By.CSS_SELECTOR, 'a[href*=documentation]')  # Update with the actual CSS selector for the link
    link.click()

    # Wait for the page to load after clicking the link (adjust time as needed)
    time.sleep(2)

        # Find the link using a CSS selector and click it
    link = driver.find_element(By.CSS_SELECTOR, 'a[href*=intro]')  # Update with the actual CSS selector for the link
    link.click()

    # Wait for the page to load after clicking the link (adjust time as needed)
    time.sleep(2)


    # Locate the <h3> element by its CSS selector and text content
    h3_elements = driver.find_elements(By.CSS_SELECTOR, 'h3')
    
    # Find the <h3> element with the text "scroll to me"
    for h3 in h3_elements:
        if h3.text == "Base URL":
            # Scroll to the found <h3> element using JavaScript
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", h3)

            current_time = datetime.now()
            timestamp = current_time.strftime("%Y%m%d_%H%M%S")

            screenshot_path = f"screenshoots/swapi_screenshot_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

            break

    # Optional: Wait to observe the scroll action
    time.sleep(3)

finally:
    # Close the browser
    driver.quit()