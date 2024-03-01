#!/usr/bin/python3
""" My GitHub! using `GitHub API` """

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(username, password))
    try:
        obj = r.json()
        print(obj.get('id'))
    except Exception:
        print(None)
