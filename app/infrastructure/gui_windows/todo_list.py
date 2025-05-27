import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tb
from ttkbootstrap import Style
import winsound


def open_todo_checklist_window(master, predefined_tasks, on_all_tasks_completed=None):
    window = tb.Toplevel(master)
    window.title("PRODUCTIVITY SYSTEM")
    window.attributes("-topmost", True)
    window.configure(bg="black")  # dark background for window
    # First number is the width, second is the height
    window.geometry("1300x550")  # Set the size of the window

    # Create custom style for dark frame
    style = Style()
    style.configure("Dark.TFrame")
    custom_font = tkfont.Font(family="Helvetica", size=16)  # font size from check box
    style.configure(".", font=custom_font)

    # Apply the dark frame style here
    task_frame = tb.Frame(window, style="Dark.TFrame")
    task_frame.pack(pady=20)

    # Header label with matching background
    tb.Label(
        task_frame,
        text="DISTRACTION IS WHAT IS BETWEEN YOU AND YOUR GOALS",
        font=("Segoe UI", 16, "bold"),
        foreground="white",
    ).pack(pady=(0, 10))

    task_vars = []

    def check_all_tasks():
        if all(var.get() for var in task_vars):
            try:
                winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            except Exception:
                pass

            if on_all_tasks_completed:
                on_all_tasks_completed()
                window.destroy()
            else:
                window.destroy()

    for task_text in predefined_tasks:
        var = tk.BooleanVar()
        cb = tb.Checkbutton(
            task_frame,
            text=task_text,
            variable=var,
            bootstyle="success-round-toggle",  # clean toggle style
            command=check_all_tasks,
        )
        cb.pack(anchor="w", padx=10, pady=5)
        task_vars.append(var)

    return window
