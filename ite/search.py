import os
import json
import re
from os.path import dirname, join
import io
import time


def htmlyfy(pages_with_searched_text, text_length, cas_hledani):

    html = ''

    html += '<p class ="lead" > Počet nalezených výsledků: ' + str(len(pages_with_searched_text)) + ' (' + str(round(cas_hledani, 2)) + ' s)' + '</p>'

    for item in pages_with_searched_text:
        html += '<div class=\"starter-template\">\n'
        html += '<h1>' + item['title'] + '</h1>'
        html += '<a href="' + item['url'] + '">' + item['url'] + '</a>\n'
        html += '<p class=\"lead\">...' + item['nalezeny_text'][:200] + '<strong>' + item['nalezeny_text'][200:200+text_length] + '</strong>' + item['nalezeny_text'][200+text_length:] + '...</p>\n'
        html += '</div>'

    return html


def search(text):
    start = time.time()
    # Cesta ke složce s daty
    directory = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/storage/')

    # Množina stránek s nalezeným textem
    pages_with_searched_text = []

    # Iterace přes všechny soubory v databázy
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            path = join(directory, filename)
            with io.open(path, 'r', encoding='utf-8') as f:
                json_file = f.read()
                json_dict = json.loads(json_file, encoding='utf-8')

                # Nalezený text
                match = re.search(text, json_dict['content'])

                if match:
                    begin = match.regs[0][0] - 200
                    end = match.regs[0][1] + 200

                    # Položka s daty k zobrazení na stránce
                    polozka = {
                        'title': json_dict['title'],
                        'url': json_dict['url'],
                        'nalezeny_text': json_dict['content'][begin: end]
                    }

                    pages_with_searched_text.append(polozka)

    end = time.time()
    return htmlyfy(pages_with_searched_text, len(text), end-start)





if __name__ == '__main__':
    search('uni')