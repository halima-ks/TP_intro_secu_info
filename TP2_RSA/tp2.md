TP2 :

Exo 1 : 

1. La clef public c'est une clef que tout le monde peut voir alors que la clef secrète est privé il y a seulement les personnes qui echangent un message qui peuvent la voir // a qui appartient la clef qui peut la voir

2. On prend 1024 pour les clefs parce que tant que les valeurs sont grande la securité est eleve

3. Les conditions sont:

- Les deux nombres p et q ils faut que les deux nombres distincts
- Le e il faut qu'il soit inférieur a phi_n
- Il faut que e soit premier


4. Pour calculer le d faut calculer l'inverse modulaire 


Exo 2 :

1. a. la clef qu'il doit utiliser est la Ap
   b. la clef qu'il doit utiliser alice est As

2. On calcule le chiffré 𝑐 = 𝑚 ^ 𝑒 mod 𝑛

c -> est le message chiffré, e -> est l'exposant de chiffrement d'Alice et n -> est le module de chiffrement d'Alice

On retrouve le message en faisant 𝑚 = 𝑐^𝑑 mod 𝑛

m -> c'est le message en clair, d -> est l'exposant de dechiffrement d'alice et n est le module de chiffrement d'Alice


Exo 3 :

1. a. Bob doit utiliser sa clé privé (Bs) pour signer le message
   b. Alice doit utiliser la clé public (Bp) de Bob pour vérifier l’authenticité du message qui est signé par Bob

2. la procedure de signature a suivre est de chiffré un hash du message avec une clé privé a l'aide de l'algorithme RSA
Le message signé est de la forme d'un message chiffré 


Exo 4 :

1.  Il suffit de transformer un message chiffré en un autre message chiffré qui déchiffre en un message en clair associé.

2. Ce probleme est du à la lenteur des systemes à clef publique, on peut pas chiffres des grands messages avec ce systeme, car RSA sert à chiffrer des messages courts.
