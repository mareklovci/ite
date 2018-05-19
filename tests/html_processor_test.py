#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import ite.html_processor as hproc
from bs4 import BeautifulSoup

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestHtmlProcessor(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(THIS_DIR, 'data/test_html.html'), 'r') as f:
            self.soup = BeautifulSoup(f, 'html.parser')

    def test_process_text(self):
        processed = hproc.process_text(self.soup)
        with open(os.path.join(THIS_DIR, 'data/test_html.txt'), 'r') as f:
            expected = f.readlines()
        expected = ''.join(expected)
        self.assertEqual(processed, expected)


if __name__ == '__main__':
    unittest.main()
