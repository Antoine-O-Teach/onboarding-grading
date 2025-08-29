# algos/sujet_chaines.py

def valider_mot_de_passe(mot_de_passe: str) -> bool:
    """
    Valide un mot de passe selon des règles de sécurité précises.

    Un mot de passe est considéré comme valide s'il respecte TOUTES les règles suivantes :
    1. Avoir une longueur d'au moins 12 caractères.
    2. Contenir au moins une lettre minuscule (a-z).
    3. Contenir au moins une lettre majuscule (A-Z).
    4. Contenir au moins un chiffre (0-9).
    5. Contenir au moins un caractère spécial parmi : ! @ # $ % ^ & * ( ) _ +
    6. Ne pas contenir de séquence de plus de 3 caractères identiques (ex: "aaaa" est invalide).

    La fonction doit retourner True si le mot de passe est valide, False sinon.
    """
    # Votre code ici
    return True


def compresser_chaine(chaine: str) -> str:
    """
    Compresse une chaîne de caractères en utilisant l'algorithme "Run-Length Encoding".

    L'algorithme consiste à remplacer les séquences de caractères identiques
    par le nombre d'occurrences suivi du caractère.
    Par exemple, "AAABBCDDDD" devient "3A2B1C4D".

    La fonction ne doit compresser que si la chaîne résultante est plus courte
    que l'originale. Sinon, elle doit retourner la chaîne originale.

    Exemples :
    - "AAABBC" -> "3A2B1C" (plus court)
    - "ABC" -> "ABC" (la version compressée "1A1B1C" est plus longue)
    - "" -> "" (chaîne vide)
    """
    # Votre code ici
    return True