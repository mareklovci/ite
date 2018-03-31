#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ITE 2018"""

from urllib import request as req
from bs4 import BeautifulSoup
import re


__all__ = ('main',)  # list of public objects of module


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


def get_urls(soup) -> str:
    url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is None:
            continue
        if re.match(url_pattern, href):
            yield href


def main():
    website1 = 'https://en.wikipedia.org/wiki/Drosera_regia'
    # website2 = 'http://vykuphubhalze.eu/'
    # website3 = 'http://legacy.carnivorousplants.org/cpn/articles/CPNv34n3p85_91.pdf'
    web = read_website(website1)
    soup = BeautifulSoup(web, 'html.parser')
    # print(soup.body.prettify())
    urls = get_urls(soup)
    urls = filter(lambda x: not re.match(r'^(.*?)\.pdf', x), urls)  # filter pdf files
    for url in urls:
        print(url)


if __name__ == '__main__':
    main()
