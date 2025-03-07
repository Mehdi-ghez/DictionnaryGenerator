import tkinter as tk
from tkinter import filedialog, messagebox
import time

# Fonction pour charger le dictionnaire selon le type choisi
def load_dictionary():
    global dictionary
    dictionary = []
    
    dict_file = filedialog.askopenfilename(title="Select a file", filetypes=[("Fichiers texte", "*.txt")])
    
    if not dict_file:
        messagebox.showwarning("Avertissement", "No selected file !")
        return

    with open(dict_file, "r", encoding="utf-8", errors="ignore") as file:
        dictionary = [line.strip() for line in file]

    messagebox.showinfo("Succès", f"Dictionnary Loaded successfuly {len(dictionary)} mots de passe.")

# Fonction pour tester le mot de passe en comparant mot à mot
def test_password():
    start_time = time.time()

    global dictionary
    if not dictionary:
        messagebox.showerror("Erreur", "Load a Dictionnary first.")
        return

    target_password = entry_password.get().strip()
    if not target_password:
        messagebox.showerror("Erreur", "Enter a word to test.")
        return

    ##test du temos de progression de la casse
    # time.sleep(1)

    found = False
    for word in dictionary:
        if word == target_password:
            found = True
            break

    end_time = time.time()

    if found:
        result_label.config(text=f"Password found {end_time - start_time:.6f} secondes.", fg="green")
    else:
        result_label.config(text="Password found.", fg="red")

# Création de l'interface Tkinter
root = tk.Tk()
root.title("Password security crack test")
root.geometry("500x300")

# Label et champ pour entrer un mot de passe
tk.Label(root, text="Enter a word to test:", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(root, width=30, font=("Arial", 12))
entry_password.pack(pady=5)

# Bouton pour charger un dictionnaire
btn_load = tk.Button(root, text="Load DIctionnary", command=load_dictionary, font=("Arial", 12))
btn_load.pack(pady=10)

# Bouton pour tester le mot de passe
btn_test = tk.Button(root, text="Crack Test", command=test_password, font=("Arial", 12))
btn_test.pack(pady=10)

# Label pour afficher le résultat
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Lancement de l'application
dictionary = []
root.mainloop()
