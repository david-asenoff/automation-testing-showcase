from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
from datetime import datetime

def get_status_code(url):
     try:
        response = requests.get(url)
        return response.status_code
     except requests.exceptions.RequestException as e:
         print(f"Error fetching the URL: {e}")
         return None
     
def open_site_and_make_screenshoot(url, screenshot_path):

    chrome_options = Options()
    chrome_options.add_argument('--disable-search-engine-choice-screen')

    driver = webdriver.Chrome(service=Service(), options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)

        css_selector = 'div#crbn'
        element = driver.find_element(By.ID, "crbn")
        #driver.implicitly_wait(10)

        if element:
            print(f"element:___{element.get_attribute('outerHTML')}___")
        else:
            print('none')

        #ActionChains(driver).move_to_element(element).click(element).perform()
        driver.execute_script("arguments[0].scrollIntoView()", element)
        #driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)

        # element.click()
        # time.sleep(5)

        driver.save_screenshot(screenshot_path)
        print(f"Saved at: {screenshot_path}")
    finally:
        driver.quit()

url = 'https://jsonplaceholder.typicode.com/guide/'
status_code = get_status_code(url)

if status_code:
    print(f"Status code: {status_code}")

current_time = datetime.now()
timestamp = current_time.strftime("%Y%m%d_%H%M%S")

screenshot_path = f"screenshot_{timestamp}.png"
open_site_and_make_screenshoot(url, screenshot_path)