#!/usr/bin/python3
""" Search API for id and name """

import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ''}

    res = requests.post(url, data=q)

    try:
        obj = res.json()
        if len(obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(obj.get('id'), obj.get('name')))
    except Exception:
        print('Not a valid JSON')
