#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ITE 2018"""

import json
import io
from ite import read_website
from ite import process_html
import os
import time
from collections import deque


# Inicializace setu s již uloženými URLS
saved_urls = set()

# Inicializace fronty URLS ke zpracování
urls_to_process = deque()

# Proměnné řešící logiku hloubky
urls_per_level = 1
counted_urls = 0

# Hloubka samotná
depth = 0


__all__ = ('main',)  # list of public objects of module


def save(title: str, content: str, url: str):
    json_file = {'title': title, 'url': url, 'content': content}
    path = '../storage/'
    if not os.path.exists(path):
        path = './storage/'
    path = os.path.join(path + title + '.json')

    with io.open(path, 'w', encoding='utf8') as jsf:
        data = json.dumps(json_file, ensure_ascii=False)
        try:
            jsf.write(data)
        except TypeError:
            # Decode data to Unicode first
            jsf.write(data.decode('utf8'))


def skip_page():
    global depth, urls_per_level, counted_urls, urls_to_process, saved_urls
    urls_per_level -= 1
    if urls_per_level < 1:
        urls_per_level = counted_urls
        counted_urls = 0
        depth += 1


def main():
    # start = time.time()

    start_url = 'https://portal.zcu.cz/portal/'

    # Inicializace globálních proměnných
    global depth, urls_per_level, counted_urls, urls_to_process, saved_urls
    saved_urls.add(start_url)
    urls_to_process.append(start_url)


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
        if not html:
            skip_page()
            continue

        # Zpracování HTML
        urls, title, text = process_html(html, url_to_read)

        # Pokud se nepodařilo zpracovat HTML, přeskočí další zpracování
        if not title:
            skip_page()
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
