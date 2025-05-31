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
from infrastructure.input_adapters import (
    get_user_input,
    merge_gui_state_with_user_input,
    pair_gui_state_with_questions,
)
from infrastructure.gui_windows.tips import display_project_tips
from infrastructure.presenters.cli import get_questions
from infrastructure.nokami import launch_nokami_gui
from infrastructure import shared_state


def firing_app():
    root = tb.Window(themename="darkly")
    root.withdraw()
    image_splash = (
        r"C:\Users\g_med\Downloads\ChatGPT Image May 13, 2025, 01_48_05 PM.png"
    )

    show_splash_screen(
        root,
        image_splash,
        on_done=lambda: open_todo_checklist_window(
            root,
            PREDEFINED_TASKS,
            lambda: launch_nokami_gui(
                root,
                lambda: display_project_tips(
                    root,
                    categories_tasks[shared_state.state_from_chosen.type_task].tips,
                    on_all_tasks_completed=None,
                ),
            ),
        ),
        duration=10000,
    )

    # This need to be defined
    questions = get_questions()
    user_data = ask_questions(questions, get_user_input)
    gui_data = pair_gui_state_with_questions(
        [
            shared_state.state_from_chosen.current_task_title,
            shared_state.state_from_chosen.description,
            shared_state.state_from_chosen.to_do,
        ],
        ["Name", "Description", "To do"],
    )
    data_merged_dic = merge_gui_state_with_user_input(user_data, gui_data)

    launch_app(
        root,
        data_merged_dic,
        categories_tasks["stabilization"].sound_url,
        categories_tasks[shared_state.state_from_chosen.type_task].sound_url,
        lambda: display_project_tips(
            root,
            categories_tasks[shared_state.state_from_chosen.type_task].tips,
            on_all_tasks_completed=None,
        ),
    )
    root.mainloop()
