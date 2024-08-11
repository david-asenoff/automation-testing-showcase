from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Open the webpage
    driver.get('https://swapi.dev/about')

    time.sleep(2)
    # Find the <h4> element with the text "statistics"
    h4_element = driver.find_element(By.XPATH, "//h4[text()='Statistics']")

    # Find all <p> elements that follow this <h4> element
    p_elements = driver.find_elements(By.XPATH, "//h4[text()='Statistics']/following-sibling::p")

    # Print the text of each <p> element
    for p in p_elements:
        print(p.text)

finally:
    # Clean up and close the browser
    driver.quit()