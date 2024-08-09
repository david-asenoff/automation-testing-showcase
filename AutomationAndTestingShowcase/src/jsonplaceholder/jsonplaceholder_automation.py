# src/jsonplaceholder/jsonplaceholder_automation.py

import requests

def get_posts():
    """
    Fetches posts from JSONPlaceholder API.
    
    Returns:
        list: A list of posts retrieved from the API.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        return response.json()
    else:
        return []

if __name__ == "__main__":
    posts = get_posts()
    print(f"Retrieved {len(posts)} posts")
