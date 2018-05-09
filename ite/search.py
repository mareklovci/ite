#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import re
from os.path import dirname, join
import io
import time
import unidecode


def _create_item(json_dict: dict, span: int, match) -> dict:
    """Polozka s daty k zobrazeni na strance"""
    first_occurrence = match.span()
    begin = first_occurrence[0] - span
    end = first_occurrence[1] + span
    item = {
        'title': json_dict['title'],
        'url': json_dict['url'],
        'content_begin': json_dict['content'][begin:first_occurrence[0]],
        'content_end': json_dict['content'][first_occurrence[1]:end],
        'searched': json_dict['content'][first_occurrence[0]:first_occurrence[1]]
    }
    return item


def _create_pack(items, start, end):
    pack = {
        'findings': len(items),
        'time': round(end - start, 2),
        'items': items
    }
    return pack


def _match(text: str, content: str, unicode_insensitive=False):
    if unicode_insensitive:
        text = unidecode.unidecode(text)
        content = unidecode.unidecode(content)
    match = re.search(text, content, re.IGNORECASE)
    return match


def _find_item(text, directory):
    """Iterace přes všechny soubory v databázy"""
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            path = join(directory, filename)
            with io.open(path, 'r', encoding='utf-8') as f:
                json_file = f.read()
                json_dict = json.loads(json_file, encoding='utf-8')

                # nalezeny text
                match = _match(text, json_dict['content'])

                if match:
                    polozka = _create_item(json_dict, 150, match)
                    yield polozka


def search(text):
    # Cesta ke složce s daty
    directory = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/storage/')

    start = time.time()

    # Množina stránek s nalezeným textem
    items = list(_find_item(text, directory))

    end = time.time()
    data = _create_pack(items, start, end)
    return data


def main():
    search('uni')


if __name__ == '__main__':
    main()
