# algos/sujet_graphes.py

def trouver_plus_court_chemin(graphe: dict, depart: str, arrivee: str) -> list | None:
    """
    Trouve le plus court chemin entre deux nœuds dans un graphe non pondéré.

    Le graphe est représenté par une liste d'adjacence (un dictionnaire où chaque
    clé est un nœud et la valeur est une liste de ses voisins).

    La fonction doit utiliser l'algorithme de parcours en largeur (BFS - Breadth-First Search)
    pour trouver le chemin le plus court.

    Args:
        graphe: Le dictionnaire représentant le graphe.
        depart: Le nœud de départ.
        arrivee: Le nœud d'arrivée.

    Returns:
        Une liste de chaînes de caractères représentant le chemin du nœud de départ
        au nœud d'arrivée (inclus).
        Si aucun chemin n'existe, retourne None.
        Si départ et arrivée sont identiques, retourne [depart].
    
    Exemple:
    graphe = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    trouver_plus_court_chemin(graphe, 'A', 'F') devrait retourner ['A', 'C', 'F'] ou ['A', 'B', 'E', 'F']
    (le parcours en largeur garantit de trouver un des chemins les plus courts, ici de longueur 3).
    Pour cet exemple, le chemin via 'C' serait trouvé en premier : ['A', 'C', 'F'].
    """
    # Votre code ici
    return None