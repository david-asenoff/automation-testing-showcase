import requests
import json
from selenium import webdriver

driver = webdriver.Chrome()

try:   
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'title_test',
        'body': 'body_test',
        'userId': 1,
    }

    headers_custom = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    
    response = requests.post(url, json=data, headers=headers_custom)

    if response.status_code == 200:
        print(f"Response: : {response.json()}")
    else:
        print(f"Response: : {response.text}")
        
finally:
    driver.quit()