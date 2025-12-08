import customtkinter as ctk

def setup_window(root: ctk) -> str:
    window_width, window_height = 250, 300

    # Screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Taskbar height assumption
    taskbar_height = 80
    
    x = -8
    y = screen_height - window_height - taskbar_height
    return f"{window_width}x{window_height}+{x}+{y}"