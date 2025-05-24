import customtkinter as ctk
from storage import get_password, add_password
from config import MASTER_PASSWORD


def authenticate():
    auth_window = ctk.CTk()
    auth_window.title("KeyMate - Authentification")
    auth_window.geometry(setup_window(auth_window))
    
    ctk.CTkLabel(auth_window, text="Entrez le Master Password:").pack(pady=10)
    password_entry = ctk.CTkEntry(auth_window, show="*")
    password_entry.pack(pady=5)
    
    result_label = ctk.CTkLabel(auth_window, text="")
    result_label.pack(pady=5)
    
    def verify():
        entered = password_entry.get()
        if entered == MASTER_PASSWORD:
            auth_window.destroy()
            launch_ui()  # Lancement de l'interface principale
        else:
            result_label.configure(text="Mot de passe incorrect", text_color="red")
    
    ctk.CTkButton(auth_window, text="Valider", command=verify).pack(pady=5)
    auth_window.mainloop()

def launch_ui():
    ctk.set_appearance_mode("System")  # Modes: "System" (auto), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Autres thèmes : "green", "dark-blue"

    root = ctk.CTk()
    root.title("KeyMate")
    
    # Positionnement de la fenêtre
    root.geometry(setup_window(root))

    # Entrées
    site_entry = ctk.CTkEntry(root, placeholder_text="Site")
    site_entry.pack(pady=10)

    id_entry = ctk.CTkEntry(root, placeholder_text="Identifiant")
    id_entry.pack(pady=10)

    password_entry = ctk.CTkEntry(root, placeholder_text="Mot de passe", show="*")
    password_entry.pack(pady=10)

    result_label = ctk.CTkLabel(root, text="")
    result_label.pack(pady=10)

    def on_get():
        site = site_entry.get().strip()
        entry = get_password(site)
        if entry:
            id_value = entry.get("id", "")
            password_value = entry.get("password", "")
            result_label.configure(text=f"Identifiant: {id_value}\nMot de passe: {password_value}")
            root.clipboard_clear()
            root.clipboard_append(password_value)
        else:
            result_label.configure(text="Site non trouvé")

    def on_add():
        site = site_entry.get().strip()
        id_value = id_entry.get().strip()
        password_value = password_entry.get().strip()
        if site and password_value:
            add_password(site, id_value, password_value)
            result_label.configure(text="Mot de passe ajouté/actualisé")
        else:
            result_label.configure(text="Veuillez remplir le site et le mot de passe")

    ctk.CTkButton(root, text="Récupérer", command=on_get).pack(pady=5)
    ctk.CTkButton(root, text="Ajouter/Mettre à jour", command=on_add).pack(pady=5)

    root.mainloop()

def setup_window(root: ctk) -> str:
    window_width, window_height = 250, 300

    # Dimensions de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Hauteur de la barre des tâches (approximatif)
    taskbar_height = 80
    
    x = -8  # Collé à gauche
    y = screen_height - window_height - taskbar_height  # Collé en bas en comptant la barre
    return f"{window_width}x{window_height}+{x}+{y}"