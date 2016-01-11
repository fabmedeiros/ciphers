# -*- coding: utf-8 -*-
from cipher import Cipher
'''
Classe Alberti
'''
class Alberti(Cipher):
    '''
    Classe Alberti
    '''
    def __init__(self):
        self.fixed_disk = None
        self.movable_disk = None
        self.fixed_key = ''
        self.movable_key = ''
        self.decrypting = False

    def set_fixed_disk(self, plain_alphabet):
        '''
        Configura o alfabeto do disco fixo com o texto de plain_alphabet.
        '''
        self.fixed_disk = plain_alphabet.upper()

    def set_movable_disk(self, cipher_alphabet):
        '''
        Configura o alfabeto do disco movel com o texto de cipher_alphabet.
        '''
        self.movable_disk = cipher_alphabet.lower()

    def set_keys(self, fixed_key, movable_key):
        '''
        Configura as chaves do disco fixo e do disco movel;
        Desloca o disco movel de acordo com as chaves.
        '''
        self.fixed_key = fixed_key.upper()
        self.set_movable_key(movable_key)
        fixed_id = self.fixed_disk.find(self.fixed_key)
        movable_id = self.movable_disk.find(self.movable_key)
        shift = -(fixed_id - movable_id)
        self.movable_disk = self.shift_alphabet(self.movable_disk, shift)

    def encrypt(self, plaintext, shift=0):
        '''
        Cifra o plaintext com a cifra de Alberti.
        '''
        ciphertext = ''
        for char in plaintext:
            if char.isupper():
                #letra maiuscula
                self.set_keys(char, self.movable_key)
            elif char.isdigit():
                #numero
                movable_key = self.movable_disk[self.fixed_disk.find(char)]
                self.set_keys(self.fixed_key, movable_key)
            else:
                #letra minuscula
                if self.decrypting:
                    #decifrando
                    i = self.movable_disk.find(char)
                    char = self.fixed_disk[i].lower()
                else:
                    #cifrando
                    i = self.fixed_disk.find(char.upper())
                    char = self.movable_disk[i]
                if shift:
                    #deslocamento
                    self.movable_disk = self.shift_alphabet(self.movable_disk, -shift)
            ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext, shift=0):
        '''
        Decifra utilizando a cifra de Alberti.
        '''
        self.decrypting = True
        text = ''
        plaintext = self.encrypt(ciphertext, shift)
        self.decrypting = False
        for char in plaintext:
            if char.islower():
                text += char
        return text

    def set_movable_key(self, movable_key):
        '''
        Configura a chave do disco movel.
        '''
        self.movable_key = movable_key.lower()
