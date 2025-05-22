import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tb
from ttkbootstrap import Style
import winsound


def display_project_tips(master, task_tip, on_all_tasks_completed=None):
    window = tb.Toplevel(master)
    window.title("TIPS")
    window.attributes("-topmost", True)
    window.configure(bg="black")  # dark background for window
    # First number is the width, second is the height

    # Apply the dark frame style here
    task_frame = tb.Frame(window, style="Dark.TFrame")
    task_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Header label with matching background
    tb.Label(
        task_frame,
        text=task_tip,
        font=("Segoe UI", 13, "bold"),
        foreground="white",
    ).pack(pady=(0, 10))

    tb.Button(
        task_frame,
        text="Exit",
        width=40,
        bootstyle="success",
        command=lambda: window.destroy(),
    ).pack(pady=6)

    return window
