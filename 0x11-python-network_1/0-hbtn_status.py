#!/usr/bin/python3
""" What's my status? """

import urllib.request


if __name__ == '__main__':

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data_content = response.read()
        utf_content = data_content.decode('utf-8')
        response_format = 'Body response:\n\t- type: {}\n\t- content: {}\n\t- \
utf8 content: {}'.format(type(data_content), data_content, utf_content)
        print(response_format)
