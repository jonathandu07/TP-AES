# -*- coding: utf-8 -*-
# Name of file: test.py
# import numpy package
import numpy as np
# import F_256 Galois Field module
import my_gf_functions as gf
# import AES transformations module
import my_transformations_functions as transfo

################################################################################
# Tabular representation of Sbox
# Tab. C.2 p. 212 in Daemen and Rijnen, "The design of Rijndael," Springer 2002 
################################################################################
# print all elements in F_216 in integer form the corresponding Sbox output
print('\nTabular representation of Sbox(a)')  
for a in range(256):
    print('a=',hex(a),hex(transfo.Sbox(a)))
  
################################################################################
# Tabular representation of InvSbox
# Tab. C.1 p. 211 in Daemen and Rijnen, "The design of Rijndael," Springer 2002 
################################################################################
# print all elements in F_216 in integer form the corresponding Sbox output
print('\nTabular representation of InvSbox(a)')  
for a in range(256):
    print('a=',hex(a),hex(transfo.InvSbox(a)))

################################################################################
# test ShiftRows() and InvShiftRows()
################################################################################
# define the state
state=np.array([[int('0x87',16),int('0xf2',16),int('0x4d',16),int('0x97',16)],
                [int('0xec',16),int('0x6e',16),int('0x4c',16),int('0x90',16)],
                [int('0x4a',16),int('0xc3',16),int('0x46',16),int('0xe7',16)],
                [int('0x8c',16),int('0xd8',16),int('0x95',16),int('0xa6',16)]],dtype='int')

# Apply Shift rows tranformation to the state
"""state after Shift rows  =
[['0x87' '0xf2' '0x4d' '0x97']
 ['0x6e' '0x4f' '0x90' '0xec']
 ['0x46' '0xe7' '0x4a' '0xc3']
 ['0xa6' '0x8c' '0xd8' '0x95']]"""
tmp=transfo.ShiftRows(state)
print('\nAfter Shift row :')
print(np.array([[hex(l) for l in row] for row in tmp]))
# Apply Inverse Shift rows tranformation to get back to the original state
state=transfo.InvShiftRows(tmp)
print('After Inverse Shift row:')
print(np.array([[hex(l) for l in row] for row in state]))

################################################################################
# check that shared.Minv is the inverse matrix of shared.M in F_256
################################################################################
# show that shared.Minv x shared.M = Identity matrix in F_256
# set state to shared.Minv
state=np.array([[int('0x0e',16),int('0x0b',16),int('0x0d',16),int('0x09',16)],
                [int('0x09',16),int('0x0e',16),int('0x0b',16),int('0x0d',16)],
                [int('0x0d',16),int('0x09',16),int('0x0e',16),int('0x0b',16)],
                [int('0x0b',16),int('0x0d',16),int('0x09',16),int('0x0e',16)]],dtype='int')
# Apply Mix column tranformation to the state
tmp=transfo.MixColumn(state)
print('\nprint shared.Minv x shared.M :')
print(np.array([[hex(l) for l in row] for row in tmp]))

################################################################################
# test MixColumn() and InvMixColum()
################################################################################
# define the state
state=np.array([[int('0x87',16),int('0xf2',16),int('0x4d',16),int('0x97',16)],
                [int('0x6e',16),int('0x4c',16),int('0x90',16),int('0xec',16)],
                [int('0x46',16),int('0xe7',16),int('0x4a',16),int('0xc3',16)],
                [int('0xa6',16),int('0x8c',16),int('0xd8',16),int('0x95',16)]],dtype='int')

# Apply Mix column tranformation to the state
tmp=transfo.MixColumn(state)
print('\nAfter Mix column :')
print(np.array([[hex(l) for l in row] for row in tmp]))
# Apply Inverse Mix column tranformation to get back to the original state
state=transfo.InvMixColumn(tmp)
print('After Inverse Mix column :')
print(np.array([[hex(l) for l in row] for row in state]))


################################################################################
# test KeyExpansion()
################################################################################
# define number of rounds
ROUNDS=10
# define key as a vector of bytes in integer form

# Example1: Vergnaud, exercices et problèmes de cryptograpie, 2è Ed, Dunod 2015
# Ex. 2.17 p. 63-64 (Rq: il y a une erreur due au fait que la matrice de clé d'origine est lue ligne par ligne oau lieude colonne par collone comme dans le standard AES !)
"""round key 1 =
[['0xc0' '0x84' '0x0c' '0xc0']
 ['0x39' '0x6c' '0xf5' '0x28']
 ['0x34' '0x52' '0xf8' '0x16']
 ['0x78' '0x0f' '0xb4' '0x4b']]"""
original_key=np.array([int('0x00',16),int('0x11',16),int('0x22',16),int('0x33',16),int('0x44',16),int('0x55',16),int('0x66',16),int('0x77',16),int('0x88',16),int('0x99',16),int('0xaa',16),int('0xbb',16),int('0xcc',16),int('0xdd',16),int('0xee',16),int('0xff',16)],dtype='int')

# W. Stallings, Cryptography and Network Security Principles, 7th Ed, Pearson 
# p. 193 Table 6.3
"""round key 0 =
[['0x0f' '0x47' '0x0c' '0xaf']
 ['0x15' '0xd9' '0xb7' '0x7f']
 ['0x71' '0xe8' '0xad' '0x67']
 ['0xc9' '0x59' '0xd6' '0x98']]"""
original_key=np.array([int('0x0f',16),int('0x15',16),int('0x71',16),int('0xc9',16),int('0x47',16),int('0xd9',16),int('0xe8',16),int('0x59',16),int('0x0c',16),int('0xb7',16),int('0xad',16),int('0xd6',16),int('0xaf',16),int('0x7f',16),int('0x67',16),int('0x98',16)],dtype='int')
# Apply key expansion 
rk=transfo.ExpandKey(original_key,ROUNDS)

for rd in range(ROUNDS+1):
    print('\nround key',rd,'=')
    print(np.array([[hex(l) for l in row] for row in rk[rd,:,:]]))

# Example3: avalanche effect in AES key change by 1 bit in position 8 
# W. Stallings, Cryptography and Network Security Principles, 7th Ed, Pearson 
# p. 197 Table 6.4
# original message 1 as a vector of bytes in integer form
original_message1=np.array([int('0x01',16),int('0x23',16),int('0x45',16),int('0x67',16),int('0x89',16),int('0xab',16),int('0xcd',16),int('0xef',16),int('0xfe',16),int('0xdc',16),int('0xba',16),int('0x98',16),int('0x76',16),int('0x54',16),int('0x32',16),int('0x10',16)],dtype='int')
# original key 1 as a vector of bytes in integer form
original_key1=np.array([int('0x0f',16),int('0x15',16),int('0x71',16),int('0xc9',16),int('0x47',16),int('0xd9',16),int('0xe8',16),int('0x59',16),int('0x0c',16),int('0xb7',16),int('0xad',16),int('0xd6',16),int('0xaf',16),int('0x7f',16),int('0x67',16),int('0x98',16)],dtype='int')

# original message 2: flip 8-th bit wrt message 1 - p. 198 Table 6.5
original_message2=np.array([int('0x00',16),int('0x23',16),int('0x45',16),int('0x67',16),int('0x89',16),int('0xab',16),int('0xcd',16),int('0xef',16),int('0xfe',16),int('0xdc',16),int('0xba',16),int('0x98',16),int('0x76',16),int('0x54',16),int('0x32',16),int('0x10',16)],dtype='int')
# original key 2: flip 8-th bit wrt key 1 - p. 199 Table 6.6
original_key2=np.array([int('0x0e',16),int('0x15',16),int('0x71',16),int('0xc9',16),int('0x47',16),int('0xd9',16),int('0xe8',16),int('0x59',16),int('0x0c',16),int('0xb7',16),int('0xad',16),int('0xd6',16),int('0xaf',16),int('0x7f',16),int('0x67',16),int('0x98',16)],dtype='int')
    
# Apply key expansion  to original key 1
rk1=transfo.ExpandKey(original_key1,ROUNDS)
    
# Apply key expansion  to original key 2
rk2=transfo.ExpandKey(original_key2,ROUNDS)

# count the number of errors among 128 key bits at each round
error=np.zeros((4,4),dtype='int')
for rd in range(ROUNDS+1):
    # compute error matrix for the current round rd in integer form
    error=rk1[rd,:,:]^rk2[rd,:,:]
    error_count=0
    for l in range(4):
        for c in range(4):
             error_count=error_count+bin(error[l,c]).count('1')
    # print error count
    print('Number of different key bit at round',rd,'=',error_count)
    
