import hashlib
from itertools import product

lettre_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']

lettre_maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caract_spe = ['&', '#', '@', '$', '%', '.', '?', '!']

hash_a_trouver = "6124f24c9b905bb9a9b27441dfba88c00f8e2368baf86aa366a818514c282a2a"

longueur_combinaison = 3

combinaisons = product(lettre_min + lettre_maj + chiffre + caract_spe, repeat=longueur_combinaison)

for tentative in combinaisons:
    mot_essai = ''.join(tentative)
    sha256_essai = hashlib.sha256(mot_essai.encode()).hexdigest()

    if sha256_essai == hash_a_trouver:
        print(f"Mot de passe trouvé : {mot_essai}")
        break
