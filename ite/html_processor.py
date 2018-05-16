#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""HTML reading and processing"""

import string as s
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_urls(soup, current_url) -> str:
    """
    Vrátí odkazy nacházející se na stránce
    :param soup: HTML předzpracované balíčkem beautifulsoup - soup object
    :param current_url: současné url pro relativní odkazy
    :return: url získané ze soup
    """
    url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is None:
            continue
        if re.match(url_pattern, href):
            yield href
        else:
            joined_url = urljoin(current_url, href)
            yield joined_url


def scrap_text(soup):
    """Returns string from bs4 placed in <p> tag"""

    # Vrácení prázdného stringu v případě soup.body = None
    if not soup.body:
        return ''

    # translator = str.maketrans('', '', s.punctuation)

    for p in soup.body.find_all('p'):
        for string in p.next_elements:
            string = str(string)
            if re.match(r'<[^>]*>', string):
                continue
            if re.match(r'\s', string):  # deletes 'standalone' whitespaces and other blank characters
                continue
            else:
                # string = string.translate(translator)
                yield string


def make_title(soup) -> str:
    """
    :param soup: HTML předzpracované balíčkem beautifulsoup - soup object
    :return: title stránky
    """
    # v případě nenalezení head nebo head.text
    if not soup.head or not soup.head.title:
        return ''
    return soup.head.title.text


def process_text(soup):
    """Vrátí veškerý obsažený text na stránce

    :param soup:
    :return:
    """
    def group_text(scra):
        """Joins text from list to one string"""
        string = ' '.join(scra)
        string = re.sub(r'\s+', ' ', string)
        return string

    # List stringů z <p> tagů
    scrap = list(scrap_text(soup))
    text = group_text(scrap)
    return text


def process_urls(soup, current_url):
    urls = get_urls(soup, current_url)
    urls = filter(lambda x: not re.match(r'^(.*?)\.pdf', x), urls)  # filter pdf files
    urls = filter(lambda x: 'facebook' not in x, urls)
    urls = filter(lambda x: 'youtube' not in x, urls)
    urls = set(urls)
    return urls


def process_html(html: str, current_url):
    """Processes HTML code.

    Separates urls, title and actual content. Serves as a "one call for all" function.

    :param html: html to process
    :param current_url:
    :return: urls, title, text
    """
    soup = BeautifulSoup(html, 'html.parser')
    urls = process_urls(soup, current_url)
    title = make_title(soup)
    if not title:
        return '', '', ''
    text = process_text(soup)
    return urls, title, text


def main():
    pass


if __name__ == '__main__':
    main()
