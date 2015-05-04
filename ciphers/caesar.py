# -*- coding: utf-8 -*-
from cipher import Cipher
""" Implementacao da Cifra de Cesar """


class Caesar(Cipher):
    '''
    Cifra de Cesar
    '''
    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, texto_plano, key=3):
        '''
        Retorna o texto_plano cifrado com a cifra de Cesar,
        utlizando a chave key, cujo padrao e 3.
        '''
        alfabeto_cifrado = self.shift_alphabet(self.letters, key)

        cipher_text = ''
        texto_plano = self.format_str(texto_plano)
        for char in texto_plano:
            if char in self.letters:
                idx = self.letters.find(char)
                cipher_text += alfabeto_cifrado[idx]
        return cipher_text

    def decrypt(self, texto_cifrado, key=3):
        '''
        Retorna em texto plano o texto_cifrado decifrado com a
        cifra de Cesar, utilizando a chave key, cujo padrao e 3.
        '''
        return self.encrypt(texto_cifrado, -key)
