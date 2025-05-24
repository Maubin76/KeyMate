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
        site = site_entry.get().strip()
        entry = get_password(site)
        if entry:
            id_value = entry.get("id", "")
            password_value = entry.get("password", "")
            result_label.config(text=f"Identifiant: {id_value}\nMot de passe: {password_value}")
            root.clipboard_clear()
            root.clipboard_append(password_value)
        else:
            result_label.config(text="Site non trouvé")

    def on_add():
        site = site_entry.get().strip()
        id_value = id_entry.get().strip()
        password_value = password_entry.get().strip()
        if site and password_value:
            add_password(site, id_value, password_value)
            result_label.config(text="Mot de passe ajouté/actualisé")
        else:
            result_label.config(text="Veuillez remplir le site et le mot de passe")

    tk.Button(root, text="Récupérer", command=on_get).pack()
    tk.Button(root, text="Ajouter/Mettre à jour", command=on_add).pack()

    root.mainloop()
