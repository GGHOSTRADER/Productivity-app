from dataclasses import dataclass


# --- prompting functions values ---
WORKTYPE = "Work type tips now"
QUESTIONS = "Organization QuestionS"
GENERAL_TIPS = "💡 General Productivity tips"


@dataclass
class PromptContinueValues:
    work_type: str
    questions: str
    general_tips: str


prompt_continue_values = PromptContinueValues(
    work_type=WORKTYPE, questions=QUESTIONS, general_tips=GENERAL_TIPS
)


# --- OI ---
def continue_prompt(STAGE):
    input(f"\n{STAGE} --> Press Enter to continue...\n\n")


# domain/questions.py
def get_questions():
    return ["Name", "What are you doing?", "Why?", "Consequence of not doing it?"]
