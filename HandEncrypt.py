#! python27
'''
Printable/Typable character output encryption tool.
Algorithm: Onepad encryption alogorithm
Author: S.Haseeb
'''
import random

class onepad:
    def encrypt(self, text):
        '''Function to encrypt text using psedo-random numbers'''
        plain = []
        key = []
        cipher = []
        for i in text:
            plain.append(ord(i))
        for i in plain:
            k = random.randint(0, 300)
            c = (i+k)*k
            cipher.append(c)
            key.append(k)
        return cipher, key
    
    def decrypt(self, cipher, key):
        '''Function to decrypt text using psedo-random numbers.'''
        plain = []
        for i in range(len(key)):
            p = (cipher[i]-(key[i])**2)/key[i]
            plain.append(chr(p))
        plain = ''.join([i for i in plain])
        return plain

c,k = onepad().encrypt('Hello')
print onepad().decrypt(c, k)
