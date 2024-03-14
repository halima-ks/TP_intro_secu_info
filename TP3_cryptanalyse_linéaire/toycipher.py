
from random import randint
import random

sbox = [9, 11, 12, 4, 10, 1, 2, 6, 13, 7, 3, 8, 15, 14, 0, 5]
xobs = [14, 5, 6, 10, 3, 15, 7, 9, 11, 0, 4, 1, 2, 8, 13, 12]
keys = [9, 3]


def enc(m, key):
    t = sbox[m ^ key[0]]
    c = sbox[t ^ key[1]]
    return c


def dec(c, key):
    t = xobs[c] ^ key[1]
    m = xobs[t] ^ key[0]
    return m


# Exercice 2.5 et 2.6

def gen_knownpair(n, k):
    return [(m, enc(m, k)) for m in [random.randint(0, 15) for x in range(n)]]


def brute_force(msg_chiffre):
    for k0 in range(0, 16):
        for k1 in range(0, 16):
            tmp = 0
            for (m, c) in msg_chiffre:
                if c != enc(m, (k0, k1)):
                    tmp = 1
                    break
            if tmp == 0:
                key = (k0, k1)
                print("\nLa clef a été touvé par force brute ! \t k = ", key)
    return key

# Exercice 3
def convertir_binaire(chiffre):
    x = 0
    for i in bin(chiffre):
        if(i == "1"):
            x += 1
    return x

# Fonction qui genere des masques
def generation_mask():
    mask = [[0 for i in range(16)] for j in range(16)]
    for i in range(1, 16):
        for j in range(1, 16):
            for m in range(1, 16):
                etp1 = m & j
                etp2 = sbox[m] & i
                # print("mask0: ", convertir_binaire(etp1), "\t\tmask1: ", convertir_binaire(etp2))
                if (convertir_binaire(etp1) % 2 == convertir_binaire(etp2) % 2):
                    mask[i][j] += 1
                    # print(mask[i][j])

    return mask


# fonction qui trouve les meilleurs scores et retourne la meilleure paire
def meilleur_sc_pr():

    liste_mask = generation_mask()
    maximum = 0
    max_bits1 = 0
    meilleur_sc = []
    meilleure_paire = []

    for i in range(16):
        for j in range(16):
            # On cherche la valeur maximale dans la liste des mask
            if(liste_mask[i][j] > maximum):
                maximum = liste_mask[i][j]
    # print("MAX: ",maximum)

    for i in range(16):
        for j in range(16):
            # On recupere tout les tuples avec le plus grand mask
            if(liste_mask[i][j] == maximum):
                meilleur_sc.append((i, j))

    for i in range(len(meilleur_sc)):
        tmp_mask = convertir_binaire(meilleur_sc[i][0]) + convertir_binaire(meilleur_sc[i][1])
        if(tmp_mask > max_bits1):
            max_bits1 = tmp_mask
            meilleure_paire = meilleur_sc[i]
    return meilleure_paire


# Exercice 4

# Fonction qui cherche les meilleurs k0
def meilleurs_k0():
    clair_chiffre = (())
    t = 0
    mask = []
    max = 0
    meilleur_k0 = []
    mask = meilleur_sc_pr()
    clair_chiffre = gen_knownpair(16, (9, 3))
    sc = [0 for _ in range(16)]

    for key0 in range(16):
        for mc in clair_chiffre:
            # chiffrer avec tout les k0
            t = sbox[enc(mc[0], (key0, 0)) & mask[0]] & mask[1]
            if (convertir_binaire(mc[1]) % 2 == convertir_binaire(t) % 2):
                sc[key0] += 1
            else:
                sc[key0] -= 1
    # On applique la valeur absolue sur chaque score
    sc = list(map(abs, sc))
    for i in range(len(sc)):
        if(sc[i] > max):
            max = sc[i]
    for i in range(len(sc)):
        if(sc[i] == max):
            meilleur_k0.append(i)
    # print("\nTableau de scores        => ", sc)
    return meilleur_k0

print(brute_force(gen_knownpair(16, keys)))

# Exercice 5:

def generation_msg(key):
    msg_chiffre = []
    for i in range(0, 16):
        msg_chiffre.append((i, enc(i, key))) 
    return msg_chiffre


def k1():
    liste_k1 = []
    msg_chiffre = generation_msg(keys)
    msg = random.randint(0, 15)
    m = msg_chiffre[msg][0]
    c = msg_chiffre[msg][1]
    for k0 in meilleurs_k0():
        print("1")
        t = sbox[m ^ k0]
        k1 = xobs[c] ^ t
        liste_k1.append(k1)
    # print("Les k1 correspondant     => ",liste_k1)
    return liste_k1

# print(k1())


def paire_k0_k1():
    K0 = meilleurs_k0()
    print("\nIndices des meilleurs k0 => ", K0, "\n")
    K1 = k1()
    print("Les k1 correspondant     => ",K1)
    paire = []
    for i in K0:
        for j in K1:
            paire.append((i, j))
    return paire
print("\npaire(k0, k1)            => ", paire_k0_k1(), "\n")
clefs = paire_k0_k1()



# test de clefs de 2 paires de clefs (k0, k1)
'''m = enc(15, (9, 6))
m1 = enc(15, (9, 2))
print("c: ", m)
print("m: ",dec(m, (9, 6)))
print("c: ", m1)
print("m: ",dec(m1, (9, 2)))'''




