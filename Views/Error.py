import customtkinter as ctk

def display_error(error_message : str):
    error_window = ctk.CTk()
    error_window.title("KeyMate - Error")
    error_window.geometry("300x150")
    
    ctk.CTkLabel(error_window, text=error_message, text_color="red").pack(pady=20)
    
    def close_error():
        error_window.destroy()
    
    ctk.CTkButton(error_window, text="OK", command=close_error).pack(pady=10)
    error_window.mainloop()