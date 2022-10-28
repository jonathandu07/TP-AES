# -*- coding: utf-8 -*-
# Name of file: my_gf_functions.py
# import constants shared across modules
import shared_constants as shared
# import numpy package
import numpy as np

#####################################################################
#
#  Multiply by x Galois Field F_256 using m(x)=x^8+x^4x^3+x+1
#
#  inputs:
#  - b: element of F_256 in integer form
#
#  outputs:
#  - res: b*x in F_256 in integer form
#
####################################################################
def xtime(b):
   # consider b in binary form b=(b7,b6,b5,b4,b3,b2,b1,b0)
   # check whether b7 is non-zero
   mask=1<<7
   b7=b&mask

   if b7 == 0:
      # b*x=(b6,b5,b4,b3,b2,b1,b0,0)
      res=(b<<1)&int('0xff',16)
   else:
      # b*x=(b6,b5,b4,b3,b2,b1,b0,0)+(0,0,0,1,1,0,1,1) mod 2
      res=((b<<1)&int('0xff',16))^int('0x1b',16)
      
   return res 
   

#####################################################################
#
#  Addition in the Galois Field F_256 using m(x)=x^8+x^4x^3+x+1
#
#  inputs:
#  - a: element of F_256 in integer form
#  - b: element of F_256 in integer form
#
#  outputs:
#  - res: a+b in F_256 in integer form
#
####################################################################
def add(a,b):
   # return bitxor of a and b
   res=a^b
   
   return res

#####################################################################
#
#  Slow Multiplication in the Galois Field F_256 using m(x)=x^8+x^4x^3+x+1
#  Using applications of xtime() 
#
#  inputs:
#  - a: element of F_256 in integer form
#  - b: element of F_256 in integer form
#
#  outputs:
#  - res: a*b in F_256 in integer form
#
####################################################################
def mul_xtime(a,b):
   # consider b in binary form b=(b7,b6,b5,b4,b3,b2,b1,b0)
   # a*b in F_256 = b0*a*x^0+b1*a*x^1+b2*a*x^2+b3*a*x^3+...+b7*a*x^7

   # initialize result
   res=0
   # initialize tmp = a
   tmp=a
   # find b0 by masking the 0-th binary digit of b
   mask=1<<0
   b0=b&mask
   # accumulate b0*ax^0
   if b0 != 0:
      res=res^tmp
      
   for i in range(1,8):
      # update tmp = a*x^i
      tmp=xtime(tmp)
      # find bi by masking the i-th binary digit of b
      mask=1<<i
      bi=b&mask
      # accumulate bi*ax^i
      if bi != 0:
         res=res^tmp
      
   return res

#####################################################################
#
#  Fast Multiplication in the Galois Field F_256 using m(x)=x^8+x^4x^3+x+1
#  Using applications of Logtable() and Alogtable()
#
#  inputs:
#  - a: element of F_256 in integer form
#  - b: element of F_256 in integer form
#
#  outputs:
#  - res: a*b in F_256 in integer form
#
####################################################################
def mul(a,b):
   """FILL IN MISSING CODE"""

   return res

#####################################################################
#
#  Fast Inverse in the Galois Field F_256 using m(x)=x^8+x^4x^3+x+1
#  Using applications of Logtable() and Alogtable()
#
#  inputs:
#  - a: element of F_256 in integer form
#
#  outputs:
#  - res: a^{-1} in F_256 in integer form         
#
####################################################################
def inv(a):
   # 0^{-1}=0 by convention in AES
   if a==0:
      return 0
   else:
      return """FILL IN MISSING CODE"""

#####################################################################
#
#  Fast Division in the Galois Field F_256 using m(x)=x^8+x^4x^3+x+1
#  Using applications of Logtable() and Alogtable()
#
#  inputs:
#  - a: element of F_256 in integer form
#  - b: element of F_256 in integer form
#
#  outputs:
#  - res: a/b in F_256 in integer form         
#
####################################################################
def div(a,b):
   return """FILL IN MISSING CODE"""
