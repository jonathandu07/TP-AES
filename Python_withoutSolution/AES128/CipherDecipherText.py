# -*- coding: utf-8 -*-
# Name of file: test.py
# import numpy package
import numpy as np
# import character string conversion module
import my_string_functions as string
# import AES128 Encyption/Decryption module
import my_aes128_functions as aes128

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
# AES128 text encryption
################################################################################
# select a key
key=np.array([int('0x00',16),int('0x11',16),int('0x22',16),int('0x33',16),int('0x44',16),int('0x55',16),int('0x66',16),int('0x77',16),int('0x88',16),int('0x99',16),int('0xaa',16),int('0xbb',16),int('0xcc',16),int('0xdd',16),int('0xee',16),int('0xff',16)],dtype='int')

# block-by-block encryption
cyphertext=np.zeros((plaintext_nb,PLAINTEXT_LENGTH),dtype='int')
for i in range(plaintext_nb):
    [cyphertext[i,:],__]=aes128.Encrypt(plaintext_int[i,:],key,ROUNDS)
    
################################################################################
# AES128 text decryption
################################################################################
# block-by-block decryption
decypheredtext=np.zeros((plaintext_nb,PLAINTEXT_LENGTH),dtype='int')
for i in range(plaintext_nb):
    [decypheredtext[i,:],__]=aes128.Decrypt(cyphertext[i,:],key,ROUNDS)
    
################################################################################
# vectors of plaintexts in integer form converted back to ASCII text  
################################################################################
text_ASCII=string.convert_Intplaintexts2ASCII(decypheredtext)
print("\nASCII text backward conversion from decyphertext:")
print(text_ASCII)
