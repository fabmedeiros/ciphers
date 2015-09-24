class Morse(object):
    def __init__(self):
        self.morse_code = {
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....',
            'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',
            'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--',
            '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }

    def decode(self, morsecode):
        ''' Decodifica codigo morse '''
        code = morsecode.split(' ')
        text = ''
        for item in code:
            for key, value in self.morse_code.iteritems():
                if item == value:
                    text += key
                    break
        return text

    def encode(self, plaintext):
        ''' Codifica em codigo morse '''
        code = ''
        for char in plaintext.upper():
            if char in self.morse_code.keys():
                code += self.morse_code[char] + ' '
        return code
