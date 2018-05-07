#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import re
from os.path import dirname, join
import io
import time


def search(text):
    start = time.time()
    # Cesta ke složce s daty
    directory = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/storage/')

    # Množina stránek s nalezeným textem
    items = []

    # Iterace přes všechny soubory v databázy
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            path = join(directory, filename)
            with io.open(path, 'r', encoding='utf-8') as f:
                json_file = f.read()
                json_dict = json.loads(json_file, encoding='utf-8')

                # Nalezený text
                match = re.search(text, json_dict['content'], re.IGNORECASE)

                if match:
                    first_occurrence = match.span()
                    begin = first_occurrence[0] - 50
                    end = first_occurrence[1] + 50
                    # Položka s daty k zobrazení na stránce
                    polozka = {
                        'title': json_dict['title'],
                        'url': json_dict['url'],
                        'content_begin': json_dict['content'][begin:first_occurrence[0]],
                        'content_end': json_dict['content'][first_occurrence[1]:end],
                        'searched': json_dict['content'][first_occurrence[0]:first_occurrence[1]]
                    }
                    items.append(polozka)
    end = time.time()
    data = {
        'findings': len(items),
        'time': round(end-start, 2),
        'items': items
    }
    return data


def main():
    search('uni')


if __name__ == '__main__':
    main()
