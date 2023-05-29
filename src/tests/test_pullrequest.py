import unittest
from unittest.mock import patch, MagicMock

from ghkit.pullrequest import PullRequest
from configuration.preflight import Env


class TestPullRequest(unittest.TestCase):
    def setUp(self):
        # Mock the environment variables
        self.mock_env = MagicMock(Env)
        self.mock_env.vars = {
            'GITHUB_BRANCH': 'test-branch'
        }

    @patch('ghkit.pullrequest.subprocess')
    def test_repository_url(self, mock_subprocess):
        # Mock the subprocess.check_output() call
        mock_subprocess.check_output.return_value = b'git@github.com:owner/repo.git'

        # Create a PullRequest instance
        pull_request = PullRequest('github_token', self.mock_env)

        # Assert the repository URL
        self.assertEqual(
            pull_request._repository_url(),
            'git@github.com:owner/repo')

    @patch('ghkit.pullrequest.Github')
    def test_repository(self, mock_github):
        # Create a mock repository object
        mock_repository = MagicMock()
        mock_github.return_value.get_repo.return_value = mock_repository

        # Create a PullRequest instance
        pull_request = PullRequest('github_token', self.mock_env)

        # Assert the repository object
        self.assertEqual(
            pull_request._repository(
                mock_github,
                'git@github.com:owner/repo'),
            mock_repository)

    @patch('ghkit.pullrequest.Repository')
    def test_pulls(self, mock_repository):
        # Create a mock pull request object
        mock_pull_request = MagicMock()
        mock_pull_request.totalCount = 1
        mock_pull_request.__getitem__.return_value = mock_pull_request

        # Mock the get_pulls() method
        mock_repository.return_value.get_pulls.return_value = mock_pull_request

        # Create a PullRequest instance
        pull_request = PullRequest('github_token', self.mock_env)

        # Assert the pull request object
        self.assertEqual(
            pull_request._pulls(
                mock_repository,
                'test-branch'),
            mock_pull_request)

    @patch('ghkit.pullrequest.PullRequest._pulls')
    def test_diff(self, mock_pulls):
        # Create a mock file object
        mock_file = MagicMock()
        mock_file.patch = '@@ -10,7 +10,7 @@ def update_description(self, new_description):\n'

        # Mock the get_files() method
        mock_pulls.return_value.get_files.return_value = [mock_file]

        # Create a PullRequest instance
        pull_request = PullRequest('github_token', self.mock_env)

        # Call the diff() method
        diff = pull_request.diff()

        # Assert the diff content
        self.assertEqual(
            diff, '@@ -10,7 +10,7 @@ def update_description(self, new_description):\n')

    @patch('ghkit.pullrequest.PullRequest._pulls')
    def test_update_description(self, mock_pulls):
        # Create a PullRequest instance
        pull_request = PullRequest('github_token', self.mock_env)

        # Call the update_description() method
        new_description = "Updated pull request description"
        pull_request.update_description(new_description)

        # Assert the description update
        mock_pulls.assert_called_once()
        mock_pulls.return_value.edit.assert_called_once_with(
            body=new_description)


if __name__ == '__main__':
    unittest.main()
