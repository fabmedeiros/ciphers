# -*- coding: utf-8 -*-
""" Cifra ADFGX """
from .cipher import Cipher

class ADFGX(Cipher):
    """ Cifra ADFGX """
    def __init__(self):
        self.chars = {
            'A': 0, 'D': 1, 'F': 2,
            'G': 3, 'X': 4
        }
        self.replace = ()

    def create_square(self, alphabet):
        """ Cria o quadrado para o alfabeto cifrado """
        self.square = Cipher.create_square(self, alphabet=alphabet)

    def get_adfgx(self, col, lin):
        """ Com as coordenadas, retorna o par de letras ADFGX correspondente """
        out = ''
        for char, value in self.chars.items():
            if col == value:
                out = char + out
            if lin == value:
                out += char
        return out

    def get_letter(self, ch):
        """ Com um par ADFGX, retorna uma letra do quadrado """
        i = self.chars[ch[0]]
        j = self.chars[ch[1]]
        return self.square[i][j]

    def set_replace(self, ch1, ch2):
        """ Substitui ch1 por ch2 """
        self.replace = (ch1, ch2)

    def encrypt(self, text, key):
        """ Cifra o texto com a cifra ADFGX """
        text = self.format_str(text)
        if self.replace:
            if self.replace[0] in text:
                text = text.replace(self.replace[0], self.replace[1])
        txt = []
        for letra in text:
            for col, text in enumerate(self.square):
                if letra in text:
                    lin = text.index(letra)
                    txt.append(self.get_adfgx(col, lin))
        ctxt = {}
        idx = 0
        for ch in ''.join(txt):
            if ctxt.get(key[idx]):
                ctxt[key[idx]] = ctxt.get(key[idx]) + ch
            else:
                ctxt[key[idx]] = ch
            if idx < len(key) - 1:
                idx += 1
            else:
                idx = 0
        ciphertext = ''
        for ch in sorted(ctxt):
            ciphertext += ctxt[ch]
        return ciphertext

    def decrypt(self, text, key):
        """ Decifra texto cifrado com a cifra ADFGX """
        extra = ''
        tam = len(text) % len(key)
        if tam:
            extra = key[:tam]
        fix = len(text) // len(key)
        okey = sorted(key)
        ptxt = {}
        idx = 0
        ext = 0
        for ch in okey:
            if ch in extra:
                ext = 1
            else:
                ext = 0
            ptxt[ch] = text[idx:idx + fix + ext]
            idx += fix + ext
        adfgx = ''
        for i in range(len(ptxt[key[0]])):
            for ch in key:
                if i < len(ptxt[ch]):
                    adfgx += ptxt[ch][i]
        plain = ''
        for _ in range(0, len(adfgx), 2):
            plain += self.get_letter(adfgx[_:_+2])
        return plain
