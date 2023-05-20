import subprocess
from github import Github


def get_repository_url():
    remote_url = subprocess.check_output(
        ['git', 'config', '--get', 'remote.origin.url']).decode().strip()
    repository_url = remote_url.replace(".git", "")
    return repository_url


def get_current_branch():
    return subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')


def get_owner_and_repo():
    remote_url = get_repository_url()
    parts = remote_url.split('/')
    owner = parts[-2]
    repo = parts[-1].rstrip('.git')
    return owner, repo


def get_pull_request_number():
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
    pull_request = get_pull_request_number()
    if pull_request is None:
        return "No open pull request found for the current branch."
    else:
        diff = pull_request.diff()
        return diff
