# -*- coding: utf-8 -*-
from cipher import Cipher


class Polybius(Cipher):
    def __init__(self):
        ## p_alphabet nao possui a letra j, que sera substituida
        ## pela letra i na cifragem e decifragem
        self.p_alphabet = 'abcdefghiklmnopqrstuvwxyz'
        self.p_alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def cipher_alphabet(self, password):
        '''
        Retorna um alfabeto cifrado iniciado com
        o texto da palavra chave password
        '''
        c_alphabet = []
        p_alphabet = self.p_alphanum
        for ch in password:
            if ch not in c_alphabet:
                c_alphabet.append(ch)
                idx = p_alphabet.find(ch)
        p_alphabet = self.format_str(p_alphabet, idx)
        for ch in p_alphabet:
            if ch not in c_alphabet:
                c_alphabet.append(ch)
        return ''.join(c_alphabet)

    def create_square(self, alphabet, lines):
        '''
        Retorna uma tabela lista quadrada definida por lines
        com cada celula preenchida com um caracter de alphabet
        '''
        square = []
        temp = []
        count = 0
        for ch in alphabet:
            temp.append(ch)
            count += 1
            if count == lines:
                square.append(temp)
                temp = []
                count = 0
        return square

    def select_square(self, key):
        '''
        Retorna o quadrado de Polibio referente a key utilizada.
        Se key for True, usa-se o quadrado de Polibio com letras e numerais;
        Se key for uma string, retorna o quadrado de Polibio com key como palavra chave.
        Se nao houver key, usa-se o quadrado de Polibio padrao.
        '''
        if key:
            if key == True:
                return self.create_square(self.p_alphanum, 6)
            else:
                return self.create_square(self.cipher_alphabet(str(key)), 6)
        return self.create_square(self.p_alphabet, 5)

    def encrypt(self, plaintext, key = None):
        '''
        Retorna o plaintext cifrado com a cifra de Polibio.
        Se key = True, cifra com quadrado de Polibio com letras e numeros.
        Se key = uma string, cifra o quadrado de Polibio com key como palavra chave.
        Se nao houver key, cifra com o quadrado de polibio padrao.
        '''
        square = self.select_square(key)
        ciphertext = ''
        for ch in plaintext.lower():
            idx = 1
            if ch == 'j':
                ch = 'i'
            for linha in square:
                if ch in linha:
                    ciphertext += str(idx) + str(linha.index(ch) + 1) + ' '
                idx += 1
        return ciphertext

    def decrypt(self, ciphertext, key = None):
        '''
        Retorna o ciphertext decifrado com a cifra de Polibio.
        Se key = True, decifra com quadrado de Polibio com letras e numeros.
        Se key = uma string, decifra o quadrado de Polibio com key como palavra chave.
        Se nao houver key, decifra com o quadrado de polibio padrao.
        '''
        square = self.select_square(key)
        plaintext = ''
        ciphertext = str(ciphertext).replace(' ', '')
        for num in range(0, len(ciphertext), 2):
            var = int(ciphertext[num:num + 2])
            i, j = var / 10, var % 10
            if i - 1 < len(square) and j - i < len(square[0]):
                plaintext += square[i - 1][j - 1]
        return plaintext.lower()
