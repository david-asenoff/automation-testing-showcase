import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def make_api_requst(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
api_url = 'https://swapi.dev/api/people/'


json_data = make_api_requst(api_url)
json_data_format = json.dumps(json_data, indent=2)

if json_data:
    # print(json.dumps(json_data, indent=2))
    data = json.loads(json_data_format)
    num_items = len(data['results'])
    print(f"People results count: {num_items}")


chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get('https://swapi.dev/api/people/')
finally:
    driver.quit()