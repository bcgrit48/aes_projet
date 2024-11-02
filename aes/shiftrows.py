def shift_rows(state):
    """
    Applique l'étape ShiftRows au bloc d'état.
    :param state: Matrice d'état (4x4) à transformer.
    :return: Matrice transformée.
    """
    state[1] = state[1][1:] + state[1][:1]  # Rotation d'un élément vers la gauche pour la 2ème ligne
    state[2] = state[2][2:] + state[2][:2]  # Rotation de deux éléments vers la gauche pour la 3ème ligne
    state[3] = state[3][3:] + state[3][:3]  # Rotation de trois éléments vers la gauche pour la 4ème ligne
    return state





























def inv_shift_rows(state):
    """
    Applique l'étape inverse ShiftRows au bloc d'état.
    :param state: Matrice d'état (4x4) à transformer.
    :return: Matrice transformée (déplacée dans le sens inverse).
    """
    state[1] = state[1][-1:] + state[1][:-1]  # Rotation d'un élément vers la droite pour la 2ème ligne
    state[2] = state[2][-2:] + state[2][:-2]  # Rotation de deux éléments vers la droite pour la 3ème ligne
    state[3] = state[3][-3:] + state[3][:-3]  # Rotation de trois éléments vers la droite pour la 4ème ligne
    return state
