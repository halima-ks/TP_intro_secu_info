# TP1

# Exercice 3 :
1. Je remarque que le contenu dans le "test.txt" il est transformé en une version chiffrée du texte à l'aide de la clef (9,0), le texte est illisible mais c'est exactement la meme chose pour les deux coucou. La sécurité est limité.

2. La clef est de seulement 8 bits (256 posibilités) donc une attaque par force brute peut etre réaliser. L'attaquant pourrait essayer toutes les combinaisons de clefs possibles avant de trouver la clef qui va dechiffrer le texte chiffré.

3. En utilisant des modes d'operations avec l'utilisation d'un vecteur d'initialisation ça ameliore directement la sécurité car ça evite  que les memes blocs de texte soient chiffrés de la même manière donc les sorties sont différentes.


executez test.py puis cfb.py 
test.ex3_q1.enc -> premier test sans le mode operation 
test.txt.enc -> avec le mode operation