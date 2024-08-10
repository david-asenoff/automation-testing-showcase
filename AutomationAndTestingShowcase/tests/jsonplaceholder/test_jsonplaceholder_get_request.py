import requests
import json
from selenium import webdriver

def make_api_requst(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
api_url = 'https://jsonplaceholder.typicode.com/todos/'
params = {'key': 'value'} 


json_data = make_api_requst(api_url, params)
json_data_format = json.dumps(json_data, indent=2)

if json_data:
    # print(json.dumps(json_data, indent=2))
    data = json.loads(json_data_format)
    num_items = len(data)
    print(f"Number of data entries: {num_items}")


driver = webdriver.Chrome()

try:
    driver.get('https://jsonplaceholder.typicode.com/todos/1')
finally:
    driver.quit()