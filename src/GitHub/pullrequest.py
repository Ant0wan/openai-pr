"""
This module provides a class for interacting with GitHub Pull Requests.

The module includes a class, 'PullRequest', that can be used to work with GitHub Pull Requests. The 'PullRequest'
class requires a GitHub token for authentication. The class provides methods for retrieving the repository URL,
fetching the repository, getting the current branch, retrieving open pull requests for the branch, getting the
diff of a pull request, and updating the description of a pull request.

Example usage:
--------------
github_token = "your_github_token"
pull_request = PullRequest(github_token)

# Print information about the pull request
print(pull_request)

# Get the diff of the pull request
diff = pull_request.diff()

# Update the description of the pull request
new_description = "Updated pull request description"
pull_request.update_description(new_description)

"""
import os
import requests
import subprocess
import logging
from github import Github


class PullRequest:
    """
    A class for interacting with GitHub Pull Requests.

    The 'PullRequest' class requires a GitHub token for authentication. It provides methods for retrieving the
    repository URL, fetching the repository, getting the current branch, retrieving open pull requests for the
    branch, getting the diff of a pull request, and updating the description of a pull request.

    Example usage:
    --------------
    github_token = "your_github_token"
    pull_request = PullRequest(github_token)

    # Print information about the pull request
    print(pull_request)

    # Get the diff of the pull request
    diff = pull_request.diff()

    # Update the description of the pull request
    new_description = "Updated pull request description"
    pull_request.update_description(new_description)
    """

    def __init__(self, github_token: str):
        """
        Initialize the PullRequest object with the provided GitHub token.

        Args:
            github_token (str): The GitHub token for authentication.

        Returns:
            None
        """
        self.__g = Github(github_token)
        self.__url = self._repository_url()
        self.__repository = self._repository(self.__g, self.__url)
        self.__branch = self._branch()
        self.__pulls = self._pulls(self.__repository, self.__branch)

    def __str__(self):
        """
        Return a string representation of the PullRequest object.

        Returns:
            str: A string representation of the PullRequest object.
        """
        return f"Github object: {self.__g}, \
Url: {self.__url}, \
Repository: {self.__repository}, \
Branch: {self.__branch}, \
PullRequest: {self.__pulls}"

    @staticmethod
    def _repository_url():
        """
        Get the URL of the repository.

        Returns:
            str: The URL of the repository.

        Raises:
            subprocess.CalledProcessError: If the 'git' command fails.
        """
        remote = subprocess.check_output(
            ['git', 'config', '--get', 'remote.origin.url']).decode().strip()
        return remote.replace(".git", "")

    @staticmethod
    def _repository(g, url):
        """
        Fetch the repository object from GitHub.

        Args:
            g (Github): The GitHub object for authentication.
            url (str): The URL of the repository.

        Returns:
            Repository: The fetched repository object.

        Raises:
            IndexError: If the URL is not valid.
        """
        parts = url.split('/')
        owner = parts[-2]
        repo = parts[-1]
        return g.get_repo(f'{owner}/{repo}')

    @staticmethod
    def _branch():
        """
        Get the current branch name.

        Returns:
            str: The current branch name.

        Raises:
            subprocess.CalledProcessError: If the 'git' command fails.
        """
        return os.environ.get('GITHUB_BRANCH')

    @staticmethod
    def _pulls(repo, branch):
        """
        Retrieve open pull requests for the specified branch.

        Args:
            repo (Repository): The repository object.
            branch (str): The branch name.

        Returns:
            PullRequest: The first open pull request for the branch, or None if no open pull requests exist.
        """
        pull_requests = repo.get_pulls(
            state='open', head=f'{repo.owner.login}:{branch}')
        if pull_requests.totalCount == 0:
            return None
        else:
            pr = pull_requests[0]
            return pr

    def diff(self):
        """
        Get the diff of the pull request.

        Returns:
            str: The diff of the pull request.

        Raises:
            requests.exceptions.RequestException: If the request to retrieve the diff fails.
        """
        files = self.__pulls.get_files()
        logging.info(files)
        diff_content = ""
        for file in files:
            diff_content += file.patch
        logging.info("====Reponse:")
        logging.info(diff_content)
        return diff_content

    def update_description(self, new_description):
        """
        Update the description of the pull request.

        Args:
            new_description (str): The new description for the pull request.

        Returns:
            None
        """
        self.__pulls.edit(body=new_description)
