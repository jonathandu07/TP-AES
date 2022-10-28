# -*- coding: utf-8 -*-
# Name of file: my_gf_functions.py
# import constants shared across modules
import shared_constants as shared
# import numpy package
import numpy as np
# import F_256 Galois Field module
import my_gf_functions as gf

################################################################################
#
# Substitute byte tranformation (Sbox)
#
# inputs:
# - a: element of F_256 in integer form
#
# outputs:
# -res: element of F_256 in integer form after Sbox
#
################################################################################
def Sbox(a):
    # compute a^{-1} in F_256 (0^{-1}=0 in AES convention)
    a_inv=gf.inv(a)
    # convert a^{-1} to binary form (a7,a6,a5,a4,a3,a2,a1,a0)
    a_inv_bin=(a_inv & np.fliplr([2**np.arange(8)])[0] !=0).astype(int)
    # output of affine transformation in binary form
    res_bin=(np.matmul(shared.A_bin,a_inv_bin)+shared.b_bin)%2
    # convert back to integer form
    res=np.dot(res_bin,np.fliplr([2**np.arange(8)])[0])

    return res

################################################################################
#
# Inverse Substitute byte tranformation (InvSbox)
#
# inputs:
# - a: element of F_256 in integer form
#
# outputs:
# -res: element of F_256 in integer form after inverse Sbox 
#
################################################################################
def InvSbox(a):
    # convert ato binary form (a7,a6,a5,a4,a3,a2,a1,a0)
    a_bin=(a & np.fliplr([2**np.arange(8)])[0] !=0).astype(int)
    # output of inverse affine transformation in binary form
    res_bin=(np.matmul(shared.Ainv_bin,a_bin)+shared.binv_bin)%2
    # convert back to integer form
    res=np.dot(res_bin,np.fliplr([2**np.arange(8)])[0])
    # compute res^{-1} in F_256 (0^{-1}=0 in AES convention)
    res_inv=gf.inv(res)
    return res_inv

################################################################################
#
# Shift rows tranformation
#
# inputs:
# - state[0:3,0:3]: 4x4 matrix of element in F_256 in integer form
#
# outputs:
# -res[0:3,0:3]: 4x4 matrix of element in F_256 in integer form after Shift rows
#
################################################################################
def ShiftRows(state):
    transfo_state=np.zeros((4,4),dtype='int')
    
    for l in range(4):
        # circularly shift the l-th row by l steps to the left
        transfo_state[l,:]=np.roll(state[l,:],-l)

    return transfo_state

################################################################################
#
# Inverse Shift rows tranformation
# inputs:
# - state[0:3,0:3]: 4x4 matrix of element in F_256 in integer form
#
# outputs:
# -res[0:3,0:3]: 4x4 matrix of element in F_256 in integer form after Inverse Shift rows
#
################################################################################
def InvShiftRows(state):
    transfo_state=np.zeros((4,4),dtype='int')
    
    for l in range(4):
        # circularly shift the l-th row by l steps to the right
        transfo_state[l,:]=np.roll(state[l,:],l)

    return transfo_state

################################################################################
#
# Mix column tranformation
#
# inputs:
# - state[0:3,0:3]: 4x4 matrix of element in F_256 in integer form
#
# outputs:
# -res[0:3,0:3]: 4x4 matrix of element in F_256 in integer form after Mix column 
#
################################################################################
def MixColumn(state):
    transfo_state=np.zeros((4,4),dtype='int')
    
    for l in range(4):
        for c in range(4):
            # loop on the elements in the column
            for k in range(4):
                transfo_state[l,c]=\
                    """FILL IN MISSING CODE"""
    
    return transfo_state

################################################################################
#
# Inverse Mix column tranformation
#
# inputs:
# - state[0:3,0:3]: 4x4 matrix of element in F_256 in integer form
#
# outputs:
# -res[0:3,0:3]: 4x4 matrix of element in F_256 in integer form after Inverse Mix column 
#
################################################################################
def InvMixColumn(state):
    transfo_state=np.zeros((4,4),dtype='int')
    
    for l in range(4):
        for c in range(4):
            # loop on the elements in the column
            for k in range(4):
                transfo_state[l,c]=\
                    """FILL IN MISSING CODE"""
    
    return transfo_state

################################################################################
#
# Add round key
#
# inputs:
# - state[0:3,0:3]: 4x4 matrix of element in F_256 in integer form for the data
# - rk[0:3,0:3]: 4x4 matrix of element in F_256 in integer form for the round key
#
# outputs:
# -res[0:3,0:3]: 4x4 matrix of element in F_256 in integer form after Inverse Mix column 
#
################################################################################
def AddRoundKey(state,rk):
    # add in F_256 the elements of the 4x4 matrix
    return state^rk

################################################################################
#
# Key expansion algorithm: find the key for each round 0,1,..,ROUNDS
# VALID ONLY FOR KEYS OF LENGTH 128 bits
#
# inputs:
# - original_key[0:15]: original key (16 bytes) as a vector in integer form
# - ROUNDS: number of rounds
#
# outputs:
# -rk[0:ROUNDS,4,4]: key for each round as a 4x4 matrix of element in F_256 in integer form 
#
################################################################################
def ExpandKey(original_key,ROUNDS):
    # define array of words
    w=np.zeros((4,4*(ROUNDS+1)),dtype='int')
    # define an empty round key matrix
    rk=np.zeros((ROUNDS+1,4,4),dtype='int')

    # define round key constants
    RC=np.zeros(ROUNDS+1,dtype='int')
    # for round j=0,..,ROUNDS-1 RC[j]=x^{j}
    RC[1]=int('0x01',16)
    for rd in range(2,ROUNDS+1):
        RC[rd]=gf.xtime(RC[rd-1])

    # round 0: copy original key in array of words
    for c in range(4):
        for l in range(4):
            w[l,c]=original_key[4*c+l]
    
    # fill in the array of words
    tmp_word=np.zeros(4,dtype='int')
    
    for c in range(4,4*(ROUNDS+1)):
        # tmp_word depends is a function of previous word
        if c%4 == 0:
            # cyclically shift the previous word upwards
            tmp_word=np.roll(w[:,c-1],-1)
            
            # apply Sbox componentwise
            for l in range(4):
                tmp_word[l]=Sbox(tmp_word[l])
                
            # add round key constant RC[l/4] to the first component in F_256
            tmp_word[0]=gf.add(tmp_word[0],RC[int(c/4)])              
        else:
            # otherwise take the previous word tmp_word[:]=w[:,c-1]
            tmp_word=w[:,c-1]
            
        # next word w[:,c]=tmp_word+w[:,c-4] elementwise in F_256
        for l in range(4):
            w[l,c]=gf.add(tmp_word[l],w[l,c-4])

    # retrieve round key for each round
    for rd in range(ROUNDS+1):
        for l in range(4):
            for c in range(4):
                rk[rd,l,c]=w[l,4*rd+c]

    return rk
    
