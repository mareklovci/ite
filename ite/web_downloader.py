#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Webpage downloading, reading and processing"""

from urllib import request as req
import time

# Zabírá určitý nezanedbatelný čas, promyslet paralelizaci
def read_website(url: str) -> str:
    try:
        fr = req.urlopen(url)
        text = fr.read()
        fr.close()
    except Exception as err:
        print('Error:', err)
        text = ''

    return text


def main():
    pass


if __name__ == '__main__':
    main()
