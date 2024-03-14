# TP2 RSA 
from Crypto.Util.number import getPrime, inverse
import hashlib
from math import gcd


def gen_rsa_keypair(bits):
    p = getPrime(bits // 2)
    q = getPrime(bits // 2)
    assert (p != q)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    if gcd(phi_n, e) == 1:
        d = inverse(e, phi_n)
    return ((e, n), (d, n))


# Clef public et secrete d'Alice et Bob
Ap, As = gen_rsa_keypair(1024)
Bp, Bs = gen_rsa_keypair(1024)


def rsa(m, key):
    return pow(m, key[0], key[1])


def convertir_en_int(msg):
    entier = int.from_bytes(msg.encode('utf-8'), 'big')
    return entier


def convertir_en_str(entier):
    msg = entier.to_bytes((entier.bit_length() + 7) //
                          8, 'big').decode('utf-8')
    return msg

# Fonction de chiffrement avec rsa
def rsa_enc(msg, key):
    m = convertir_en_int(msg)
    c = rsa(m, key)
    return c

# Fonction de dechiffrement avec rsa
def rsa_dec(c, key):
    m = rsa(c, key)
    msg = convertir_en_str(m)
    return msg

#Hachage
def h(msg):
	hs = hashlib.sha256(b"msg").digest()
	return int.from_bytes(hs, 'big')

 
def rsa_sign(m, Ks):
	s = rsa(h(m), Ks)
	return s


def rsa_verify(m,sign, Kp):
	vf = rsa(sign, Kp)
	if(h(m) ==  vf):
		print("->Message authentique<-\n")
	else:
		print("->Message pas authentique<-\n")

msg_alice = "Salut Bob"
msg_bob = "Salut Alice"


print("--Alice--\n")
rsa_enc(msg_alice , Bp)
print(rsa_dec(rsa_enc(msg_alice , Bp), Bs))
rsa_verify(msg_alice ,rsa_sign(msg_alice , As), Ap)

print("-------------------------------\n")
print("--Bob--\n")
rsa_enc(msg_bob, Ap)
print(rsa_dec(rsa_enc(msg_bob, Ap), As))
rsa_verify(msg_bob,rsa_sign(msg_bob, Bs), Bp)
