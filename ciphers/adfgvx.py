# -*- coding: utf-8 -*-

from .adfgx import ADFGX
from .cipher import Cipher

class ADFGVX(ADFGX):
    def __init__(self):
        self.chars = {
            'A': 0, 'D': 1, 'F': 2,
            'G': 3, 'V': 4, 'X': 5
        }
        self.replace = ()

    def create_square(self, alphabet):
        self.square = Cipher.create_square(self, alphabet=alphabet, alphanum=True)
