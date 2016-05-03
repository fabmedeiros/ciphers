# -*- coding: utf-8 -*-
from .cipher import Cipher
""" implementacao da cifra Railfence """

class Railfence(Cipher):
    ''' Cifra railfence '''
    def gen_railfence(self, tam, key):
        '''
        Retorna um lista de inteiros com a posicao da linha que o caracter
        do texto ira ocupar, variando de 0 ate key - 1.
        '''
        j = 0
        inc = 0
        idx = []
        for i in range(tam):
            if j == key - 1:
                inc = -1
            elif j == 0:
                inc = 1
            idx.append(j)
            j += inc
        return idx

    def encrypt(self, texto, key):
        '''
        Retorna o texto plano cifrado na cifra rail fence com a chave key.
        '''
        tabela = []
        for i in range(key):
            tabela.append([])
        i, idx = 0, 1
        texto = self.format_str(texto)
        for ch in texto:
            tabela[i].append(ch)
            if i == key - 1:
                idx = -1
            elif i < 1:
                idx = 1
            i += idx
        saida = ''
        for tab in tabela:
            saida += ''.join(tab)
        return saida

    def decrypt(self, texto, key):
        '''
        Retorna o texto plano para um texto cifrado com a cifra railfence
        com a chave key.
        '''
        texto = self.format_str(texto)
        tam = len(texto)
        # gera lista com os indices do railfence
        idx = self.gen_railfence(tam, key)
        # ordena a lista de indices do railfence
        idx_sorted = sorted(idx)
        # faz uma busca em idx e idx_sorted, verificando os indices
        # e colocando os caracters de acordo com a posicao no railfence
        texto_plano = ''
        for i in range(tam):
            for j in range(tam):
                if idx[i] == idx_sorted[j] and idx[i] > -1:
                    texto_plano += texto[j]
                    idx[i] = -1
                    idx_sorted[j] = -1
        return texto_plano.lower()
