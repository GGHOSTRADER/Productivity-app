# In application (testable)
def ask_questions(questions, input_func):
    answers = {}
    for q in questions:
        answers[q] = input_func(f"{q}: ")
    return answers


# Input adapter need to be injected
