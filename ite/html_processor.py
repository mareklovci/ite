#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""HTML reading and processing"""

import random
import string as s
import re
from unidecode import unidecode
from bs4 import BeautifulSoup
import time

def get_urls(soup) -> str:
    url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is None:
            continue
        if re.match(url_pattern, href):
            yield href

# Místo pro optimalizaci: cca 1/2 doby běhu programu
def scrap_text(soup):
    # hotfix - vrácení prázdného stringu v případě soup.body = None
    if not soup.body:
        return ''

    translator = str.maketrans('', '', s.punctuation)

    for p in soup.body.find_all('p'):
        for string in p.next_elements:
            string = str(string)
            if re.match(r'<[^>]*>', string):
                continue
            if re.match(r'\s', string):  # deletes 'standalone' whitespaces and other blank characters
                continue
            else:
                string = string.translate(translator)
                # TODO: navrhnout regex pro odstraneni VSECH nevhodnych znaku - HOTOVO
                # string = re.sub(r'[,.|\s+]', ' ', string).strip()  # odstrani prebytecne mezery a jine znaky z retezce
                yield string


def group_text(scrap):
    string = ' '.join(scrap)
    string = re.sub(r'\s+', ' ', string)
    return string

def discard_interpunction(text, chars_to_discard = [':', '\'','\"', '*', '.', ',', '|', '?', '/', '\\', '<', '>', ' ']):
    """
    Hotfix - odstraní nebezpečné znaky u titlu - aby šel uložit soubor
    """
    for char in chars_to_discard:
        text = text.replace(char, '')
    return text

def failed_title():
    """
    Hotfix  - v případě, že soup nemá title
            - TODO: investigace stránek s url dle souborů empty-string-XXXXXX, proč zde není title?
            - random nemá hlubší výzanm, jen aby se to ukládalo pod jiným názvem :D
    """
    return 'failed-title-' + str(random.randint(0, 100000))

def make_title(soup) -> str:
    # hotfix - v případě nenalezení head nebo head.text
    if not soup.head or not soup.head.title:
        return ''

    title: str = soup.head.title.text
    splt = title.lower().split()
    for item in splt:
        if re.match(r'[^a-zA-Z\d\s:]', item):
            splt.remove(item)
    title = '-'.join(splt)
    unaccented_title = unidecode(title)
    unaccented_title = discard_interpunction(unaccented_title)
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
    # BeautifulSoup zabírá určitý nezanedbatelný čas - zvážit
    soup = BeautifulSoup(html, 'html.parser')
    urls = process_urls(soup)
    title = make_title(soup)
    if not title:
        return '', '', ''
    text = process_text(soup)
    return urls, title, text


def main():
    pass


if __name__ == '__main__':
    main()
