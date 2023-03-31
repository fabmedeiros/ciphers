import sys

sys.path.insert(0, '..')
print(sys.path)

import streamlit as st
from ciphers import Playfair

text = 'WQ EM YK HK CS UP LD FR UP ZP IK TA RK LE TR LS YS QX TR SU EF CS DK GZ'
cifra = Playfair()
print(cifra.decrypt(text, 'DRSEU'))

st.write(text)
ciphertext = st.text_input('Texto cifrado')
password = st.text_input('Senha')

if st.button('Clique'):
    st.text('CIFRAGEM')
    st.write(cifra.decrypt(ciphertext, password))
