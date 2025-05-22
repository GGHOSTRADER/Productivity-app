# infrastructure/splash_adapter.py
import tkinter as tk
from PIL import Image, ImageTk


# Controller that calls smaller funcs
def show_splash_screen(root, img_path, on_done=None, duration=10000):
    splash = create_splash_window(root)

    try:
        render_image(splash, img_path)
    except Exception as e:
        render_error(splash, str(e))

    render_text(splash, "ENGAGING ORDER 66")
    center_window(splash)

    root.after(duration, lambda: close_splash(splash, on_done))


def create_splash_window(root):
    splash = tk.Toplevel(root)
    splash.title("Booting...")
    splash.geometry("1400x1200")
    splash.attributes("-topmost", True)  # Keep on top
    splash.configure(bg="black")
    return splash


def render_image(parent, path, max_w=1200, max_h=1000):
    image = Image.open(path)
    image.thumbnail((max_w, max_h), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(parent, image=photo, bg="black")
    label.image = photo  # Prevent garbage collection
    label.pack(pady=10)


def render_error(parent, message):
    tk.Label(
        parent, text=f"(Image load failed: {message})", fg="white", bg="black"
    ).pack()


def render_text(parent, text):
    tk.Label(
        parent,
        text=text,
        font=("Helvetica", 16, "bold"),
        relief="flat",
    ).pack(pady=10)


def center_window(window):
    window.update_idletasks()
    w, h = window.winfo_width(), window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (w // 2)
    y = (window.winfo_screenheight() // 2) - (h // 2)
    window.geometry(f"+{x}+{y}")


def close_splash(window, on_done=None):
    window.destroy()
    if on_done:
        on_done()
