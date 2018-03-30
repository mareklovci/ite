#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ITE 2018"""

from urllib import request as req
from bs4 import BeautifulSoup
import re


__all__ = ('main',)  # list of public objects of module


def read_website(url):
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


def get_urls(links: list):
    url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    results = list()
    for link in links:
        href = link.get('href')
        if href is None:
            continue
        http = re.match(url_pattern, href)
        if http:
            results.append(href)
    return results


def get_links(soup):
    links = soup.find_all('a')
    return links


def main():
    web = read_website('http://vykuphubhalze.eu/')
    soup = BeautifulSoup(web, 'html.parser')
    # print(soup.body.prettify())
    links = get_links(soup)
    urls = get_urls(links)
    for url in urls:
        print(url)


if __name__ == '__main__':
    main()
