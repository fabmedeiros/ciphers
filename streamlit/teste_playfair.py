import sys

sys.path.insert(0, '..')
print(sys.path)

import streamlit as st
from ciphers import Playfair

text = 'WQ EM YK HK CS UP LD FR UP ZP IK TA RK LE TR LS YS QX TR SU EF CS DK GZ'
cifra = Playfair()
print(cifra.decrypt(text, 'DRSEU'))

st.write(text)
texto = st.text_input('Texto cifrado')
if st.button('Clique'):
    st.write(cifra.decrypt(text, 'DRSEU'))
    st.text('CIFRAGEM')
    st.write(cifra.decrypt(texto, 'DRSEU'))
