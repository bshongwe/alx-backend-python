#!/usr/bin/env python3
"""
Module: tests - integration & unittests
"""
import unittest
import json


class TestGitHubRepos(unittest.TestCase):
    def setUp(self):
        """Load the JSON data from the file
        """
        with open('github_repos.json', 'r') as file:
            self.data = json.load(file)

    def test_data_loaded(self):
        """Test if the data is loaded properly
        """
        self.assertIsNotNone(self.data)
        self.assertIsInstance(self.data, list)
        self.assertTrue(len(self.data) > 0)

    def test_repo_attributes(self):
        """Test if each repository object has all the
        required attributes
        """
        for repo in self.data:
            self.assertIn('id', repo)
            self.assertIsInstance(repo['id'], int)
            self.assertIn('name', repo)
            self.assertIsInstance(repo['name'], str)
            self.assertIn('full_name', repo)
            self.assertIsInstance(repo['full_name'], str)
            self.assertIn('html_url', repo)
            self.assertIsInstance(repo['html_url'], str)
            self.assertIn('description', repo)
            self.assertIsInstance(repo['description'], (str, type(None)))
            self.assertIn('fork', repo)
            self.assertIsInstance(repo['fork'], bool)
            self.assertIn('created_at', repo)
            self.assertIsInstance(repo['created_at'], str)
            self.assertIn('updated_at', repo)
            self.assertIsInstance(repo['updated_at'], str)
            self.assertIn('pushed_at', repo)
            self.assertIsInstance(repo['pushed_at'], str)
            self.assertIn('size', repo)
            self.assertIsInstance(repo['size'], int)
            self.assertIn('stargazers_count', repo)
            self.assertIsInstance(repo['stargazers_count'], int)
            self.assertIn('watchers_count', repo)
            self.assertIsInstance(repo['watchers_count'], int)
            self.assertIn('language', repo)
            self.assertIsInstance(repo['language'], (str, type(None)))
            self.assertIn('has_issues', repo)
            self.assertIsInstance(repo['has_issues'], bool)
            self.assertIn('has_projects', repo)
            self.assertIsInstance(repo['has_projects'], bool)
            self.assertIn('has_downloads', repo)
            self.assertIsInstance(repo['has_downloads'], bool)
            self.assertIn('has_wiki', repo)
            self.assertIsInstance(repo['has_wiki'], bool)
            self.assertIn('has_pages', repo)
            self.assertIsInstance(repo['has_pages'], bool)
            self.assertIn('forks_count', repo)
            self.assertIsInstance(repo['forks_count'], int)
            self.assertIn('archived', repo)
            self.assertIsInstance(repo['archived'], bool)
            self.assertIn('disabled', repo)
            self.assertIsInstance(repo['disabled'], bool)
            self.assertIn('open_issues_count', repo)
            self.assertIsInstance(repo['open_issues_count'], int)
            self.assertIn('default_branch', repo)
            self.assertIsInstance(repo['default_branch'], str)
            self.assertIn('permissions', repo)
            self.assertIsInstance(repo['permissions'], dict)
            self.assertIn('admin', repo['permissions'])
            self.assertIsInstance(repo['permissions']['admin'], bool)
            self.assertIn('push', repo['permissions'])
            self.assertIsInstance(repo['permissions']['push'], bool)
            self.assertIn('pull', repo['permissions'])
            self.assertIsInstance(repo['permissions']['pull'], bool)

    def test_repo_integration(self):
        """Integration test to verify the structure
        and content of the JSON data
        """
        for repo in self.data:
            """Verify required attributes
            """
            self.assertIn('id', repo)
            self.assertIn('name', repo)
            self.assertIn('full_name', repo)
            self.assertIn('html_url', repo)
            self.assertIn('fork', repo)
            self.assertIn('created_at', repo)
            self.assertIn('updated_at', repo)
            self.assertIn('pushed_at', repo)
            self.assertIn('size', repo)
            self.assertIn('stargazers_count', repo)
            self.assertIn('watchers_count', repo)
            self.assertIn('language', repo)
            self.assertIn('has_issues', repo)
            self.assertIn('has_projects', repo)
            self.assertIn('has_downloads', repo)
            self.assertIn('has_wiki', repo)
            self.assertIn('has_pages', repo)
            self.assertIn('forks_count', repo)
            self.assertIn('archived', repo)
            self.assertIn('disabled', repo)
            self.assertIn('open_issues_count', repo)
            self.assertIn('default_branch', repo)
            self.assertIn('permissions', repo)

            """Verify permissions
            """
            self.assertIn('admin', repo['permissions'])
            self.assertIn('push', repo['permissions'])
            self.assertIn('pull', repo['permissions'])


if __name__ == "__main__":
    """Start unittest
    """
    unittest.main()

