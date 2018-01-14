'''
securipy.py
Author: Haseeb
'''
#!python27
import os

class Secure:
    '''
    Contains function for destroying information at source.
    '''
    def delete(self, filepath, passes=1):
        for i in range(passes):
            fd = open(filepath)
            length = len(fd.read())
            fd.close()
            del fd
            fd = open(filepath, 'wb')
            fd.write(os.urandom(length+1))
            fd.close()
            del fd
        os.remove(filepath)
