def mix_columns(state):
    """
    Applique l'étape MixColumns au bloc d'état.
    :param state: Matrice d'état (4x4).
    :return: Matrice transformée.
    """
    for i in range(4):
        a = state[i]
        state[i] = [
            a[0] ^ a[1] ^ a[2] ^ a[3],
            a[0] ^ a[1] ^ a[2] ^ a[3],
            a[0] ^ a[1] ^ a[2] ^ a[3],
            a[0] ^ a[1] ^ a[2] ^ a[3]
        ]
    return state






















def inv_mix_columns(state):
    """
    Applique l'étape inverse MixColumns au bloc d'état.
    :param state: Matrice d'état (4x4) à transformer.
    :return: Matrice transformée.
    """
    for i in range(4):
        a = state[i]
        # Même logique, car XOR est symétrique (A ^ B ^ B = A)
        state[i] = [
            a[0] ^ a[1] ^ a[2] ^ a[3],
            a[0] ^ a[1] ^ a[2] ^ a[3],
            a[0] ^ a[1] ^ a[2] ^ a[3],
            a[0] ^ a[1] ^ a[2] ^ a[3]
        ]
    return state


