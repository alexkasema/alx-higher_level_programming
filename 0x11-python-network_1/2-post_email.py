#!/usr/bin/python3
""" POST an email """

import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    email = urlencode(email)
    email = email.encode('ascii')
    req = Request(url, email)

    with urlopen(req) as response:
        data_content = response.read().decode('utf-8')
        print(data_content)
