# -*- coding: utf-8 -*-
from cipher import Cipher

class Trifid(Cipher):
    def create_alphabet(self, key=''):
        alphabet = super().create_alphabet(key) + '+'
        return alphabet
        
    def _create_squares(self, alphabet):
        square_lines = []
        for i in range(0, 9):
            square_lines.append(alphabet[0 + 3 * i:3 + 3 * i])

        squares = {
            "1": square_lines[0:3],
            "2": square_lines[3:6],
            "3": square_lines[6:9]
        }
        return squares
    
    def encrypt(self, plaintext, alphabet=None):
        quads = ''
        lines = ''
        cols = ''
        ciphertext = ''
        plaintext = plaintext.upper()
        square = self._create_squares(alphabet)
        ### busca letra dentro do tres quadrados
        for letra in plaintext:
            for quad in square.keys():
                for line in square[quad]:
                    if letra in line:
                        quads += quad
                        lines += str(square[quad].index(line) + 1)
                        cols += str(line.index(letra) + 1)
        cipher_num = quads + lines + cols
        # varre cipher_num e usa cada tres numeros para varrer os tres quadrados
        for i in range(0, len(cipher_num), 3):
            idx = cipher_num[i:i + 3]
            quad = idx[0]
            line = int(idx[1]) - 1
            col = int(idx[2]) - 1
            ciphertext += square[quad][line][col]
        return ciphertext

    def decrypt(self, ciphertext, alphabet=None):
        text = ciphertext.upper()
        cipher_num = ''
        square = self._create_squares(alphabet)
        ### busca letra dentro do tres quadrados
        for letra in text:
            for quad in square.keys():
                for line in square[quad]:
                    if letra in line:
                        lines = str(square[quad].index(line) + 1)
                        cols = str(line.index(letra) + 1)
                        cipher_num += quad + lines + cols
        squares = []
        for i in range(0, len(cipher_num), len(text)):
            squares.append(cipher_num[i:i + len(text)])
        plaintext = ''
        for col in range(0, len(text)):
            item = ''
            for lin in range(0, 3):
                item += squares[lin][col]
            plaintext += square[item[0]][int(item[1]) - 1][int(item[2]) - 1]
        return plaintext
