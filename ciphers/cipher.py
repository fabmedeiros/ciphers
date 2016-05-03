# -*- coding: utf-8 -*-
""" Classe com metodos basicos para cifras classicas """

class Cipher(object):
    """ Classe base para as cifras classicas """
    plain_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plain_alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def format_str(self, text):
        '''Retorna text sem espacos e em maiusculas'''
        return text.replace(' ', '').upper()

    def shift_alphabet(self, alphabet, shift):
        '''Retorna alphabet com deslocamento de valor shift'''
        return alphabet[shift:] + alphabet[:shift]

    def create_square(self, key = '', alphanum = False, replace = ['J', 'I'], sequence = False):
        """Retorna um alfabeto numa matriz de num x num
        Por padrao, retorna uma matriz formada pelo alfabeto ABCDEFGHIKLMNOPQRSTUVWXYZ
        """
        square = []
        if alphanum:
            num = 6
            alfabeto = self.plain_alphanum
            replace = ['', '']
        else:
            num = 5
            alfabeto = self.plain_alphabet
        alfabeto = self.create_alphabet(key, alfabeto, replace, sequence)
        for idx in range(0, len(alfabeto), num):
            square.append(alfabeto[idx:idx + num])
        return square

    def create_alphabet(self, key = '', alfabeto = plain_alphabet, replace = ['', ''], sequence = False):
        '''Retorna um alfabeto com key como chave e no inicio do alfabeto'''
        if key:
            key = key.upper()
            temp = ''
            for ch in key:
                if ch not in temp:
                    temp += ch
            key = temp
            if replace[0] in key:
                key = key.replace(replace[0], replace[1])
            if sequence:
                idx = alfabeto.index(key[-1])
                alfabeto = self.shift_alphabet(alfabeto, idx)
        cipher = alfabeto.replace(replace[0], '')
        for ch_key in key:
            if ch_key in cipher:
                cipher = cipher.replace(ch_key, '')
        return key + cipher
