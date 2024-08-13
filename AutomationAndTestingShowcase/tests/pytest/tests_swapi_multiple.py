import requests

BASE_URL = "https://swapi.dev/api/"

def get_data(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    return response.json()

def test_people_endpoint_status_code():
    response = requests.get(f"{BASE_URL}people/")
    assert response.status_code == 200

def test_planets_endpoint_status_code():
    response = requests.get(f"{BASE_URL}planets/")
    assert response.status_code == 200

def test_starships_endpoint_status_code():
    response = requests.get(f"{BASE_URL}starships/")
    assert response.status_code == 200

def test_vehicles_endpoint_status_code():
    response = requests.get(f"{BASE_URL}vehicles/")
    assert response.status_code == 200

def test_species_endpoint_status_code():
    response = requests.get(f"{BASE_URL}species/")
    assert response.status_code == 200

def test_film_endpoint_status_code():
    response = requests.get(f"{BASE_URL}films/")
    assert response.status_code == 200

def test_people_count():
    data = get_data("people/")
    assert data["count"] > 0

def test_planets_count():
    data = get_data("planets/")
    assert data["count"] > 0

def test_starships_count():
    data = get_data("starships/")
    assert data["count"] > 0

def test_vehicles_count():
    data = get_data("vehicles/")
    assert data["count"] > 0

def test_species_count():
    data = get_data("species/")
    assert data["count"] > 0

def test_films_count():
    data = get_data("films/")
    assert data["count"] > 0

def test_people_name():
    data = get_data("people/1/")
    assert data["name"] == "Luke Skywalker"

def test_planets_name():
    data = get_data("planets/1/")
    assert data["name"] == "Tatooine"

def test_starships_name():
    data = get_data("starships/2/")
    assert data["name"] == "CR90 corvette"

def test_vehicles_name():
    data = get_data("vehicles/4/")
    assert data["cost_in_credits"] == "150000"

def test_species_name():
    data = get_data("species/1/")
    assert data["name"] == "Human"

def test_films_title():
    data = get_data("films/1/")
    assert data["title"] == "A New Hope"

# To run tests, use the command: pytest test_swapi.py