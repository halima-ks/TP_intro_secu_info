TP3 : Introduction à la sécurité 

exo 1 : 

2. Ce cryptosysteme appartient à la famille symétrique des chiffrements par bloc   

3. Le Type de cryptosysteme utilisé est RSP (reseau de substitution et permutation)

4. a. La taille du bloc est de 4 bits 
   b. La taille de la clef est 8 bits
   c. Il y a 2 tours 
   d. Le premier tour se fait entre le xor et le m et la clef et le 2ème c'est une subtitutuion entre t et k1 
   e. L'étape de substitution consiste à remplacé le valeur du Xor d'une clef et un d'un texte clair par une valeur comprise entre 0 et 16. 
   f. Il n'y a pas de permutation il y a juste subtitution, son nom est l'identité

exo 2 :
1. a. Le type d'attaque est l'attaque KPA (Attaque à texte clair connu)
   b. C'est une attaque chiffré clair connu : l'attaquant possède à la fois le texte chiffré (cipher) et un texte clair
   on fait le xor 
   voici le calcul à faire :

   c' = t ^ k1
   t' = m ^ k0
   t = sbox[t']

2. Il ne suffit pas de repeter deux fois l'operation de la question precedente car le message est chiffré deux fois et les clefs ne sont pas connues.

3.  a. Il y'a 16 clefs.
    b. Il n'est pas possible de toutes les tester car on ne connait pas les t, on a donc aucun moyen de les tester .

4. 256 etapes sont necessaires pour attaquer ToyCipher par force brute car on va chiffrer chaque messages avec k0 pour le premier tour qui prend une valeur de 0 à 15 et avec k1 pour le deuxieme tour qui prend egalement une valeur de 0 à 15 ce qui fait en tout 256 etapes d'executions.

Exo 3 

1. la conception de notre cryptosystème notre fonction de tour n’est pas linéaire car les entrées dans la boite S ne sont pas toutes paires.

5.  b. Avec l'attaque par force brute on obtient la clef de chiffrement.


Exo 6:

1. Le nombre d'etapes necessaires pour une attaque par force brute est de 4096 etapes (16 * 16 * 16)
   Le nombre d'etapes necessaires pour une attaque parcryptanalyse linéaire est :
   - Etape generation des masques : 4096 etapes(16 * 16 * 16)
   - Etape meilleurs K0           : 256 etapes(16 * 16)

2. Le nombre d'etapes necessaires pour une attaque par force brute est de 4096 etapes (16 * 16 * 16)
L'attaque par force brute prends bouceaup plus de temps que l'attaque par cryptanalyse lineaire.

3. Je pense que oui car l’approximation lineaire de la boite S est trés couteuse en terme de calcule.





