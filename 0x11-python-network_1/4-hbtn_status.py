#!/usr/bin/python3
""" What's my status? """

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)

    data_content = res.text

    res_format = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
                  type(data_content), data_content)

    print(res_format)
