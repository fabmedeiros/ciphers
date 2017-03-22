# -*- coding: utf-8 -*-
#https://github.com/jameslyons/pycipher/blob/master/pycipher/polybius.py
#http://practicalcryptography.com/ciphers/adfgvx-cipher/
from adfgx import ADFGX
from cipher import Cipher

class ADFGVX(ADFGX):
    def __init__(self):
        self.chars = {
            'A': 0, 'D': 1, 'F': 2,
            'G': 3, 'V': 4, 'X': 5
        }

    def create_square(self, alphabet):
        print('ok')
        self.square = Cipher.create_square(self, alphabet=alphabet, alphanum=True)

cifra = ADFGVX()
alfabeto = 'ZC0BD5MH1AO6INL7R2SPQ8WXE3UTY9FG4KVJ'
cifra.create_square(alfabeto)
cifrado = cifra.encrypt('FABIO mariano de medeiros', 'SENHAdf')
print(cifrado)
print(cifra.decrypt(cifrado, 'SENHA'))
