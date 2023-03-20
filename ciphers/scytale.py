# -*- coding: utf-8 -*-
from .cipher import Cipher
""" Implementacao da Cifra Scytale """

class Scytale(Cipher):
    def encrypt(self, plaintext, key):
        ''' Cifra o texto com a cifra scytale utilizando a chave key. '''
        square = []
        plaintext = self.format_str(plaintext)
        idx = 0
        lines = len(plaintext) // key
        if len(plaintext) % key:
           lines += 1
        for lin in range(lines):
            square.append([])
            for col in range(key):
                if len(plaintext) > idx:
                    square[lin].append(plaintext[idx])
                else:
                    square[lin].append('')
                idx += 1
        ciphertext = ''.join([square[lin][col] for col in range(key) for lin in range(lines)])
        return ciphertext

    def decrypt(self, ciphertext, key):
        ''' Decifra o ciphertext com a cifra Scytale usando a chave key. '''
        idx = 0
        ciphertext = self.format_str(ciphertext)
        lines = len(ciphertext) // key
        if len(ciphertext) % key:
            lines += 1
        # quantidade de colunas completas
        spaces = len(ciphertext) % key
        square = [['' for col in range(key)] for lin in range(lines)]
        for col in range(key):
            for lin in range(lines):
                if len(ciphertext) > idx:
                    if not spaces and lin >= lines - 1:
                        # executa caso a coluna ao seja completa
                        square[lin][col] = ''
                        idx -= 1
                    else:
                        square[lin][col] = ciphertext[idx]
                idx += 1
            if spaces:
                spaces -= 1
        plaintext = ''.join([square[lin][col] for lin in range(lines) for col in range(key)])
        return plaintext
