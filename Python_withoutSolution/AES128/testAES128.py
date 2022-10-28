# -*- coding: utf-8 -*-
# Name of file: test.py
# import numpy package
import numpy as np
# import AES128 Encyption/Decryption module
import my_aes128_functions as aes128


################################################################################
# AES128 encryption/decryption of single blocs
################################################################################
# define number of rounds
ROUNDS=10
# define key as a vector of bytes in integer form

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
    

################################################################################
# Test the AES128 avalanche effect by modifying 1 message bit using the same key
################################################################################
# encryption
[cyphertext1,state1]=aes128.Encrypt(original_message1,original_key1,ROUNDS)
[cyphertext2,state2]=aes128.Encrypt(original_message2,original_key1,ROUNDS)

# count the number of errors among 128 key bits at each round
error=np.zeros((4,4),dtype='int')
for rd in range(ROUNDS+1):
    # compute error matrix for the current round rd in integer form
    error=state1[rd,:,:]^state2[rd,:,:]
    error_count=0
    for l in range(4):
        for c in range(4):
             error_count=error_count+bin(error[l,c]).count('1')
    # print error count
    print('Number of different key bit at round',rd,'=',error_count)
    
# decryption
[recovered_message1,state1]=aes128.Decrypt(cyphertext1,original_key1,ROUNDS)
[recovered_message2,state2]=aes128.Decrypt(cyphertext2,original_key1,ROUNDS)

# check correctness
sum=0
for i in range(original_message1.shape[0]):
    sum=sum+(original_message1[i]-recovered_message1[i])
if sum==0:
    print('encryption/decryption for original_message1 is correct!')
else:
    print('encryption/decryption for original_message1 is incorrect!')

sum=0
for i in range(original_message2.shape[0]):
    sum=sum+(original_message2[i]-recovered_message2[i])
if sum==0:
    print('encryption/decryption for original_message2 is correct!')
else:
    print('encryption/decryption for original_message2 is incorrect!')

################################################################################
# Test the AES128 avalanche effect by modifying 1 key bit using the same message
################################################################################
# encryption
[cyphertext1,state1]=aes128.Encrypt(original_message1,original_key1,ROUNDS)
[cyphertext1_prime,state2]=aes128.Encrypt(original_message1,original_key2,ROUNDS)

# count the number of errors among 128 key bits at each round
error=np.zeros((4,4),dtype='int')
for rd in range(ROUNDS+1):
    # compute error matrix for the current round rd in integer form
    error=state1[rd,:,:]^state2[rd,:,:]
    error_count=0
    for l in range(4):
        for c in range(4):
             error_count=error_count+bin(error[l,c]).count('1')
    # print error count
    print('Number of different key bit at round',rd,'=',error_count)
    
# decryption
[recovered_message1,state1]=aes128.Decrypt(cyphertext1,original_key1,ROUNDS)
[recovered_message1_prime,state2]=aes128.Decrypt(cyphertext1_prime,original_key2,ROUNDS)

# check correctness
sum=0
for i in range(original_message1.shape[0]):
    sum=sum+(original_message1[i]-recovered_message1[i])
if sum==0:
    print('encryption/decryption for original_message1 is correct!')
else:
    print('encryption/decryption for original_message1 is incorrect!')

sum=0
for i in range(original_message1.shape[0]):
    sum=sum+(original_message1[i]-recovered_message1_prime[i])
if sum==0:
    print('encryption/decryption for original_message1 is correct!')
else:
    print('encryption/decryption for original_message1 is incorrect!')
