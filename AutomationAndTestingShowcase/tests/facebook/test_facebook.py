# tests/facebook/test_facebook.py

import unittest
from src.facebook.facebook_automation import fetch_facebook_title_and_url

class TestFacebookAutomation(unittest.TestCase):

    def test_facebook_title_and_url(self):
        title, url = fetch_facebook_title_and_url()
        self.assertIn("Facebook", title)
        self.assertEqual(url, "https://www.facebook.com/")

if __name__ == "__main__":
    unittest.main()
