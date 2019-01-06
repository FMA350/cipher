import os
import sys

def vigenere(self, ciphertext, key, toggle_decription):
    if(ciphertext == ""):
        print "Type the string to encipher"
        ciphertext = raw_input()

    if (key == ""):
        print "the key provided is too short!"
        return
    else:
        index = 0
        new_word = ""
        if(toggle_decription):
            print "deciphering the text..."
            for letter in ciphertext:
                new_word = new_word + chr(((ord(letter)-97)-(ord(key[index])-97))%26+97)
                # works because python modulo operator returns always a
                # value witht the same sign as the denumerator.
                # This is different from C!
                index +=1
                if (index == len(key)):
                    index = 0
        else:
            print "encriptiong the text..."
            for letter in ciphertext:
                new_word = new_word + chr(((ord(letter)-97)+(ord(key[index])-97))%26+97)
                index +=1
                if (index == len(key)):
                    index = 0
        print new_word
