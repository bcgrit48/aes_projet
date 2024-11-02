def add_round_key(state, round_key):
    """
    Applique la clé de round à la matrice d'état.
    :param state: Matrice d'état (4x4).
    :param round_key: Sous-clé de round (16 octets).
    :return: Matrice transformée.
    """
    # Debug: Afficher la taille de state et round_key
    print(f"State size: {len(state)}x{len(state[0]) if state else 0}")
    print(f"Round key size: {len(round_key)}")

    # Vérifier que state est 4x4 et round_key est de 16 octets
    if len(state) != 4 or any(len(row) != 4 for row in state):
        raise ValueError("State matrix must be 4x4.")
    if len(round_key) != 16:
        raise ValueError("Round key must be 16 bytes.")

    # Appliquer la clé de round
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i * 4 + j]

    return state
