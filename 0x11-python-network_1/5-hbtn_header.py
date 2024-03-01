#!/usr/bin/python3
""" Response header value """

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    res = requests.get(url)
    res_headers = res.headers

    print(res_headers.get('X-Request-Id'))
