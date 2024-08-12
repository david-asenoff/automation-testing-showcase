from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure options for ChromeDriver (optional)
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')
chrome_options.add_argument('--inkognito')

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the login page
    driver.maximize_window()
    driver.get('https://practicetestautomation.com/practice-test-login/')  # Replace with the actual login URL


    time.sleep(5)
    # Find the username and password input fields and login button
    username_field = driver.find_element(By.CSS_SELECTOR, "input[name='username']")  # Update with the actual selector
    password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")  # Update with the actual selector
    login_button = driver.find_element(By.CSS_SELECTOR, "button[id='submit']")  # Update with the actual selector

    # Input credentials
    username_field.send_keys('student')  # Replace with your username
    password_field.send_keys('Password123')  # Replace with your password

    # Click the login button
    login_button.click()

    # Wait for the page to load and verify login by checking for a specific element
    element_after_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".post-title"))  # Update with the actual selector
    )

    # Get the text of the element
    text_after_login = element_after_login.text
    print("Text after login:", text_after_login)
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()