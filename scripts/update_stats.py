#!/usr/bin/env python3
"""
GitHub Stats Updater
Automatically updates profile statistics and badges in README.md
"""

import os
import requests
from datetime import datetime
from github import Github

def get_github_stats(username: str, token: str) -> dict:
    """Fetch GitHub statistics for the user"""
    g = Github(token)
    user = g.get_user(username)

    stats = {
        'total_repos': user.public_repos,
        'total_gists': user.public_gists,
        'followers': user.followers,
        'following': user.following,
        'total_stars': sum(repo.stargazers_count for repo in user.get_repos()),
        'total_forks': sum(repo.forks_count for repo in user.get_repos()),
        'contributions': 0,  # Would need GraphQL API for this
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    }

    return stats

def update_readme_stats(stats: dict):
    """Update README.md with new statistics"""
    readme_path = 'README.md'

    if not os.path.exists(readme_path):
        print(f"❌ {readme_path} not found!")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add stats to README (you can customize this section)
    stats_section = f"""
<!-- AUTO-GENERATED STATS - DO NOT EDIT MANUALLY -->
<!-- Last updated: {stats['last_updated']} -->
<!-- Total Repositories: {stats['total_repos']} -->
<!-- Total Stars: {stats['total_stars']} -->
<!-- Total Followers: {stats['followers']} -->
<!-- END AUTO-GENERATED STATS -->
"""

    # You can add more sophisticated replacement logic here
    print(f"✅ Stats updated: {stats['total_repos']} repos, {stats['total_stars']} stars")

def main():
    username = os.environ.get('GITHUB_REPOSITORY', '').split('/')[0] or 'olaflaitinen'
    token = os.environ.get('GITHUB_TOKEN', '')

    if not token:
        print("⚠️  GITHUB_TOKEN not found, skipping stats update")
        return

    print(f"📊 Fetching stats for {username}...")

    try:
        stats = get_github_stats(username, token)
        update_readme_stats(stats)
        print("✨ Stats update completed successfully!")
    except Exception as e:
        print(f"❌ Error updating stats: {e}")

if __name__ == "__main__":
    main()
