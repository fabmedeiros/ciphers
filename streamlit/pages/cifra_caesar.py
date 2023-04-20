import sys

sys.path.insert(0, '..')
print(sys.path)

import streamlit as st
from ciphers import Caesar

cifra = Caesar()

ciphertext = st.text_input('Texto cifrado')
password = st.text_input('Senha')

if st.button('Clique'):
    st.text('CIFRAGEM')
    st.write(cifra.decrypt(ciphertext, password))
