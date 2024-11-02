import tkinter as tk
from tkinter import messagebox
from aes.aes import aes_encrypt  # Assurez-vous que aes_encrypt est importé

class AESApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AES Encryption")

        # Variables pour stocker les valeurs saisies
        self.input_text_var = ""
        self.key_input_var = ""
        self.result_var = ""

        # Création de l'interface de chiffrement
        self.create_encryption_widgets()

    def create_encryption_widgets(self):
        # Champ pour le texte
        self.input_label_enc = tk.Label(self.root, text="Texte à chiffrer :")
        self.input_label_enc.grid(row=0, column=0, padx=10, pady=10)
        self.input_text_enc = tk.Entry(self.root, width=50)
        self.input_text_enc.grid(row=0, column=1, padx=10, pady=10)

        # Champ pour la clé
        self.key_label_enc = tk.Label(self.root, text="Clé (16 caractères) :")
        self.key_label_enc.grid(row=1, column=0, padx=10, pady=10)
        self.key_input_enc = tk.Entry(self.root, width=50)
        self.key_input_enc.grid(row=1, column=1, padx=10, pady=10)

        # Bouton pour chiffrer
        self.encrypt_button = tk.Button(self.root, text="Chiffrer", command=self.encrypt_text)
        self.encrypt_button.grid(row=2, column=1, padx=10, pady=10)

        # Affichage du résultat chiffré
        self.result_label_enc = tk.Label(self.root, text="Résultat chiffré :")
        self.result_label_enc.grid(row=3, column=0, padx=10, pady=10)
        self.result_text_enc = tk.Text(self.root, height=5, width=50)
        self.result_text_enc.grid(row=3, column=1, padx=10, pady=10)

    def encrypt_text(self):
        try:
            # Récupérer le texte et la clé
            plain_text = self.input_text_enc.get().strip().encode('ascii')
            key = self.key_input_enc.get().strip().encode('ascii')

        except UnicodeEncodeError:
            messagebox.showerror("Error", "Le texte et la clé doivent contenir uniquement des caractères ASCII.")
            return

        if len(key) != 16:
            messagebox.showerror("Error", "La clé doit être exactement de 16 caractères.")
            return

        # Appel à la fonction de chiffrement AES
        encrypted = aes_encrypt(plain_text, key)

        # Suppression du contenu actuel du widget Text
        self.result_text_enc.delete('1.0', tk.END)

        # Insertion du texte chiffré
        self.result_text_enc.insert(tk.END, encrypted)

