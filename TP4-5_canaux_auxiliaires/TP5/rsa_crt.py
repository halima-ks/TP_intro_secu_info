from Crypto.Util.number import getPrime, inverse
import hashlib
import time
from math import gcd 

p = getPrime(512 // 2)
q = getPrime(512 // 2)
assert (p != q)
if (gcd(p,q) == 1):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    if gcd(phi_n, e) == 1:
        d = inverse(e, phi_n)

def gen_rsa_keypair():
    return ((e, n), (d, n))

def gen_rsa_keypair_crt():
    dp = d % (p - 1)
    dq = d % (q - 1)
    iq = inverse(q, p)
    return ((e, n), (p, q, dp, dq, iq))

Ap, As = gen_rsa_keypair()
Bp, (Bpp, Bq, dp, dq, iq) = gen_rsa_keypair_crt()
message = 513


def RSA(m, key):
    return pow(m, key[0], key[1])

# fonction de signature avec rsa 
def signature_rsa(m, Ks):
    t0 = time.time()
    for i in range(1000):
        s = RSA(m, Ks)
        t1 = time.time()
    t2 = t1 - t0
    print("time_rsa : ", t2)
    return s

# fonction de signature avec rsa crt
def signature_rsa_crt(m, p, q, dp, dq, iq):
    t0 = time.time()
    for i in range(1000):
        sp = pow(m, dp, p)
        sq = pow(m, dq, q)
        s = sq + q * (iq * (sp - sq) % p)
        t1 = time.time()
    t2 = t1 - t0
    print("time_rsa_crt: ", t2)
    return s

print(signature_rsa(message, As))
print(signature_rsa_crt(message, Bpp, Bq, dp, dq, iq))


# Rsa crt va 3 plus vite que rsa  