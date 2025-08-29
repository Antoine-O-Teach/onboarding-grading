# tests/test_chaines.py

from algos.sujet_chaines import valider_mot_de_passe, compresser_chaine

# --- Tests pour valider_mot_de_passe ---

def test_mdp_valide_cas_nominal():
    """Teste un mot de passe qui respecte toutes les règles."""
    pass

def test_mdp_trop_court():
    """Teste un mot de passe qui ne respecte pas la longueur minimale."""
    pass

def test_mdp_sans_majuscule():
    """Teste un mot de passe sans lettre majuscule."""
    pass

def test_mdp_sans_chiffre():
    """Teste un mot de passe sans chiffre."""
    pass

def test_mdp_sans_caractere_special():
    """Teste un mot de passe sans caractère spécial."""
    pass

def test_mdp_avec_sequence_trop_longue():
    """Teste un mot de passe avec une séquence de caractères identiques invalide."""
    pass

# --- Tests pour compresser_chaine ---

def test_compression_cas_general():
    """Teste une chaîne avec plusieurs séquences à compresser."""
    pass

def test_compression_non_rentable():
    """Teste une chaîne où la compression résulterait en une chaîne plus longue."""
    pass

def test_compression_chaine_vide():
    """Teste le comportement avec une chaîne vide."""
    pass

def test_compression_avec_un_seul_caractere():
    """Teste une chaîne composée d'un seul type de caractère (ex: "BBBBBB")."""
    pass