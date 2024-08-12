import requests
from bs4 import BeautifulSoup

url = 'https://github.com/login'

# Send a GET request
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

# Check if the request was successful (status code 200)
if resp.status_code == 200:
    csrf_token = soup.find("input",{"name":"authenticity_token"}).get("value")
    timestamp = soup.find("input",{"name":"timestamp"}).get("value")
    timestamp_secret = soup.find("input",{"name":"timestamp_secret"}).get("value")
else:
    print(f'Authentication failed. Status code: {resp.status_code}')


print("csrf token is ", csrf_token)
print("timestamp is ", timestamp)
print("timestamp secret is ", timestamp_secret)