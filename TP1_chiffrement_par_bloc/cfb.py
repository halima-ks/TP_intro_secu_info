import random

sbox = [9, 11, 12, 4, 10, 1, 2, 6, 13, 7, 3, 8, 15, 14, 0, 5]
xobs = [14, 5, 6, 10, 3, 15, 7, 9, 11, 0, 4, 1, 2, 8, 13, 12]
k = [9, 0]
def round(m, k):
    return sbox[m ^ k]

def back_round(c, k):
    return xobs[c] ^ k
def enc(m, k):
    t = round(m, k[0])
    c = round(t, k[1])
    return(c)

def dec(c, k):
    t = back_round(c, k[0])
    m = back_round(t, k[1])
    return m
    
def enc_byte(x, k):
    n0 = x & 0xf
    n1 = x >> 4
    en0 = enc(n0, k)
    en1 = enc(n1, k)
    return (en1 << 4) | en0

def dec_byte(x, k):
    n0 = x & 0xf
    n1 = x >> 4
    dn0 = dec(n0, k)
    dn1 = dec(n1, k )
    return (dn1 << 4) | dn0
    
def enc_file_cfb(path, key):
    src = open(path, "rb")
    dst = open(path +".enc", "wb")
    msg = src.read()
    src.close()
    iv = random.randint(0, 255)
    ciphertext = [iv]
    prev = iv
    for b in msg:
        c = enc_byte(prev, key) ^ b
        ciphertext.append(c)
        prev = c
    dst.write(bytes(ciphertext))
    dst.close()
    print(ciphertext)

def dec_file_cfb(path, key):
    src = open(path, "rb")
    dst = open(path +".dec", "wb")
    ctxt = src.read()
    src.close()
    
    iv = ctxt[0]
    cleartxt = []
    prev = iv
    for b in ctxt[1:]:
        p_c = enc_byte(prev, key)
        c = p_c ^ b 
        cleartxt.append(c)
        prev = b
    dst.write(bytes(cleartxt))
    dst.close()
    print(cleartxt)

#enc_file_cfb("image.jpg", k)
#dec_file_cfb("image.jpg.enc", k)


enc_file_cfb("test.txt", k)
dec_file_cfb("test.txt.enc", k)

