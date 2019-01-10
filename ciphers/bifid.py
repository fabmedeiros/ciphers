# -*- coding: utf-8 -*-
from .cipher import Cipher

class Bifid(Cipher):
    def encrypt(self, plaintext, alphabet=None):
        lins = ''
        cols = ''
        plaintext = plaintext.upper()
        matriz = self.create_square(alphabet)
        for letra in plaintext:
            for lin in matriz:
                if letra in lin:
                    cols += str(lin.find(letra) + 1)
                    lins += str(matriz.index(lin) + 1)
        cipher_num = lins + cols
        ciphertext = ''
        for i in range(0, len(cipher_num), 2):
            ref = cipher_num[i:i + 2]
            ciphertext += matriz[int(ref[0]) - 1][int(ref[1]) - 1]
        return ciphertext

    def decrypt(self, texto, alphabet=None):
        num = ''
        plain = ''
        texto = texto.upper()
        matriz = self.create_square(alphabet)
        for letra in texto:
            for linha in matriz:
                if letra in linha:
                    num += str(matriz.index(linha) + 1) + str(linha.find(letra) + 1)
        linhas = num[:len(num)//2]
        colunas = num[len(num)//2:]
        for i in range(0, len(linhas)):
            plain += matriz[int(linhas[i]) - 1][int(colunas[i]) - 1]
        return plain

