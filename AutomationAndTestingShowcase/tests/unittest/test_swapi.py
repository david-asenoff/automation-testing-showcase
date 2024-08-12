import unittest
import requests

BASE_URL = "https://swapi.dev/api/"

def get_data(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    return response.json()

class TestSWAPI(unittest.TestCase):

    def test_people_endpoint_status_code(self):
        response = requests.get(f"{BASE_URL}people/")
        self.assertEqual(response.status_code, 200)

    def test_planets_endpoint_status_code(self):
        response = requests.get(f"{BASE_URL}planets/")
        self.assertEqual(response.status_code, 200)

    def test_starships_endpoint_status_code(self):
        response = requests.get(f"{BASE_URL}starships/")
        self.assertEqual(response.status_code, 200)

    def test_vehicles_endpoint_status_code(self):
        response = requests.get(f"{BASE_URL}vehicles/")
        self.assertEqual(response.status_code, 200)

    def test_species_endpoint_status_code(self):
        response = requests.get(f"{BASE_URL}species/")
        self.assertEqual(response.status_code, 200)

    def test_films_endpoint_status_code(self):
        response = requests.get(f"{BASE_URL}films/")
        self.assertEqual(response.status_code, 200)

    def test_people_count(self):
        data = get_data("people/")
        self.assertGreater(data["count"], 0)

    def test_planets_count(self):
        data = get_data("planets/")
        self.assertGreater(data["count"], 0)

    def test_starships_count(self):
        data = get_data("starships/")
        self.assertGreater(data["count"], 0)

    def test_vehicles_count(self):
        data = get_data("vehicles/")
        self.assertGreater(data["count"], 0)

    def test_species_count(self):
        data = get_data("species/")
        self.assertGreater(data["count"], 0)

    def test_films_count(self):
        data = get_data("films/")
        self.assertGreater(data["count"], 0)

    def test_people_name(self):
        data = get_data("people/1/")
        self.assertEqual(data["name"], "Luke Skywalker")

    def test_planets_name(self):
        data = get_data("planets/1/")
        self.assertEqual(data["name"], "Tatooine")

    def test_species_name(self):
        data = get_data("species/1/")
        self.assertEqual(data["name"], "Human")

    def test_films_title(self):
        data = get_data("films/1/")
        self.assertEqual(data["title"], "A New Hope")

    def test_people_valid_keys(self):
        data = get_data("people/1/")
        keys = {"name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_year", "gender", "homeworld", "films", "species", "vehicles", "starships", "created", "edited", "url"}
        self.assertTrue(keys.issubset(data.keys()))

    def test_planets_valid_keys(self):
        data = get_data("planets/1/")
        keys = {"name", "rotation_period", "orbital_period", "diameter", "climate", "gravity", "terrain", "surface_water", "population", "films", "residents", "created", "edited", "url"}
        self.assertTrue(keys.issubset(data.keys()))

    def test_starships_valid_keys(self):
        data = get_data("starships/2/")
        keys = {"name", "model", "manufacturer", "cost_in_credits", "length", "max_atmosphering_speed", "crew", "passengers", "cargo_capacity", "consumables", "hyperdrive_rating", "MGLT", "starship_class", "pilots", "films", "created", "edited", "url"}
        self.assertTrue(keys.issubset(data.keys()))

    def test_vehicles_valid_keys(self):
        data = get_data("vehicles/4/")
        keys = {"name", "model", "manufacturer", "cost_in_credits", "length", "max_atmosphering_speed", "crew", "passengers", "cargo_capacity", "consumables", "vehicle_class", "pilots", "films", "created", "edited", "url"}
        self.assertTrue(keys.issubset(data.keys()))

    def test_species_valid_keys(self):
        data = get_data("species/1/")
        keys = {"name", "classification", "designation", "average_height", "skin_colors", "hair_colors", "eye_colors", "average_lifespan", "homeworld", "language", "people", "films", "created", "edited", "url"}
        self.assertTrue(keys.issubset(data.keys()))

    def test_films_valid_keys(self):
        data = get_data("films/1/")
        keys = {"title", "episode_id", "opening_crawl", "director", "producer", "release_date", "characters", "planets", "starships", "vehicles", "species", "created", "edited", "url"}
        self.assertTrue(keys.issubset(data.keys()))

    def test_people_film_links(self):
        data = get_data("people/1/")
        self.assertGreater(len(data["films"]), 0)

    def test_planets_residents(self):
        data = get_data("planets/1/")
        self.assertGreater(len(data["residents"]), 0)

    def test_species_people(self):
        data = get_data("species/1/")
        self.assertGreater(len(data["people"]), 0)

    def test_films_characters(self):
        data = get_data("films/1/")
        self.assertGreater(len(data["characters"]), 0)

    def test_people_links(self):
        data = get_data("people/1/")
        self.assertTrue(data["homeworld"].startswith(f"{BASE_URL}planets/"))

    def test_planets_links(self):
        data = get_data("planets/1/")
        self.assertTrue(data["residents"][0].startswith(f"{BASE_URL}people/"))

    def test_species_links(self):
        data = get_data("species/1/")
        self.assertTrue(data["homeworld"].startswith(f"{BASE_URL}planets/"))

    def test_films_links(self):
        data = get_data("films/1/")
        self.assertTrue(data["characters"][0].startswith(f"{BASE_URL}people/"))

if __name__ == "__main__":
    unittest.main()