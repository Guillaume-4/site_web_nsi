import random
import math

#Definition de fonction

def encode_RSA(msg,e,n):
    global C
    C = pow(msg,e)
    C = math.fmod(C, n)
    return C

def decode_RSA(C,d,n):
    M = pow(C,d)
    M = math.fmod(M,n)
    return M

#Programme principal

p = 3
q = 7
msg = 11
n = p*q
phi = (p-1) * (q-1)
e = 5
k = 2
d = ((k*phi)+1)//e
cle_pub = (e,n)
cle_pv = (d,n)

print(cle_pub)
print(cle_pv)
print(encode_RSA(msg,e,n))
print(decode_RSA(C,d,n))