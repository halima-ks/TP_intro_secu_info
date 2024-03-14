
# Exercie 2: 
1. 
sans faute : s = 3f010be37eb5eca9
Avec faute : sf = e2e0f76e2d5e496d (faute injecté sur le registre)

2. 
N = 47775493107113604137
Pour retouver la valeur de p ou q on doit calculer le pgcd(N,s - sf)
pgcd(47775493107113604137, 4539922971077504169 - 40719886873676685005) = p
p = 8548494751

La valeur de q on la deduit de la relation p * q = N <=> q = N / p
q = 5588760887

On a besoin maintenant de trouver la valeur de Phi = (p - 1)* (q - 1)
Phi = 47775493092976348500

Calculant l'inverse pour retouvé la clef privé d :
d = inverse(e, phi) 
d = 22482584984930046353
Pour verifier si on a obtenu la bonne clef, o, doit chiffer et dechiffrer un message  
Chiffrer : pow (message, e, N)
pow (532, 17, 47775493107113604137) = 19664836895107349454

Dechiffrer :  pow (chiffré, d, N)
pow (19664836895107349454, 22482584984930046353, 47775493107113604137) = 532
On a obtenu la bonne clef d
