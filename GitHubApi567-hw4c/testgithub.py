#Ryan Feroz SSW567 HW04c

import unittest
from unittest.mock import patch
import github

class TestGitHubAPI(unittest.TestCase):

    @patch('github.requests.get')
    def test_get_repos(self, mock_get):
        """Test fetching user repositories"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]

        repos = github.get_repos("testuser")
        self.assertEqual(repos, ["Repo1", "Repo2"])

    @patch('github.requests.get')
    def test_get_commit_count(self, mock_get):
        """Test fetching commit count for a repo"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{}, {}, {}]  #Mock 3 commits

        commit_count = github.get_commit_count("testuser", "Repo1")
        self.assertEqual(commit_count, 3)

    @patch('github.requests.get')
    def test_get_repo_commit_info(self, mock_get):
        """Test overall function for fetching repo commit info"""

        def mock_response(url, *args, **kwargs):
            if url == "https://api.github.com/users/testuser/repos":
                return MockResponse([
                    {"name": "Repo1"}
                ], 200)
            elif url == "https://api.github.com/repos/testuser/Repo1/commits":
                return MockResponse([{}, {}, {}], 200)  #3 commits
            return MockResponse(None, 404)

        mock_get.side_effect = mock_response

        expected = ["Repo: Repo1 # of commits: 3"]
        self.assertEqual(github.get_repo_commit_info("testuser"), expected)

class MockResponse:
    """Mock Response class for simulating API responses"""
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

if __name__ == '__main__':
    unittest.main()
