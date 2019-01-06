#file: "main.py"
import os
import sys
import getopt

import caesar
import vigenere


METHOD_NAME = "method_name"

class Cipherbox:
    toggle_decription = 0
    ciphertext = ""
    key = ""



def main(argv):
    if(len(sys.argv) < 2):
        print "Wrong number of arguments"
        print_help()
        sys.exit(1)
    cipherbox = Cipherbox()

    try:
        opts, args = getopt.getopt(argv, "c:v:edt:h")
    except getopt.GetoptError:
        print "### error, wrong argument"
        print_help()
        sys.exit(2)

    for opt, arg in opts:

        if opt == '-h':
            print_help()
            exit(0)

        elif opt  == '-c':
            print "you selected the Caesar cipher"
            cipherbox.key = arg
            print "key is "+ cipherbox.key
            setattr(Cipherbox, METHOD_NAME, caesar.caesar)

        elif opt == '-v':
            print "you selected the Vigenere cipher"
            cipherbox.key = arg
            setattr(Cipherbox, METHOD_NAME, vigenere.vigenere)

        elif opt == '-d':
            print "you choose deciphering"
            cipherbox.toggle_decription = 1

        elif opt == '-e':
            print "you choose enciphering"
            cipherbox.toggle_decription = 0

        elif opt == '-t':
            cipherbox.ciphertext = arg
            print cipherbox.ciphertext
    cipherbox.method_name(cipherbox.ciphertext, cipherbox.key, cipherbox.toggle_decription)



def print_help():
    print "### Usage ###"
    print "# -h displays this help message"
    print "# -c [number] launches the caesar cipher"
    print "# -v [word]   launches the vigenere cipher"
    print "# Use python V. 2.x"

if __name__ == "__main__":
   main(sys.argv[1:])
