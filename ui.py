import tkinter as tk
from storage import get_password, add_password

def launch_ui():
    root = tk.Tk()
    root.title("KeyMate")

    # Entrée pour le nom du site
    tk.Label(root, text="Site:").pack()
    site_entry = tk.Entry(root)
    site_entry.pack()

    # Entrée pour l'identifiant
    tk.Label(root, text="Identifiant:").pack()
    id_entry = tk.Entry(root)
    id_entry.pack()

    # Entrée pour le mot de passe
    tk.Label(root, text="Mot de passe:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Zone d'affichage
    result_label = tk.Label(root, text="")
    result_label.pack()

    def on_get():
        site = site_entry.get()
        id = id_entry.get()
        password = get_password(site)
        if password:
            result_label.config(text=f"Mot de passe: {password}")
            root.clipboard_clear()
            root.clipboard_append(password)
        else:
            result_label.config(text="Site non trouvé")

    def on_add():
        site = site_entry.get()
        password = password_entry.get()
        add_password(site, password)
        result_label.config(text="Mot de passe ajouté")

    tk.Button(root, text="Récupérer", command=on_get).pack()
    tk.Button(root, text="Ajouter", command=on_add).pack()

    root.mainloop()
