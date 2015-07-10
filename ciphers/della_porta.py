# -*- coding: utf-8 -*-
from cipher import Cipher

class DellaPorta(Cipher):
    ''' Cifra criptografica de Giambattista della Porta '''
    def __init__(self):
        '''
        keys - chaves para determinar o deslocamento da cifra
        plain - alfabeto fixo
        cipher - alfabeto a ser deslocado
        '''
        self.keys = {
            'A': 0, 'B': 0, 'C': 1, 'D': 1, 'E': 2, 'F': 2,
            'G': 3, 'H': 3, 'I': 4, 'J': 4, 'K': 5, 'L': 5,
            'M': 6, 'N': 6, 'O': 7, 'P': 7, 'Q': 8, 'R': 8,
            'S': 9, 'T': 9, 'U': 10, 'V': 10, 'W': 11,
            'X': 11, 'Y': 12, 'Z': 12
        }
        self.plain = 'ABCDEFGHIJKLM'
        self.cipher = 'NOPQRSTUVWXYZ'

    def shift(self, key):
        ''' Desloca o alfabeto '''
        shift = self.keys[key]
        return self.shift_alphabet(self.cipher, shift)

    def repeat_password(self, password, length):
        ''' Repete a password ate o tamanho do texto plano '''
        new_pass = password * (length/len(password))
        length -= len(new_pass)
        if length:
            new_pass += password[:length]
        return new_pass

    def encrypt(self, plaintext, password):
        ''' Retorna o texto cifrado '''
        ciphertext = ''
        plaintext = self.format_str(plaintext)
        plainalphabet = self.plain
        password = self.format_str(
            self.repeat_password(password, len(plaintext))
        )
        for idx in range(len(plaintext)):
            char = plaintext[idx]
            cipheralphabet = self.shift(password[idx])
            if char in plainalphabet:
                idchar = plainalphabet.find(char)
                ciphertext += cipheralphabet[idchar]
            elif char in cipheralphabet:
                idchar = cipheralphabet.find(char)
                ciphertext += plainalphabet[idchar]
        return ciphertext

    def decrypt(self, ciphertext, password):
        ''' Retorna o texto decifrado '''
        return self.encrypt(ciphertext, password)
