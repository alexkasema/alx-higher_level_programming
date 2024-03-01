#!/usr/bin/python3
""" Time for an interview! """

import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    res = requests.get(url)

    try:
        data = res.json()
        for i, obj in enumerate(data):
            print('{}: {}'.format(obj.get('sha'),
                                  obj.get('commit').get('author').get('name')))
            if i == 9:
                break
    except Exception:
        pass
