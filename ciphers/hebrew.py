from cipher import Cipher
""" Implementacao das Cifras Hebraicas Atbash, Albam e Atbah """


class HebrewCipher(Cipher):
    atbash = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    albam = 'NOPQRSTUVWXYZABCDEFGHIJKLM'
    atbah = 'IHGFNDCBARQPOEMLKJZYXWVUTS'

    def __init__(self):
        self.plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt(self, text, cipher):
        '''
        Retorna o texto cifrado com a cifra hebraica escolhida
        '''
        txt = ''
        text = self.format_str(text)
        for ch in text:
            idx = self.plain.find(ch)
            txt += cipher[idx]
        return txt

    def decrypt(self, text, cipher):
        '''
        Retorna o texto decifrado com a cifra hebraica escolhida
        '''
        return self.encrypt(text, cipher).lower()
