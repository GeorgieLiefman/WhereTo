import unittest
from app import build_application
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"] = "testing"

class TestCourses(unittest.TestCase):
    def setUp(self): 
        self.app = build_application()
        self.client = self.app.test_client()

    # Testing to see that the login page loads correctly
    def test_login_page_loads(self):
        # we use the client to make a request
        response = self.client.get("/login")
        # Now we can perform tests on the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login Below!", response.data)

    # Testing to see that the signup page loads correctly
    def test_homepage_loads(self):
        response = self.client.get("/sign_up")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up Below!', response.data)





    
   
if __name__ == "__main__":
    unittest.main()