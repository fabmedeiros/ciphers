#cifra de substituicao simples
from .cipher import Cipher

class SimpleSubstitution(Cipher):
    def __init__(self):
        self.decrypting = False

    def cipher_alphabet(self, password):
        '''
        Retorna um alfabeto cifrado iniciado com
        o texto da palavra chave password
        '''
        c_alphabet = []
        password = password.upper()
        for ch in password:
            if ch not in c_alphabet:
                c_alphabet.append(ch)
                idx = Cipher.plain_alphabet.find(ch)
        p_alphabet = self.shift_alphabet(Cipher.plain_alphabet, idx)
        for ch in p_alphabet:
            if ch not in c_alphabet:
                c_alphabet.append(ch)
        return ''.join(c_alphabet)

    def encrypt(self, plaintext, password):
        '''
        Retorna o texto plano cifrado com a cifra de
        substituicao com a palavra chave password
        '''
        txt = ''
        p_alphabet = Cipher.plain_alphabet
        text = self.format_str(plaintext)
        cipher = self.cipher_alphabet(password)
        if self.decrypting:
            p_alphabet, cipher = cipher, p_alphabet
            self.decrypting = False
        for ch in text:
            txt += cipher[p_alphabet.find(ch)]
        return txt

    def decrypt(self, ciphertext,  password):
        '''
        Retorna o texto cifrado decifrado com a cifra de
        substituicao com a palavra chave password
        '''
        self.decrypting = True
        return self.encrypt(ciphertext, password)
