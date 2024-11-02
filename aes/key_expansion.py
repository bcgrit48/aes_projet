from aes.subbytes import SBOX

RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

def key_expansion(key):
    """
    Génère les sous-clés AES à partir de la clé principale AES-128.
    :param key: Clé principale (16 octets).
    :return: Clés étendues.
    """
    if len(key) != 16:
        raise ValueError("La clé doit être de 16 octets pour AES-128.")

    # Diviser la clé initiale en mots de 4 octets (4x4 = 16 octets)
    round_keys = [list(key[i:i + 4]) for i in range(0, len(key), 4)]

    # Générer les 40 mots supplémentaires pour AES-128 (44 mots au total)
    for i in range(4, 44):
        temp = round_keys[i - 1]
        if i % 4 == 0:
            # Rotation des octets (RotWord)
            temp = temp[1:] + temp[:1]
            # Vérifier et contraindre les valeurs à la plage 0-255
            temp = [b % 128 for b in temp]
            # Substitution des octets avec la S-box (SubWord)
            temp = [SBOX[b] for b in temp]
            # XOR avec RCON
            temp[0] ^= RCON[(i // 4) - 1]  # Vérification RCON

        # Ajouter le nouveau mot à la clé étendue
        round_keys.append([round_keys[i - 4][j] ^ temp[j] for j in range(4)])

    # Aplatir la liste des clés pour la retourner sous forme de liste d'octets
    return [byte for word in round_keys for byte in word]