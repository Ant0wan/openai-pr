import requests
import subprocess
from github import Github


class PullRequest:

    def __init__(self, github_token: str):
        self.__g = Github(github_token)
        self.__url = self._repository_url()
        self.__repository = self._repository(self.__g, self.__url)
#        self.__branch = self._branch()
#        self.__pulls = self._pulls()


    def __str__(self):
        return f"Github object: {self.__g}, \
Url: {self.__url}, \
Repository: {self.__repository}"


    @staticmethod
    def _repository_url():
        remote = subprocess.check_output(
            ['git', 'config', '--get', 'remote.origin.url']).decode().strip()
        return remote.replace(".git", "")

    @staticmethod
    def _repository(g, url):
        parts = url.split('/')
        owner = parts[-2]
        repo = parts[-1].rstrip('.git')
        return g.get_repo(f'{owner}/{repo}')


    @staticmethod
    def _branch():
        return subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')

    @staticmethod
    def _pulls():
        pull_requests = self.__repository.repository.get_pulls(
            state='open', head=f'{self.__repository.owner.login}:{self.__branch}')
        if pull_requests.totalCount == 0:
            return None
        else:
            pr = pull_requests[0]
            return pr


    def diff(self):
        diff_url = self.__pulls.diff_url
        response = requests.get(diff_url)
        diff_content = response.text
        return diff_content


#def change_pull_request_description(pr_number, new_description):
#    g = Github()
#    owner, repo = get_owner_and_repo()
#    repository = g.get_repo(f'{owner}/{repo}')
#
#    pull_request = repository.get_pull(pr_number)
#    pull_request.edit(body=new_description)
