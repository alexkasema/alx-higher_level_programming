#!/usr/bin/python3
""" Response header value """

from urllib.request import urlopen
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    with urlopen(url) as response:
        header = response.info()
        print(header.get('X-Request-Id'))
