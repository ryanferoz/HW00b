#Ryan Feroz SSW567 HW04a
import requests
import json

def get_repos(user_id):
    """Fetch the list of repositories for a given user."""
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return None  #User does not exist or API error

    repos = response.json()
    return [repo["name"] for repo in repos]

def get_commit_count(user_id, repo_name):
    """Fetch the commit count for a given repository."""
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        return None  #Repository not found or API error

    commits = response.json()
    return len(commits)
def get_repo_commit_info(user_id):
    """Return a list of repositories with their commit count."""
    repos = get_repos(user_id)

    if repos is None:
        return f"Error: Could not retrieve repositories for user {user_id}."

    results = []
    for repo in repos:
        commit_count = get_commit_count(user_id, repo)
        results.append(f"Repo: {repo} # of commits: {commit_count if commit_count is not None else 'Error'}")

    return results

if __name__ == "__main__":
    user_id = input("Enter a GitHub username please: ")
    output = get_repo_commit_info(user_id)
    for line in output:
        print(line)
