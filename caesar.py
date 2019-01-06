import os
import sys

def caesar(self, ciphertext, key, toggle_decription):
    print
    rotation = int(key)

    if not (isinstance(rotation, int)):
        print "the argument provided is not a number!"
        return
    else:
        if(toggle_decription):
            rotation = -rotation
        if(ciphertext == ""):
            print "Type the string to encipher"
            ciphertext = raw_input()

        new_word = ""
        for letter in ciphertext:
            new_word = new_word + chr(((ord(letter)-97)+rotation)%26+97)
        print new_word
