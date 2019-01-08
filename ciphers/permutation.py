#cifra de substituicao simples
from cipher import Cipher

class Permutation(Cipher):
    def __init__(self):
        pass
        #self.decrypting = False

    def encrypt(self, plaintext, key):
        '''
        Retorna o texto plano cifrado com permutacao simples
        '''
        txt = ''
        text = self.format_str(plaintext)
        matriz = []
        idx = 0
        for i in range(0, len(key)):
            idx = i * len(key)
            matriz.append(text[idx:idx + len(key)])
        print(matriz)

        matriz = []
        idx = 0
        while idx < len(text):
            #print(idx)
            matriz.append(text[idx:idx + len(key)])
            idx += len(key)
        print(matriz)
        
        #return matriz

    def decrypt(self, ciphertext,  password):
        '''
        Retorna o texto cifrado decifrado com a cifra de
        substituicao com a palavra chave password
        '''
        self.decrypting = True
        return self.encrypt(ciphertext, password)
