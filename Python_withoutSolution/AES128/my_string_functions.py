# -*- coding: utf-8 -*-
# Name of file: my_string_functions.py
# import numpy package
import numpy as np

#####################################################################
#
#  Padding of original ASCII text with spaces
#  (length must be a multiple of PLAINTEXT_LENGTH) 
#
#  inputs:
#  - text[]: string of ASCII characters
#  - PLAINTEXT_LENGTH: plaintext length in bytes
#
#  outputs:
#  - text_padding[]: original ASCII text after padding (if necessary)
#
####################################################################
def textpadd(text,PLAINTEXT_LENGTH):
   # copy original text
   text_padding = text
   # retrieve original number of ASCII characters
   text_length=len(text)
   # if character string is empty
   if text_length==0:
      # padd the original text with PLAINTEXT_LENGTH spaces
      for i in range(PLAINTEXT_LENGTH):
         text_padding = text_padding + " "
   # or its length is not  multiple of PLAINTEXT_LENGTH
   elif (text_length % PLAINTEXT_LENGTH)>0:
      # padd the original text with spaces
      for i in range(text_length,int(np.floor(text_length/PLAINTEXT_LENGTH)+1)*PLAINTEXT_LENGTH):
         text_padding = text_padding + " "
        
   return text_padding

#####################################################################
#
#  Convert ASCII text to matrices of plaintexts in integer and hexadecimal form
#
#  inputs:
#  - text_ASCII: string of ASCII characters
#  - PLAINTEXT_LENGTH: plaintext length in bytes
#
#  outputs:
#  - plaintext_int[:,PLAINTEXT_LENGTH]: successive plaintexts coming as length-PLAINTEXT_LENGTH vectors in int form 
#  - plaintext_hex[:,PLAINTEXT_LENGTH]: successive plaintexts coming as length-PLAINTEXT_LENGTH vectors in hex form
#
####################################################################
def convert_ASCII2plaintexts(text_ASCII,PLAINTEXT_LENGTH):
   # total number of plaintexts to cypher
   plaintext_nb=int(len(text_ASCII)/PLAINTEXT_LENGTH)

   # init matrix of plaintexts in integer form
   plaintext_int=np.zeros((plaintext_nb,PLAINTEXT_LENGTH),dtype=int)
   # init matrix of plaintexts in hexadecimal form
   plaintext_hex=np.zeros((plaintext_nb,PLAINTEXT_LENGTH),'U4')

   # for each character in the ASCII text
   counter=0
   for i in text_ASCII:
      # convert i-th ASCII character to integer and save
      plaintext_int[counter // PLAINTEXT_LENGTH,counter % PLAINTEXT_LENGTH] = ord(i)
      # convert i-th ASCII character to hexadecimal and save
      plaintext_hex[counter // PLAINTEXT_LENGTH,counter % PLAINTEXT_LENGTH] = hex(ord(i))
      counter=counter+1

   return plaintext_int,plaintext_hex

#####################################################################
#
#  Convert plaintexts in integer form to ASCII text
#
#  inputs:
#  - plaintext_int[:,PLAINTEXT_LENGTH]: successive plaintexts in int form
#    coming as successive length-PLAINTEXT_LENGTH vectors 
#  outputs:
#  - text_ASCII[]: string of ASCII characters
#
####################################################################
def convert_Intplaintexts2ASCII(plaintext_int):
   # retrieve total number of plaintexts
   plaintext_nb=plaintext_int.shape[0]
   # retrieve plaintext length (in number of bytes)
   PLAINTEXT_LENGTH=plaintext_int.shape[1]

   # create empty ASCII string
   text_ASCII = ""

   # concatenate plaintext blocks to ASCII character string
   for l in range(plaintext_nb):
      for c in range(PLAINTEXT_LENGTH):
         # retrieve the character in position (l,c) and convert to ASCII
         text_ASCII =  text_ASCII + chr(plaintext_int[l,c])

   return text_ASCII

#####################################################################
#
#  Convert plaintexts in hexadecimal form to ASCII text
#
#  inputs:
#  - plaintext_hex[:,PLAINTEXT_LENGTH]: successive plaintexts in hex form
#    coming as successive length-PLAINTEXT_LENGTH vectors
#  outputs:
#  - text_ASCII[]: string of ASCII characters
#
####################################################################
def convert_Hexplaintexts2ASCII(plaintext_hex):
   # retrieve total number of plaintexts
   plaintext_nb=plaintext_hex.shape[0]
   # retrieve plaintext length (in number of bytes)
   PLAINTEXT_LENGTH=plaintext_hex.shape[1]

   # create empty ASCII string
   text_ASCII = ""

   # concatenate plaintext blocks to ASCII character string
   for l in range(plaintext_nb):
      for c in range(PLAINTEXT_LENGTH):
         # retrieve the character in position (l,c) and convert to ASCII
         text_ASCII =  text_ASCII + chr(int(plaintext_hex[l,c],16))

   return text_ASCII
