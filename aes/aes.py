from aes.subbytes import SBOX
from aes.shiftrows import shift_rows
from aes.mixcolumns import mix_columns
from aes.addroundkey import add_round_key
from aes.key_expansion import key_expansion

from aes.subbytes import INV_SBOX
from aes.shiftrows import inv_shift_rows
from aes.mixcolumns import inv_mix_columns


def pkcs7_pad(data):
    """Ajoute un padding PKCS#7 pour que le texte ait une longueur multiple de 16 octets."""
    pad_len = 16 - (len(data) % 16)
    padding = bytes([pad_len] * pad_len)
    return data + padding

def pkcs7_unpad(data):
    """Retire le padding PKCS#7 après déchiffrement."""
    pad_len = data[-1]
    return data[:-pad_len]

def aes_encrypt(plain_text, key):
    """
    Chiffrement AES avec padding PKCS#7.
    :param plain_text: Texte à chiffrer (chaîne de caractères ou bytes).
    :param key: Clé de chiffrement (16 octets, bytes).
    :return: Texte chiffré en hexadécimal.
    """
    # Si le texte est une chaîne, le convertir en bytes
    if isinstance(plain_text, str):
        plain_text = plain_text.encode('ascii')

    # Appliquer le padding PKCS#7
    padded_text = pkcs7_pad(plain_text)

    # Diviser le texte en blocs de 16 octets
    blocks = [padded_text[i:i+16] for i in range(0, len(padded_text), 16)]

    round_keys = key_expansion(key)  # Expansion de la clé

    encrypted_blocks = []

    # Pour chaque bloc de 16 octets, appliquer l'algorithme AES
    for block in blocks:
        # Crée la matrice d'état (4x4) à partir du bloc de 16 octets
        state = [list(block[i:i + 4]) for i in range(0, 16, 4)]

        # Premier round
        state = add_round_key(state, round_keys[:16])

        # 9 rounds intermédiaires
        for round_num in range(1, 10):
            state = [[SBOX[byte] for byte in row] for row in state]  # SubBytes
            state = shift_rows(state)
            state = mix_columns(state)
            state = add_round_key(state, round_keys[round_num * 16:(round_num + 1) * 16])

        # Dernier round (sans mix_columns)
        state = [[SBOX[byte] for byte in row] for row in state]
        state = shift_rows(state)
        state = add_round_key(state, round_keys[160:176])

        # Transformer la matrice d'état en un tableau d'octets
        encrypted_bytes = [byte for row in state for byte in row]
        encrypted_blocks.append(encrypted_bytes)

    # Convertir les blocs chiffrés en hexadécimal
    encrypted_hex = ''.join(''.join(f'{byte:02x}' for byte in block) for block in encrypted_blocks)

    return encrypted_hex





















def aes_decrypt(cipher_text, key):
    """
    Déchiffrement AES avec padding PKCS#7.
    :param cipher_text: Texte chiffré en hexadécimal.
    :param key: Clé de chiffrement (16 octets, bytes).
    :return: Texte déchiffré (chaîne originale).
    """
    # Convertir le texte chiffré hexadécimal en liste d'octets
    cipher_bytes = [int(cipher_text[i:i + 2], 16) for i in range(0, len(cipher_text), 2)]

    # Crée la matrice d'état à partir du texte chiffré
    state = [list(cipher_bytes[i:i + 4]) for i in range(0, len(cipher_bytes), 4)]
    round_keys = key_expansion(key)

    state = add_round_key(state, round_keys[160:176])

    for round_num in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = [[INV_SBOX[byte] for byte in row] for row in state]  # InvSubBytes
        state = add_round_key(state, round_keys[round_num * 16:(round_num + 1) * 16])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)
    state = [[INV_SBOX[byte] for byte in row] for row in state]
    state = add_round_key(state, round_keys[:16])

    decrypted_bytes = [byte for row in state for byte in row]

    # Retirer le padding
    unpadded_text = pkcs7_unpad(bytes(decrypted_bytes))

    return unpadded_text.decode('ascii')  # Conversion en chaîne après déchiffrement et suppression du padding
