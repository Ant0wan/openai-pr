import unittest
from unittest.mock import MagicMock, patch
from ghkit.pullrequest import PullRequest


class TestPullRequest(unittest.TestCase):
    def setUp(self):
        self.mock_env = MagicMock()

    @patch('ghkit.pullrequest.Github')
    def test_init(self, mock_github):
        pull_request = PullRequest('github_token', self.mock_env)
        mock_github.assert_called_once_with('github_token')

    @patch('ghkit.pullrequest.Github')
    def test_repository_url(self, mock_github):
        mock_repo = mock_github().get_repo().html_url
        pull_request = PullRequest('github_token', self.mock_env)
        self.assertEqual(pull_request.repository_url, mock_repo)

    @patch('ghkit.pullrequest.Github')
    def test_pulls(self, mock_github):
        mock_pulls = mock_github().get_repo().get_pulls.return_value
        pull_request = PullRequest('github_token', self.mock_env)
        self.assertEqual(pull_request.get_pulls(), mock_pulls)

    @patch('ghkit.pullrequest.Github')
    def test_update_description(self, mock_github):
        pull_request = PullRequest('github_token', self.mock_env)
        pull_request.update_description('new_description')
        mock_github().get_repo().get_pull.return_value.edit.assert_called_once_with(
            body='new_description'
        )

    @patch('ghkit.pullrequest.Github')
    def test_diff(self, mock_github):
        mock_files = mock_github().get_repo().get_pull.return_value.get_files.return_value
        pull_request = PullRequest('github_token', self.mock_env)
        pull_request.diff()
        mock_github().get_repo().get_pull.assert_called_once_with(pull_request.pull_number)
        mock_files.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()

