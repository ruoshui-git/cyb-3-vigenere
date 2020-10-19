from itertools import cycle
from sys import argv

ord_A = ord('A')

def encrypt(text: str, key: str) -> str:
    '''Encrypt a string with given key in vigenere cipher.

    Table is assumed to be constructed from standard alphabet order

    Any non-alphabet character is skipped and does not use up a letter in key
    '''
    return _transform(text, key)


def decrypt(text: str, key: str) -> str:
    '''Decrypt a string with given key in vigenere cipher.

    Table is assumed to be constructed from standard alphabet order

    Any non-alphabet character is skipped and does not use up a letter in key
    '''
    return _transform(text, key, encode=False)


def _transform(text: str, key: str, encode=True):
    src = []
    ki = cycle(key.upper())
    for t in text.upper():
        if t.isalpha():
            k = next(ki)
            if encode:
                src.append(
                    chr((ord(t) - ord_A + (ord(k) - ord_A)) % 26 + ord_A))
            else:
                src.append(
                    chr((ord(t) - ord_A - (ord(k) - ord_A)) % 26 + ord_A))
        else:
            src.append(t)
    return "".join(src)

if __name__ == "__main__":

    if len(argv) != 4:
        print('useage: python vigenere.py encode/decode text key')
        exit(1)
    cmd = argv[1]
    src = argv[2]
    key = argv[3]

    if cmd == 'encode':
        result =         encrypt(src, key)
    elif cmd == 'decode':
        result = decrypt(src, key)
    else:
        print(f'command "{cmd}" not recognized')
        exit(1)
    
    print(result)