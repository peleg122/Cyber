#!/usr/bin/python

import sys

# Part1:

file = open(sys.argv[1], 'r')
text = file.readlines()
line1 = text[0][0:-1].upper()
line2 = text[1].upper()
numberOfChars = len(line2)


def exhaustive_search(plainTxt):
    counter = 0
    working_line = plainTxt
    number = 0
    if len(line2) != len(plainTxt):
        print("Wrong input...")
    elif numberOfChars <= 0:
        print "None,", counter
    elif numberOfChars > 0:
        while counter != 25:
            final_message = ""
            if counter == 0:
                print working_line + ",", counter
            for x in range(0, len(working_line)):
                if ord(working_line[x]) in range(65, 91):
                    final_message += (chr(((ord(working_line[x])-64) % 26)+65))
            counter = counter + 1
            working_line = final_message
            if line2 == final_message:
                number = counter
            print working_line+",", counter
        if number == 0:
            print "No Solution"
        else:
            print number
        return number


exhaustive_search(line1)

# Part 2:

file2 = open(sys.argv[2], 'r')
# dictionary
theDict = {chr(y): y-65 for y in range(65, 91)}
# my ID as Key
my_code = "DBGEIGHIG"
# reading lines from txt
text2 = file2.readlines()
message = text2[0].upper()
encypt = text2[2].upper()


def vigenere_cipher_decrypt(plainTxt, key):
    cipher = ""
    new_code = key
    if len(plainTxt) > len(new_code):
        new_code += new_code[0:len(plainTxt) - len(new_code)]
    for x in range(0, len(plainTxt)):
        if ord(plainTxt[x]) in range(65, 91):
            cipher += (chr((((ord(plainTxt[x]) - 65) + (ord(new_code[x]) - 65)) % 26) + 65))
    print ('\n')
    return cipher


print vigenere_cipher_decrypt(message, my_code)


def vigenere_cipher_key(plainTxt, cipherTxt):
    key = ""
    for x in range(0, len(plainTxt)):
        if ord(plainTxt[x]) in range(65, 91):
            key += (chr((((ord(cipherTxt[x]) - 65) - (ord(plainTxt[x]) - 65)) % 26) + 65))
    print key


vigenere_cipher_key(message, vigenere_cipher_decrypt(message, my_code))
