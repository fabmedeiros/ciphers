from cipher import Cipher
""" Implementacao das Cifras Hebraicas Atbash, Albam e Atbah """


class Hebrew(Cipher):
    atbash = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    albam = 'NOPQRSTUVWXYZABCDEFGHIJKLM'
    atbah = 'IHGFNDCBARQPOEMLKJZYXWVUTS'

    def encrypt(self, text, cipher):
        '''
        Retorna o texto cifrado com a cifra hebraica escolhida
        '''
        txt = ''
        text = self.format_str(text)
        for ch in text:
            idx = Cipher.plain_alphabet.find(ch)
            txt += cipher[idx]
        return txt

    def decrypt(self, text, cipher):
        '''
        Retorna o texto decifrado com a cifra hebraica escolhida
        '''
        return self.encrypt(text, cipher).lower()
