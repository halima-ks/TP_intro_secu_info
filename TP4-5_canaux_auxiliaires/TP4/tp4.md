# TP4 EXO1

# 1. python3 -m seselab rsa.asm nous affiche : 

m = 42c0ffee93
N = 02c99a781f
s = 02306bf1b7


# 2. Que signifie "modexp"

"modexp" signifie exponentiation modulaire
L'algorithme utilisé par cette fonction est l'algorithme de l'exponentiation modulaire "Square and multiply" 


# 4. On voit que les activités electriques sont différentes. Il y a des creux vers 200 

# 5.

Calcul : 
convertir en decimal :
m = 42c0ffee93 = 286705839763
N = 02c99a781f = 11972278303
s = 02306bf1b7 = 9402315191

######################################################

Avec trace.png on va trouver d :
1 = grand 
0 = petit

Ce qui nous donne : 

111101000101010110110011000001 = 1024814273

pow(m, d, N)
pow(286705839763,1024814273,11972278303) = 9402315191 = 2306bf1b7
