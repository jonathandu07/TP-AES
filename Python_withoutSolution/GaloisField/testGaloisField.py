# -*- coding: utf-8 -*-
# Name of file: test.py
# import numpy package
import numpy as np
# import F_256 Galois Field module
import my_gf_functions as gf

################################################################################
#
#  Define the Logtable and and its inverse Alogtable for all elements in F_256
#  as global variables
#
#  outputs: let g^i is in integer form, where g is a generator of F_256
#  - Logtable[g^i]=i for i=0,..,254 by convention Logtable[0]=0
#  - Alogtable[i]=g^i for i=0,..,255
#
################################################################################
def Generate_Logtable_Alogtable():
   # define the generator of F_256
   g=int('0x03',16)
   # initialize Logtable
   Logtable=np.zeros(256,dtype='int')

   # initialize inverse Logtable
   Alogtable=np.zeros(256,dtype='int')

   """FILL IN MISSING CODE"""

   return Logtable,Alogtable

################################################################################
# Tabular representation of xtime(xy)
################################################################################
"""FILL IN MISSING CODE"""

################################################################################
# Example of addition in F_256
################################################################################
# a1='0xa1' in hexadecimal form converted to integer form
a1=int('0xa1',16)
# b1='0x12' in hexadecimal form converted to integer form
b1=int('0x12',16)
# print a1+b1='0xb3' in hex form
"""FILL IN MISSING CODE"""

################################################################################
# Example of slow multiplication in F_256 using xtime()
################################################################################
# a2='0x57' in hexadecimal form converted to integer form
a2=int('0x57',16)
# b2='0x83' in hexadecimal form converted to integer form
b2=int('0x83',16)
# print a2*b2='0xc1' in hex form
"""FILL IN MISSING CODE"""

################################################################################
# Show that a='0x03' generates F_256
################################################################################
a=int('0x03',16)
print('powers of the generator:\n')
# print all powers of a 
for i in range(256):
    if i == 0:
        tmp=int('0x01',16)
    else:
        """FILL IN MISSING CODE"""
        
    print('a^',i,'=',hex(tmp),'\n')

################################################################################
# Galois Field F_256 parameters using irreducible polynomial m(x)=x^8+x^4x^3+x+1
################################################################################
# generate Logtable and Alogtable
[Logtable,Alogtable]=Generate_Logtable_Alogtable()
# print Logtable
for i in range(256):
    print('Logtable[',i,']=',Logtable[i])
    if i%16==15:
        print('\n')
# print Alogtable
for i in range(256):
    print('Alogtable[',i,']=',Alogtable[i])
    if i%16==15:
        print('\n')
    
################################################################################
# Example of fast multiplication in F_256 using Logtable() and Alogtable()
################################################################################
# a2='0x57' in hexadecimal form converted to integer form
a2=int('0x57',16)
# b2='0x83' in hexadecimal form converted to integer form
b2=int('0x83',16)
# print a2*b2='0xc1' in hex form
"""FILL IN MISSING CODE"""

################################################################################
# Example of fast inversion in F_256 using Logtable() and Alogtable()
################################################################################
# a='0x83' in hexadecimal form converted to integer form
a=int('0x83',16)
a_inv=gf.inv(a)
# print a^{-1}='0x80'
print("a^{-1}=",hex(a_inv))

################################################################################
# Example of fast division in F_256 using Logtable() and Alogtable()
################################################################################
# a='0x01' in hexadecimal form converted to integer form
a=int('0x01',16)
# a='0x83' in hexadecimal form converted to integer form
b=int('0x83',16)
res=gf.div(a,b)
# print a/b='0x80'
print("a/b=",hex(res))



