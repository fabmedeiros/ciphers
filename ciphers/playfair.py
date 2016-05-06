# -*- coding: utf-8 -*-
from .cipher import Cipher

class Playfair(Cipher):
    def encrypt(self, text, key = '', decrypt = False):
        """Retorna text cifrado com a cifra de Playfair.
        key - chave a ser usada; havendo chave, o alfabeto sera iniciado com ela
        decrypt - se True, decifra; se False, cifra
        """
        ciphertext = ''
        text = text.upper()
        text = text.replace('J', 'I').replace(' ', '')
        # checa se o texto contem par de letras iguais
        text = self.check_double(text)
        # se text nao tiver numero par de letras
        if len(text) % 2:
            text += 'W'
        # cria a tabela
        self.square = self.create_square(key)
        for i in range(0, len(text), 2):
             ciphertext += self.change_pair(text[i:i + 2], decrypt)
        return ciphertext.upper()

    def decrypt(self, ciphertext, key = ''):
        """Retorna o ciphertext decifrado com a cifra de Playfair"""
        return self.encrypt(ciphertext.upper(), key, True).lower()

    def check_double(self, text):
        out = ''
        for idx in range(0, len(text), 2):
            pair = text[idx:idx+2]
            if len(pair) > 1 and pair[0] == pair[1]:
                out += pair[0] + 'W' + pair[1]
            else:
                out += pair
        return out

    def change_pair(self, pair, decrypt = False):
        """Retorna as posicoes de um par de letras de uma matriz 5x5."""
        # retorno - valor a ser retornado quando se atinge o limite da tabela
        # limite - valor de limite das celulas da tabela
        # passo - valor de incremento/decremento
        if decrypt:
            retorno = 4
            limite = -1
            passo = -1
        else:
            retorno = 0
            limite = 5
            passo = 1
        coord1, coord2 = self.coords(pair)
        if coord1[0] == coord2[0]:
            # caso em que as duas letras estao na mesma linha
            coord1[1] += passo
            coord2[1] += passo
        elif coord1[1] == coord2[1]:
            # caso em que as duas letras estao na mesma coluna
            coord1[0] += passo
            coord2[0] += passo
        else:
            # caso em que as duas letras nao estao na mesma linha nem mesma coluna
            coord1[1], coord2[1] = coord2[1], coord1[1]
        coord1 = [retorno if x == limite else x for x in coord1]
        coord2 = [retorno if x == limite else x for x in coord2]
        return self.letter(coord1) + self.letter(coord2)

    def coords(self, pair):
        """Retorna as coordenadas de um par de letras numa matriz."""
        coords = []
        for letter in pair:
            for line in range(len(self.square)):
                if letter in self.square[line]:
                    coords.append([line, self.square[line].index(letter)])
                    break
        return coords

    def letter(self, coord):
        """Retorna a letra com a coordenada dada"""
        return self.square[coord[0]][coord[1]]
