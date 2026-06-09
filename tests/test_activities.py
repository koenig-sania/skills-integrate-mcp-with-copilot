import sys
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from app import app


class GitHubSkillsActivityTests(unittest.TestCase):
    def test_github_skills_activity_is_available(self):
        with TestClient(app) as client:
            response = client.get("/activities")

        self.assertEqual(response.status_code, 200)

        activities = response.json()
        self.assertIn("GitHub Skills", activities)

        activity = activities["GitHub Skills"]
        self.assertTrue(activity["description"])
        self.assertGreater(activity["max_participants"], 0)

    def test_github_skills_signup_is_supported(self):
        with TestClient(app) as client:
            response = client.post("/activities/GitHub%20Skills/signup?email=test@mergington.edu")

        self.assertEqual(response.status_code, 200)
        self.assertIn("test@mergington.edu", response.json()["message"])


if __name__ == "__main__":
    unittest.main()
