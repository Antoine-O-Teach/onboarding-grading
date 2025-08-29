def trouver_max(elements: list[int]) -> int | None:
    """
    Cette fonction doit retourner le plus grand entier d'une liste.
    Si la liste est vide, elle doit retourner None.
    """
    # On traite d'abord le cas d'une liste vide, comme demandé.
    if not elements:
        return None
    
    # La fonction intégrée max() de Python est la manière la plus simple
    # et la plus efficace de trouver le plus grand élément.
    return max(elements)

def trier_bulles(elements: list[int]) -> list[int]:
    """
    Cette fonction doit trier la liste en utilisant l'algorithme du tri à bulles.
    Elle retourne une nouvelle liste triée.
    """
    # On crée une copie de la liste pour ne pas modifier l'originale,
    # respectant ainsi la consigne "retourne une nouvelle liste".
    nombres = elements.copy()
    n = len(nombres)

    # L'algorithme du tri à bulles compare les paires d'éléments adjacents
    # et les échange s'ils sont dans le mauvais ordre.
    
    # La boucle externe parcourt toute la liste.
    for i in range(n):
        # La boucle interne "fait remonter" le plus grand élément de la partie non triée.
        # Le "-i-1" est une optimisation car après 'i' passages, les 'i' plus grands 
        # éléments sont déjà à la fin de la liste, à leur place.
        for j in range(0, n - i - 1):
            # Si l'élément trouvé est plus grand que l'élément suivant, on les échange.
            if nombres[j] > nombres[j + 1]:
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                
    return nombres