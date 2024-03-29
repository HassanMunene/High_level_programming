#!/usr/bin/python3
"""
this script will list the last 10 commits
made in a repository of a certain user both the
repository and the user are specified in the cli
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repo/owner/commits'
    response = requests.get(url)
    json_resp = response.json()

    for commit in json_resp[:10]:
        commit_data = commit['commit']
        sha = commit_data.get('sha')
        author = commit_data.get('author').get('name')
        print(f"{sha}: {author}")
