#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ITE 2018"""

import json
from ite import read_website
from ite import process_html
import os

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
    url = 'https://en.wikipedia.org/wiki/Drosera_regia'
    # url = 'http://vykuphubhalze.eu/'
    # url = 'http://legacy.carnivorousplants.org/cpn/articles/CPNv34n3p85_91.pdf'
    # url = 'https://www.seznam.cz/'
    # url = 'https://portal.zcu.cz/portal/'
    # url = 'https://www.tensorflow.org/'

    levels = {0: [url]}
    for i in range(2):
        for url in levels[i]:
            print('read...') # výpis do konzole, že se něco děje - smažte, jestli se vám to nelíbí :D
            html = read_website(url)
            urls, title, text = process_html(html)
            save(title, text, url)
            levels[i + 1] = urls


if __name__ == '__main__':
    main()
