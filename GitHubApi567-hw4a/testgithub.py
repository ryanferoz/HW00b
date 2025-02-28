#Ryan Feroz SSW567 HW04a
import unittest
from unittest.mock import patch
import github

class TestGitHub(unittest.TestCase):

    @patch('requests.get')
    def test_get_repos_success(self, mock_get):
        """Test fetching repositories successfully."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"name": "Repo1"}, {"name": "Repo2"}]
        self.assertEqual(github.get_repos("testuser"), ["Repo1", "Repo2"])

    @patch('requests.get')
    def test_get_commit_count_success(self, mock_get):
        """Test fetching commit count successfully."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{}] * 5  #5 commits
        self.assertEqual(github.get_commit_count("testuser", "Repo1"), 5)

    @patch('requests.get')
    def test_get_repo_commit_info(self, mock_get):
        """Test overall function for fetching repo commit info."""
        def side_effect(url):
            """Mock API responses based on URL."""
            if url == "https://api.github.com/users/testuser/repos":
                mock_response = unittest.mock.Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = [{"name": "Repo1"}]  #Return repo list
                return mock_response
            elif url == "https://api.github.com/repos/testuser/Repo1/commits":
                mock_response = unittest.mock.Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = [{}] * 3  #Simulate 3 commits
                return mock_response
            else:
                mock_response = unittest.mock.Mock()
                mock_response.status_code = 404  #Simulating not found
                return mock_response

        mock_get.side_effect = side_effect
        expected = ["Repo: Repo1 # of commits: 3"]
        self.assertEqual(github.get_repo_commit_info("testuser"), expected)


if __name__ == "__main__":
    unittest.main()
