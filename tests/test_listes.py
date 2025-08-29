from algos.sujet_listes import trouver_max, trier_bulles

# --- Tests pour trouver_max ---
def test_trouver_max_simple():
    assert trouver_max([1, 5, 2, 9, 3]) == 9

def test_trouver_max_vide():
    assert trouver_max([]) is None

# --- Tests pour trier_bulles ---
def test_trier_bulles_cas_general():
    assert trier_bulles([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]

def test_trier_bulles_deja_trie():
    assert trier_bulles([1, 2, 3]) == [1, 2, 3]