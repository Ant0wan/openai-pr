import subprocess
from github import Github


def get_repository_url():
    remote_url = subprocess.check_output(
        ['git', 'config', '--get', 'remote.origin.url']).decode().strip()
    repository_url = remote_url.replace(".git", "")
    return repository_url


def get_diff(url):
    url_parts = url.split("/")
    repository = "/".join(url_parts[-4:-2])
    pull_request_number = int(url_parts[-1])
    g = Github()
    repo = g.get_repo(repository)
    pull_request = repo.get_pull(pull_request_number)
    diff_text = pull_request.diff()
    return diff_text
