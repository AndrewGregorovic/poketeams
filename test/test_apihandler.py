import os
import sys
import unittest


sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                + "/src")

from apihandler import APIHandler


class TestAPIHandlerClass(unittest.TestCase):
    def test_api_url(self):
        pass

    def test_get_single_pokemon(self):
        pass

    def test_get_pokemon_with_querystring(self):
        pass

    def test_get_move(self):
        pass

    def test_get_ability(self):
        pass