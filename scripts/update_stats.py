#!/usr/bin/env python3
"""
GitHub Statistics Update Script

This script fetches GitHub statistics and updates the README.md file.
It's designed to run as a GitHub Action but can also be run manually.
"""

import os
import sys
from datetime import datetime
from github import Github, GithubException


def get_github_stats(username: str, token: str) -> dict:
    """
    Fetch GitHub statistics for a given user.

    Args:
        username: GitHub username
        token: GitHub API token

    Returns:
        Dictionary containing user statistics
    """
    try:
        g = Github(token)
        user = g.get_user(username)

        stats = {
            'total_repos': user.public_repos,
            'total_stars': sum(repo.stargazers_count for repo in user.get_repos()),
            'total_forks': sum(repo.forks_count for repo in user.get_repos()),
            'total_commits': 0,  # This would require more complex calculation
            'followers': user.followers,
            'following': user.following,
        }

        return stats

    except GithubException as e:
        print(f"Error fetching GitHub stats: {e}")
        sys.exit(1)


def update_readme_stats(stats: dict) -> None:
    """
    Update the README.md file with latest statistics.

    Args:
        stats: Dictionary containing GitHub statistics
    """
    readme_path = 'README.md'

    if not os.path.exists(readme_path):
        print(f"README.md not found at {readme_path}")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update timestamp
    timestamp = datetime.utcnow().strftime('%B %Y')
    content = content.replace(
        '<sub>Last updated:',
        f'<sub>Last updated: {timestamp} |'
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("README.md updated successfully!")
    print(f"Stats: {stats}")


def main():
    """Main execution function."""
    username = os.environ.get('GITHUB_REPOSITORY', '').split('/')[0]
    if not username:
        username = 'olaflaitinen'

    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("GITHUB_TOKEN environment variable not set")
        sys.exit(1)

    print(f"Fetching stats for user: {username}")
    stats = get_github_stats(username, token)

    print("Updating README...")
    update_readme_stats(stats)

    print("Done!")


if __name__ == '__main__':
    main()
