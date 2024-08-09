# src/oxylabs/oxylabs_automation.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def fetch_oxylabs_product_page():
    """
    Automates the browser to fetch the title and URL of Oxylabs' products page.
    
    Returns:
        tuple: A tuple containing the page title and current URL.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.maximize_window()
    driver.get("https://sandbox.oxylabs.io/products")
    
    title = driver.title
    current_url = driver.current_url
    
    driver.quit()
    
    return title, current_url

if __name__ == "__main__":
    title, url = fetch_oxylabs_product_page()
    print(f"Application title is: {title}")
    print(f"Application URL is: {url}")
