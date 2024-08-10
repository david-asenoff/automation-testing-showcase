from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')
chrome_options.add_argument('--headless=new')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.oxylabs.io/")
print(driver.page_source)
driver.quit()