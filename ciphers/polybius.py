# -*- coding: utf-8 -*-
from .cipher import Cipher

class Polybius(Cipher):
    def select_square(self, key):
        '''
        Retorna o quadrado de Polibio referente a key utilizada.
        Se key for True, usa-se o quadrado de Polibio com letras e numerais;
        Se key for uma string, retorna o quadrado de Polibio com key como palavra chave.
        Se nao houver key, usa-se o quadrado de Polibio padrao.
        '''
        if key == True:
            return self.create_square(alphanum = True, sequence = True)
        elif key == '':
            return self.create_square(key, alphanum = True, sequence = True)
        return self.create_square(sequence = True)

    def encrypt(self, plaintext, key = ''):
        '''
        Retorna o plaintext cifrado com a cifra de Polibio.
        Se key = True, cifra com quadrado de Polibio com letras e numeros.
        Se key = uma string, cifra o quadrado de Polibio com key como palavra chave.
        Se nao houver key, cifra com o quadrado de polibio padrao.
        '''
        square = self.select_square(key)
        ciphertext = ''
        for ch in plaintext.upper():
            idx = 1
            if ch == 'J':
                ch = 'I'
            for linha in square:
                if ch in linha:
                    ciphertext += str(idx) + str(linha.index(ch) + 1) + ' '
                idx += 1
        return ciphertext

    def decrypt(self, ciphertext, key = ''):
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
            i, j = var // 10, var % 10
            if i - 1 < len(square) and j - i < len(square[0]):
                plaintext += square[i - 1][j - 1]
        return plaintext.lower()
