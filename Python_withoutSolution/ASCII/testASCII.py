# -*- coding: utf-8 -*-
# Name of file: test.py
# import numpy package
import numpy as np
# import character string conversion module
import my_string_functions as string

################################################################################
# AES128 parameters
################################################################################
# plaintext length in bytes
PLAINTEXT_LENGTH = 16
# key length in bytes
KEY_LENGTH = 16
# number of rounds
ROUNDS = 10

################################################################################
# ASCII text of any length (string of characters)
################################################################################
text_ASCII = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# padding with spaces to set len(text)/PLAINTEXT_LENGTH to the nearest integer
text_ASCII=string.textpadd(text_ASCII,PLAINTEXT_LENGTH)

################################################################################
# convert ASCII text to vectors of plaintexts in integer and hexadecimal form 
################################################################################
[plaintext_int,plaintext_hex]=string.convert_ASCII2plaintexts(text_ASCII,PLAINTEXT_LENGTH)

# retrieve total number of plaintexts
plaintext_nb=plaintext_int.shape[0]

print("\nASCII text:")
print(text_ASCII)
print("\nInt plaintexts:")
for i in range(plaintext_nb):
    print(plaintext_int[i,:])
print("\nHex plaintexts:")
for i in range(plaintext_nb):
    print(plaintext_hex[i,:])
    
################################################################################
# vectors of plaintexts in integer form converted back to ASCII text  
################################################################################
text_ASCII=string.convert_Intplaintexts2ASCII(plaintext_int)
print("\nASCII text backward conversion from Int plaintexts:")
print(text_ASCII)

################################################################################
# vectors of plaintexts in hexadecimal form converted back to ASCII text  
################################################################################
text_ASCII=string.convert_Hexplaintexts2ASCII(plaintext_hex)
print("\nASCII text backward conversion from Hex plaintexts:")
print(text_ASCII)
