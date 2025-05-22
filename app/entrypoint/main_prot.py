# main.py
from app.infrastructure.time_gui import launch_app
from app.infrastructure.splash import show_splash_screen
from app.infrastructure.questions import get_questions
from app.application.input_service import ask_questions
from app.infrastructure.input_adapters import get_user_input
import ttkbootstrap as tb

if __name__ == "__main__":

    questions = get_questions()
    user_data = ask_questions(questions, get_user_input)
    root = tb.Window(themename="flatly")
    root.withdraw()
    show_splash_screen(
        root,
        r"C:\Users\g_med\Downloads\ChatGPT Image May 13, 2025, 01_48_05 PM.png",
        on_done=lambda: launch_app(root, user_data),
    )
    root.mainloop()
