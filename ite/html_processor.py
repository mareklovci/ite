#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""HTML reading and processing"""

import re
from unidecode import unidecode
from bs4 import BeautifulSoup


def get_urls(soup) -> str:
    url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is None:
            continue
        if re.match(url_pattern, href):
            yield href


def scrap_text(soup):
    for p in soup.body.find_all('p'):
        for string in p.next_elements:
            string = str(string)
            if re.match(r'<[^>]*>', string):
                continue
            if re.match(r'\s', string):  # deletes 'standalone' whitespaces and other blank characters
                continue
            else:
                # TODO: navrhnout regex pro odstraneni VSECH nevhodnych znaku
                string = re.sub(r'[,.|\s+]', ' ', string).strip()  # odstrani prebytecne mezery a jine znaky z retezce
                yield string


def group_text(scrap):
    string = ' '.join(scrap)
    string = re.sub(r'\s+', ' ', string)
    return string


def make_title(soup) -> str:
    title: str = soup.head.title.text
    splt = title.lower().split()
    for item in splt:
        if re.match(r'[^a-zA-Z\d\s:]', item):
            splt.remove(item)
    title = '-'.join(splt)
    unaccented_title = unidecode(title)
    return unaccented_title


def process_text(soup):
    scrap = scrap_text(soup)
    text = group_text(scrap)
    return text


def process_urls(soup):
    urls = get_urls(soup)
    urls = filter(lambda x: not re.match(r'^(.*?)\.pdf', x), urls)  # filter pdf files
    urls = set(urls)
    return urls


def process_html(html: str):
    """
    Processes HTML code. Separates urls, title and actual content. Serves as a "one call for all" function.

    :param html: html to process
    :return: urls, title, text
    """
    soup = BeautifulSoup(html, 'html.parser')
    urls = process_urls(soup)
    title = make_title(soup)
    text = process_text(soup)
    return urls, title, text


def main():
    pass


if __name__ == '__main__':
    main()
