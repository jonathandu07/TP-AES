# -*- coding: utf-8 -*-
# Name of file: my_aes128_functions.py
# import constants shared across modules
import shared_constants as shared
# import numpy package
import numpy as np
# import F_256 Galois Field module
import my_gf_functions as gf
# import AES transformations module
import my_transformations_functions as transfo

################################################################################
#
# AES128 Encryption of one length-128 bits block
#
# inputs:
# - plaintext[0:15]: plaintext as a vector of 16 bytes in integer form
# - key[0:15]: key as a vector of 16 bytes in integer form
# - ROUNDS: number of rounds
#
# outputs:
# - cyphertext[0:15]: cyphertext as a vector of 16 bytes in integer form
# - state[0:ROUNDS,4,4]: state for each round as a 4x4 matrix of element in F_256 in integer form 
#
################################################################################
def Encrypt(plaintext,key,ROUNDS):
    # retrieve plaintext length in bytes
    PLAINTEXT_LENGTH = plaintext.shape[0]
    # retrieve key length in bytes
    KEY_LENGTH = key.shape[0]

    # define an empty state matrix at each round
    state=np.zeros((ROUNDS+1,4,4),dtype='int')
    # define an empty cyphertext vector
    cyphertext=np.zeros(PLAINTEXT_LENGTH,dtype='int')
    
    # Apply key expansion to the original key
    # (rk[rd:,:,:] is the round key at round rd as a 4x4 matrix in integer form)
    rk=transfo.ExpandKey(key,ROUNDS)

    # INIT STATE: transform plaintext to 4x4 matrix of element in F_256 in integer form
    rd=0
    for c in range(4):
        for l in range(4):
            state[rd,l,c]=plaintext[4*c+l]

    # APPLY ROUND#0: only add rk[0:,:,:]
    state[rd,:,:]=transfo.AddRoundKey(state[rd,:,:],rk[rd,:,:])

    # APPLY ROUND#1 TO #ROUNDS-1:
    for rd in range(1,ROUNDS):
        # copy state at previous round
        state[rd,:,:]=state[rd-1,:,:]
        # Byte Substitution transformation
        for l in range(4):
            for c in range(4):
                state[rd,l,c]=transfo.Sbox(state[rd,l,c])
        # Shift Rows transformation
        state[rd,:,:]=transfo.ShiftRows(state[rd,:,:])
        # Mix Columns transformation
        state[rd,:,:]=transfo.MixColumn(state[rd,:,:])
        # Add current round key
        state[rd,:,:]=transfo.AddRoundKey(state[rd,:,:],rk[rd,:,:])

    # APPLY LAST ROUND (same but without Mix Columns transformation)
    """FILL IN MISSING CODE"""

    # REFORMAT 4x4 final state matrix to cyphertext in vector form
    for c in range(4):
        for l in range(4):
            cyphertext[4*c+l]=state[ROUNDS,l,c]

    return cyphertext,state


################################################################################
#
# AES128 Decryption of one length-128 bits block
#
# inputs:
# - cyphertext[0:15]: plaintext as a vector of 16 bytes in integer form
# - key[0:15]: key as a vector of 16 bytes in integer form
# - ROUNDS: number of rounds
#
# outputs:
# - plaintext[0:15]: cyphertext as a vector of 16 bytes in integer form
# - state[0:ROUNDS,4,4]: state for each round as a 4x4 matrix of element in F_256 in integer form 
#
################################################################################
def Decrypt(cyphertext,key,ROUNDS):
    # retrieve plaintext length in bytes
    PLAINTEXT_LENGTH = cyphertext.shape[0]
    # retrieve key length in bytes
    KEY_LENGTH = key.shape[0]

    # define an empty state matrix at each round
    state=np.zeros((ROUNDS+1,4,4),dtype='int')
    # define an empty plaintext vector
    plaintext=np.zeros(PLAINTEXT_LENGTH,dtype='int')
    
    # Apply key expansion to the original key
    # (rk[rd:,:,:] is the round key at round rd as a 4x4 matrix in integer form)
    rk=transfo.ExpandKey(key,ROUNDS)
    
    # INIT STATE: transform cyphertext to 4x4 matrix of element in F_256 in integer form
    rd=ROUNDS
    for c in range(4):
        for l in range(4):
            state[rd,l,c]=cyphertext[4*c+l]

    # INVERT LAST ROUND (without Inverse Mix Columns transformation)
     #"""FILL IN MISSING CODE"""

    # INVERT #ROUNDS-1 TO ROUND#1:
    for rd in range(ROUNDS-1,0,-1):
        # copy state at next round
        state[rd,:,:]=state[rd+1,:,:]
        # Remove current round key (AddRoundKey is equal to its inverse)
        state[rd,:,:]=transfo.AddRoundKey(state[rd,:,:],rk[rd,:,:])
        # Mix Columns Inverse transformation
        state[rd,:,:]=transfo.InvMixColumn(state[rd,:,:])
        # Shift Rows Inverse transformation
        state[rd,:,:]=transfo.InvShiftRows(state[rd,:,:])
        # Byte Substitution Inverse transformation
        for l in range(4):
            for c in range(4):
                state[rd,l,c]=transfo.InvSbox(state[rd,l,c])
        
    # INVERT ROUND#0: only add rk[0:,:,:] (AddRoundKey is equal to its inverse)
    # copy state at next round
    rd=0
    state[rd,:,:]=state[rd+1,:,:]
    # remove current round key (AddRoundKey is equal to its inverse)
    state[rd,:,:]=transfo.AddRoundKey(state[rd,:,:],rk[rd,:,:])
    
    # REFORMAT 4x4 final state matrix to cyphertext in vector form
    for c in range(4):
        for l in range(4):
            plaintext[4*c+l]=state[0,l,c]

    return plaintext,state
