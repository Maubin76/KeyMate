import customtkinter as ctk
from storage import get_all_passwords, update_password, delete_password

def on_show_all():
    all_passwords = get_all_passwords()

    list_window = ctk.CTkToplevel()
    list_window.title("Tous les mots de passe")
    list_window.geometry("500x500")

    ctk.CTkLabel(list_window, text="Liste des mots de passe enregistrés", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

    table_frame = ctk.CTkFrame(list_window)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    headers = ["Site", "Identifiant", "Mot de passe", "Actions"]
    for i, header in enumerate(headers):
        header_label = ctk.CTkLabel(table_frame, text=header, font=ctk.CTkFont(weight="bold"))
        header_label.grid(row=0, column=i, padx=10, pady=5, sticky="w")

    if not all_passwords:
        empty_label = ctk.CTkLabel(table_frame, text="Aucun mot de passe enregistré.")
        empty_label.grid(row=1, column=0, columnspan=4, pady=10)
    else:
        for row_index, entry in enumerate(all_passwords, start=1):
            site = entry["site"]
            identifiant = entry["id"]
            password = entry["password"]

            ctk.CTkLabel(table_frame, text=site).grid(row=row_index, column=0, padx=10, pady=3, sticky="w")
            ctk.CTkLabel(table_frame, text=identifiant).grid(row=row_index, column=1, padx=10, pady=3, sticky="w")
            ctk.CTkLabel(table_frame, text=password).grid(row=row_index, column=2, padx=10, pady=3, sticky="w")

            # --- ACTION BUTTONS ---
            action_frame = ctk.CTkFrame(table_frame, fg_color="transparent")
            action_frame.grid(row=row_index, column=3, padx=10, pady=3)

            def make_delete_callback(site_name):
                return lambda: (
                    delete_password(site_name),
                    list_window.destroy(),
                    on_show_all()
                )

            def make_copy_callback(pwd):
                return lambda: (
                    list_window.clipboard_clear(),
                    list_window.clipboard_append(pwd)
                )

            def make_edit_callback(entry_data):
                def edit():
                    edit_window = ctk.CTkToplevel()
                    edit_window.title(f"Modifier: {entry_data['site']}")
                    edit_window.geometry("400x250")

                    ctk.CTkLabel(edit_window, text="Identifiant:").pack(pady=(20, 5))
                    id_entry = ctk.CTkEntry(edit_window)
                    id_entry.insert(0, entry_data["id"])
                    id_entry.pack(pady=5)

                    ctk.CTkLabel(edit_window, text="Mot de passe:").pack(pady=5)
                    pwd_entry = ctk.CTkEntry(edit_window)
                    pwd_entry.insert(0, entry_data["password"])
                    pwd_entry.pack(pady=5)

                    def save_changes():
                        update_password(entry_data["site"], id_entry.get(), pwd_entry.get())
                        edit_window.destroy()
                        list_window.destroy()
                        on_show_all()

                    ctk.CTkButton(edit_window, text="Enregistrer", command=save_changes).pack(pady=10)

                return edit

            ctk.CTkButton(action_frame, text="modifier", width=10, command=make_edit_callback(entry)).pack(side="left", padx=2)
            ctk.CTkButton(action_frame, text="copier", width=10, command=make_copy_callback(password)).pack(side="left", padx=2)
            ctk.CTkButton(action_frame, text="supprimer", width=10, command=make_delete_callback(site)).pack(side="left", padx=2)
    close_button = ctk.CTkButton(list_window, text="Fermer", command=list_window.destroy)