import customtkinter as ctk
from Views.ViewConfig import setup_window
from Views.Home import launch_ui
from crypto import is_password_correct



def authenticate():
    auth_window = ctk.CTk()
    auth_window.title("KeyMate - Authentification")
    auth_window.geometry(setup_window(auth_window))
    
    ctk.CTkLabel(auth_window, text="Entrez le Master Password:").pack(pady=10)
    password_entry = ctk.CTkEntry(auth_window, show="*")
    password_entry.pack(pady=5)
    
    result_label = ctk.CTkLabel(auth_window, text="")
    result_label.pack(pady=5)
    
    def verify(entered=None):
        if entered is None:
            entered = password_entry.get()
        if is_password_correct(entered):
            auth_window.destroy()
            launch_ui()  # Launch the main UI
        else:
            result_label.configure(text="Mot de passe incorrect", text_color="red")
    
    def on_enter(event):
        verify(event.widget.get())
    
    ctk.CTkButton(auth_window, text="Valider", command=verify).pack(pady=5)
    password_entry.bind("<Return>", command=on_enter)
    auth_window.mainloop()