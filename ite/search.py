import os
import json
import re
from os.path import dirname, join
import io


def search(text):

    directory = os.path.normpath(dirname(__file__) + os.sep + os.pardir + '/storage/')

    pages_with_searched_text = ''

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            path = join(directory, filename)
            with io.open(path, 'r', encoding='utf-8') as f:
                json_file = f.read()
                json_dict = json.loads(json_file, encoding='utf-8')

                match = re.search(text, json_dict['content'])

                if match:
                    polozka = json_dict['title'] + ': ' + json_dict['url']
                    hladany_text = json_dict['content']
                    begin = match.regs[0][0]
                    end = match.regs[0][1]
                    hladany_text = hladany_text[begin - 10: end + 10]
                    polozka += hladany_text + '\n\n'
                    pages_with_searched_text += polozka

                # if text in json_dict['content']:
                #     polozka = json_dict['title'] + ': ' + json_dict['url'] + '\n'
                #     pages_with_searched_text += polozka
        else:
            print('fail')

    print(pages_with_searched_text)
    return pages_with_searched_text


if __name__ == '__main__':
    search('uni')