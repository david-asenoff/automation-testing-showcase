# src/facebook/facebook_automation.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def fetch_facebook_title_and_url():
    """
    Automates the browser to fetch the title and URL of Facebook's homepage.
    
    Returns:
        tuple: A tuple containing the page title and current URL.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.maximize_window()
    driver.get("http://www.facebook.com")
    
    title = driver.title
    current_url = driver.current_url
    
    driver.quit()
    
    return title, current_url

if __name__ == "__main__":
    title, url = fetch_facebook_title_and_url()
    print(f"Application title is: {title}")
    print(f"Application URL is: {url}")
