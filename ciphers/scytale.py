# -*- coding: utf-8 -*-
from .cipher import Cipher
""" Implementacao da Cifra Scytale """

class Scytale(Cipher):
    def encrypt(self, texto, key):
        '''
        Cifra o texto com a cifra scytale utilizando a chave key.
        '''
        cifrado = ''
        texto = self.format_str(texto)
        # calcula a qtd de caracteres e a qtd de colunas
        qtd_ch = len(texto)
        col = qtd_ch // key
        if qtd_ch % key > 0:
            col += 1
        # preencher string com caracteres adicionais
        i = ord('A')
        while len(texto) < key * col:
            texto += chr(i)
            i += 1
        # cifragem
        for i in range(col):
            for j in range(0, qtd_ch, col):
                cifrado += texto[i + j]
        return cifrado.upper()

    def decrypt(self, texto, key):
        '''
        Decifra o texto cifrado com a cifra Scytale usando a chave key.
        '''
        texto_plano = ''
        texto = self.format_str(texto)
        for i in range(key):
            for j in range(0, len(texto), key):
                texto_plano += texto[i + j]
        return texto_plano.lower()
