# -*- coding: utf-8 -*-
from cipher import Cipher


class Vigenere(Cipher):
    """ Cifra de Vigenere """
    def repeat_password(self, password, text):
        '''
        Repete a password ate o tamanho de text
        '''
        if len(password) < len(text):
            new_pass = password * (len(text)/len(password))
            if len(new_pass):
                new_pass += password[:len(new_pass)]
            return new_pass.upper()
        return password.upper()

    def encrypt(self, plaintext, password, decrypt=False):
        '''
        Cifra plaintext com a cifra de Vigenere
        Decifra se decrypt for True
        '''
        password = self.repeat_password(password, plaintext)
        plaintext = self.format_str(plaintext)
        textout = ''
        for idx, char in enumerate(plaintext.upper()):
            # indice da letra da cifra
            idx_key = Cipher.plain_alphabet.find(password[idx])
            # gera alfabeto cifrado
            c_alphabet = self.shift_alphabet(Cipher.plain_alphabet, idx_key)
            if decrypt:
                idx_p = c_alphabet.find(char)
                textout += Cipher.plain_alphabet[idx_p]
            else:
                idx_p = Cipher.plain_alphabet.find(char)
                textout += c_alphabet[idx_p]
        return textout

    def decrypt(self, ciphertext, password):
        '''
        Decifra ciphertext
        '''
        return self.encrypt(ciphertext, password, True)
