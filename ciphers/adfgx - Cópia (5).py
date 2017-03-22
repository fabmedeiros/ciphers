# -*- coding: utf-8 -*-

from cipher import Cipher

class ADFGX(Cipher):
    def __init__(self):
        self.chars = {
            'A': 0, 'D': 1, 'F': 2,
            'G': 3, 'X': 4
        }

    def create_square(self, alphabet):
        self.square = Cipher.create_square(self, alphabet=alphabet)

    def letras(self, col, lin):
        '''Com as coordenadas, retorna as letras correspondentes'''
        out = ''
        for char, value in self.chars.items():
            if col == value:
                out = char + out
            if lin == value:
                out += char
        return out

    def encrypt(self, text, key):
        # guarda o texto cifrado sem senha
        text = self.format_str(text)
        if 'J' in text:
            text = text.replace('J', 'I')
        txt = []
        for letra in text:
            lin = None
            col = None
            for col, text in enumerate(self.square):
                if letra in text:
                    lin = text.index(letra)
                    txt.append(self.letras(col, lin))
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
            plain += self.retorno(adfgx[_:_+2])
        return(plain)

    def retorno(self, ch):
        """ Retorna os indices com as letras """
        i = self.chars[ch[0]]
        j = self.chars[ch[1]]
        return self.square[i][j]

    def show_square(self):
        """ """
        show = ' |A|D|F|G|X|\n'
        keys = sorted(cifra.chars.keys())
        lista = ''
        for idx, key in enumerate(keys):
            for letra in self.square[idx]:
                lista += letra + '|'
            show += key + '|' + lista + '\n'
            lista = ''
        return show

# cria uma matriz de 5x5 aleatoria
# com o texto para cifrar usa a primeira matriz
# com uma chave ordena o texto em colunas
# ordenam-se as colunas
# texto cifrado

if __name__ == '__main__':
    cifra = ADFGX()
    alfabeto = 'ZCBDMHAOINLRSPQWXEUTYFGKV'
    cifra.create_square(alfabeto)
    cifrado = cifra.encrypt('FABIO mariano de medeiros', 'SENHADF')
    print(cifrado)
    print(cifra.decrypt(cifrado, 'SENHADF'))

# opcao com alfabeto gerado
# opcao com alfabeto proprio

def imprimir(texto: str) -> str:
    """ imprime texto """
    print(texto)

def imprimir_2(texto):
    # type: (str) -> str
    """ imprime texto """
    print(texto)
