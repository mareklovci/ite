#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Webpage downloading, reading and processing"""

from urllib import request as req


def read_website(url: str) -> str:
    try:
        fr = req.urlopen(url)
        text = fr.read()
        fr.close()
    except req.HTTPError as err:
        if err.code == 404:
            print('Server unavailable')
            text = ''
        else:
            raise
    return text


def main():
    pass


if __name__ == '__main__':
    main()
