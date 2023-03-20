# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, '..')

from ciphers import Playfair

'''
txt_in = input('Texto a ser codificado: ')
chave = input('Chave:')
if chave:
    chave = int(chave)
else:
    chave = 3
cifra = Caesar()
cifrado = cifra.encrypt(txt_in, chave)
print('Texto cifrado: ', cifrado)
print('  Texto plano: ', cifra.decrypt(cifrado, chave))
'''

text = 'WQ EM YK HK CS UP LD FR UP ZP IK TA RK LE TR LS YS QX TR SU EF CS DK GZ'

cifra = Playfair()
print(text)
print(cifra.decrypt(text, 'DRSEU'))
