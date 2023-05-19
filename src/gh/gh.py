from github import Github


def print_user_repos(access_token):
    g = Github(access_token)

    for repo in g.get_user().get_repos():
        print(repo.name)
