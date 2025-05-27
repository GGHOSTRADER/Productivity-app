from infrastructure.prompt_project_type import prompt_user_for_project_type
from infrastructure.presenters.cli import (
    prompt_continue_values,
    continue_prompt,
)
from infrastructure.presenters.task_profile import categories_tasks
from infrastructure.gui_windows.time import launch_app
from infrastructure.gui_windows.todo_list import open_todo_checklist_window
from infrastructure.presenters.gui import PREDEFINED_TASKS
import ttkbootstrap as tb
from infrastructure.gui_windows.splash import show_splash_screen
from application.input_service import ask_questions
from infrastructure.input_adapters import get_user_input
from infrastructure.gui_windows.tips import display_project_tips
from infrastructure.presenters.cli import get_questions


def firing_app():
    root = tb.Window(themename="darkly")
    root.withdraw()
    image_splash = (
        r"C:\Users\g_med\Downloads\ChatGPT Image May 13, 2025, 01_48_05 PM.png"
    )

    show_splash_screen(
        root,
        image_splash,
        on_done=lambda: open_todo_checklist_window(root, PREDEFINED_TASKS),
        duration=10000,
    )

    user_input = prompt_user_for_project_type(list(categories_tasks.keys()))

    display_project_tips(
        root, categories_tasks[user_input].tips, on_all_tasks_completed=None
    )

    # This need to be defined
    questions = get_questions()
    user_data = ask_questions(questions, get_user_input)

    launch_app(
        root,
        user_data,
        categories_tasks["stabilization"].sound_url,
        categories_tasks[user_input].sound_url,
        lambda: display_project_tips(
            root, categories_tasks[user_input].tips, on_all_tasks_completed=None
        ),
    )
    root.mainloop()
