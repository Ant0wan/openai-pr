"""
This module provides functions for interacting with a remote Git repository and retrieving information about open pull requests.

It relies on the `requests`, `subprocess`, and `github` libraries.

Functions:
    - get_repository_url(): Retrieves the URL of the remote repository.
    - get_current_branch(): Retrieves the name of the current Git branch.
    - get_owner_and_repo(): Parses the owner and repository name from the remote repository URL.
    - get_pull_request(): Retrieves the open pull request associated with the current branch.
    - get_pull_request_diff(): Retrieves the diff content of the open pull request associated with the current branch.
"""
import requests
import subprocess
from github import Github


def get_repository_url():
    """
    Retrieves the URL of the remote repository.

    Returns:
        str: The URL of the remote repository.
    """
    remote_url = subprocess.check_output(
        ['git', 'config', '--get', 'remote.origin.url']).decode().strip()
    repository_url = remote_url.replace(".git", "")
    return repository_url


def get_current_branch():
    """
    Retrieves the name of the current Git branch.

    Returns:
        str: The name of the current branch.
    """
    return subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')


def get_owner_and_repo():
    """
    Parses the owner and repository name from the remote repository URL.

    Returns:
        Tuple[str, str]: A tuple containing the owner and repository name.
    """
    remote_url = get_repository_url()
    parts = remote_url.split('/')
    owner = parts[-2]
    repo = parts[-1].rstrip('.git')
    return owner, repo


def get_pull_request():
    """
    Retrieves the open pull request associated with the current branch.

    Returns:
        github.PullRequest.PullRequest or None: The open pull request or None if not found.
    """
    g = Github()
    branch_name = get_current_branch()
    owner, repo = get_owner_and_repo()
    repository = g.get_repo(f'{owner}/{repo}')
    pull_requests = repository.get_pulls(
        state='open', head=f'{repository.owner.login}:{branch_name}')

    if pull_requests.totalCount == 0:
        return None
    else:
        pr = pull_requests[0]
        return pr


def get_pull_request_diff():
    """
    Retrieves the diff content of the open pull request associated with the current branch.

    Returns:
        str: The diff content of the open pull request, or a message if no pull request is found.
    """
    pull_request = get_pull_request()

    if pull_request is None:
        return "No open pull request found for the current branch."
    else:
        diff_url = pull_request.diff_url
        response = requests.get(diff_url)
        diff_content = response.text
        return diff_content
