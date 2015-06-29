# -*- coding: utf-8 -*-
from cipher import Cipher

class Trithemius(Cipher):
    '''
    Classe de cifra Trithemius
    '''
    def __init__(self):
        self.cipher = Cipher.plain_alphabet

    def encrypt(self, text, decrypt=False):
        '''
        Cifra text com a cifra de Trithemius.
        Se decrypt é True, decifra ao invés de cifrar o text.
        '''
        text = self.format_str(text)
        ret_text = ''
        for char in text.upper():
            if decrypt:
                idx = self.cipher.find(char)
                ret_text += Cipher.plain_alphabet[idx]
            else:
                idx = Cipher.plain_alphabet.find(char)
                ret_text += self.cipher[idx]
            self.cipher = self.shift_alphabet(self.cipher, 1)
        self.cipher = Cipher.plain_alphabet
        return ret_text

    def decrypt(self, text):
        '''
        Decifra text com a cifra de Trithemius.
        '''
        return self.encrypt(text, True)
