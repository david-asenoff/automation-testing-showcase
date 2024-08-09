# src/swapi/swapi_automation.py

import requests

def get_character(character_id):
    """
    Fetches a character from the Star Wars API (SWAPI).
    
    Args:
        character_id (int): The ID of the character to fetch.
    
    Returns:
        dict: The character data retrieved from the API.
    """
    url = f"https://swapi.dev/api/people/{character_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {}

if __name__ == "__main__":
    character = get_character(1)
    print(f"Character name: {character.get('name')}")
