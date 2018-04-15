#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ITE 2018"""

import json
from ite import read_website
from ite import process_html
import os
import time
from collections import deque

__all__ = ('main',)  # list of public objects of module


def save(title: str, content: str, url: str):
    json_file = {'title': title, 'url': url, 'content': content}
    path = '../storage/'
    if not os.path.exists(path):
        path = './storage/'
    path = os.path.join(path + title + '.json')
    with open(path, 'w+') as fp:
        json.dump(json_file, fp)
        fp.flush()


def main():
    # start = time.time()

    # Prostor pro vstupní URL
    # start_url = 'https://en.wikipedia.org/wiki/Drosera_regia'
    # start_url = 'http://vykuphubhalze.eu/'
    # start_url = 'http://legacy.carnivorousplants.org/cpn/articles/CPNv34n3p85_91.pdf'
    start_url = 'https://www.seznam.cz/'
    # start_url = 'https://portal.zcu.cz/portal/'
    # start_url = 'https://www.tensorflow.org/'
    # start_url = 'https://pornhub.com'

    # Inicializace setu s již uloženými URLS
    saved_urls = set()
    saved_urls.add(start_url)

    # Inicializace fronty URLS ke zpracování
    urls_to_process = deque()
    urls_to_process.append(start_url)

    # Proměnné řešící logiku hloubky
    urls_per_level = 1
    counted_urls = 0

    # Hloubka samotná
    depth = 0

    # Cyklus zpracovávající po sobě řazené URLS ve frontě
    while depth < 2:
        # Reakce na případ, že už nejsou žádné další stránky k prohledání
        # Pro množství u většiny běžných stránek by nemělo nastat
        if not urls_to_process:
            print('Byli uloženy veškeré stránky dosažitelné ze vstupního URL')
            exit(0)

        # Výpis pro vývojáře
        print('read...')

        # URL ke zpracování
        url_to_read = urls_to_process.popleft()

        # HTML ke zpracování
        html = read_website(url_to_read)

        # Pokud se nepodařilo načíst HTML, přeskočí další zpracování
        # TODO: THO: sjednotit přeskakování do 1 metody
        if not html:
            urls_per_level -= 1
            if urls_per_level < 1:
                urls_per_level = counted_urls
                counted_urls = 0
                depth += 1
            continue

        # Zpracování HTML
        urls, title, text = process_html(html, url_to_read)

        # Pokud se nepodařilo zpracovat HTML, přeskočí další zpracování
        if not title:
            urls_per_level -= 1
            if urls_per_level < 1:
                urls_per_level = counted_urls
                counted_urls = 0
                depth += 1
            continue

        # Uložení JSONU s potřebnými daty
        save(title, text, url_to_read)

        # Uložení zpracovaného URL do setu již zpracovaných
        saved_urls.add(url_to_read)

        # Přidání všech doposud neuložených URLS do fronty k zpracování
        for url in urls:
            if url not in saved_urls:
                urls_to_process.append(url)
                counted_urls += 1

        # Logika hloubky
        urls_per_level -= 1
        if urls_per_level < 1:
            urls_per_level = counted_urls
            counted_urls = 0
            depth += 1

    # Prostor pro měření času
    # end = time.time()
    # print('time:',end-start,'s')

if __name__ == '__main__':
    main()
