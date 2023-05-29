import unittest
from unittest.mock import MagicMock, patch
from github import Github
from ghkit.pullrequest import PullRequest


class TestPullRequest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Mock the subprocess.check_output() method
        cls.mock_check_output = MagicMock(
            return_value=b'https://github.com/owner/repo')
        patch('subprocess.check_output', cls.mock_check_output).start()

        # Create a mock GitHub instance
        cls.mock_github = MagicMock(spec=Github)
        cls.mock_repo = cls.mock_github.get_repo.return_value

    @classmethod
    def tearDownClass(cls):
        # Stop patching subprocess.check_output()
        patch.stopall()

    def setUp(self):
        # Create a mock environment variable loader (Env) instance
        self.mock_env = MagicMock()
        self.mock_env.vars = {
            'GITHUB_BRANCH': 'test-branch'
        }

    def test_init(self):
        # Mock the _repository_url() method
        mock_url = 'https://github.com/owner/repo'
        with patch.object(PullRequest, '_repository_url', return_value=mock_url):
            # Create a PullRequest instance
            pull_request = PullRequest('github_token', self.mock_env)

        # Assert the initialization
        self.assertEqual(pull_request._PullRequest__url, mock_url)
        self.assertEqual(pull_request._PullRequest__branch, 'test-branch')
        self.mock_github.get_repo.assert_called_once_with('owner/repo')
        self.mock_repo.get_pulls.assert_called_once_with(
            state='open', head='owner:test-branch')

    def test_diff(self):
        # Mock the _pulls() method
        mock_pulls = MagicMock()
        mock_file = MagicMock()
        mock_file.patch = 'diff_content'
        mock_pulls.get_files.return_value = [mock_file]
        with patch.object(PullRequest, '_pulls', return_value=mock_pulls):
            # Create a PullRequest instance
            pull_request = PullRequest('github_token', self.mock_env)

        # Call the diff() method
        diff_content = pull_request.diff()

        # Assert the diff content
        self.assertEqual(diff_content, 'diff_content')

    def test_update_description(self):
        # Mock the _pulls() method
        mock_pulls = MagicMock()
        with patch.object(PullRequest, '_pulls', return_value=mock_pulls):
            # Create a PullRequest instance
            pull_request = PullRequest('github_token', self.mock_env)

        # Call the update_description() method
        new_description = "Updated pull request description"
        pull_request.update_description(new_description)

        # Assert the description update
        mock_pulls.edit.assert_called_once_with(body=new_description)
