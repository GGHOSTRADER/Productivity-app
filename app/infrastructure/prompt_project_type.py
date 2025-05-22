# This module is for initating the prompting for project type


def prompt_user_for_project_type(categories):
    while True:
        user_input = input(_project_type_prompt()).strip().lower()
        if user_input in categories:
            return user_input
        print("❌ Invalid project type. Please try again.\n")
    return user_input


def _project_type_prompt():
    return (
        "What type of Project:\n"
        "- Book research\n"
        "- Agent research\n"
        "- Conceptualization/ Planning\n"
        "- Deliberate Work\n"
        "\nYour choice: "
    )
