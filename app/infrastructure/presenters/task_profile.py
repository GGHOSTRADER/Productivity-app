from dataclasses import dataclass

# --- Static Media URLs ---
BROWN_NOISE = (
    "https://www.youtube.com/watch?v=RqzGzwTY-6w&list="
    "PLex1YocpfQzmt9wuvV7io6YDZS4Eb4pvU"
)

ALPHA_BINAURAL = (
    "https://www.youtube.com/watch?v=p2_zDvtPQ"
    "-g&list=PLex1YocpfQzmy-CByxBQ1dth_iMUgfwTL"
)

CHILLPOP = (
    "https://www.youtube.com/watch?v=5v-z79NQJC0&list="
    "PLex1YocpfQzmUu_uAnEI6iMgm9qtqdHDI&index=1"
)

STABILIZATION = "https://www.youtube.com/watch?v=RcMX0PCw1m0"

# --- Static Tips ---
BOOK_RESEARCH_TIPS = (
    "I don't absorb from passive learning, I need to be active and engaged\n\n"
    "1) Keeping Focus:\n"
    "- WHY AM I READING THIS?\n"
    "- WHAT AM I TRYING TO SOLVE OR LEARN?\n"
    "- Reading for the sake of reading is boring — I need a reason.\n\n"
    "2) Promote Memory:\n"
    "- Simulate as I read\n"
    "- Do drawings\n"
    "- Address questions from first read\n"
    "- I am a spatial thinker — I need to simulate and question to retain.\n\n"
    "3) Friction Management:\n"
    "- Read topics and get familiar with jargon\n"
    "- Start from the back of the book\n"
    "- It's OK to focus only on relevant parts\n"
    "- First read = confusion → Write questions\n"
    "- Second read = deeper understanding\n\n"
    "READ TO HUNT FOR INFORMATION!\n\n"
)

AGENT_TIPS = (
    "Make the most of your time using the agent — BE PRECISE AND PRODUCTIVE\n\n"
    "1) Focus:\n"
    "- WHY AM I ASKING THIS?\n"
    "- WHAT AM I TRYING TO SOLVE?\n"
    "- Is this impacting immediate work?\n"
    "- Don’t fall into rabbit holes — be targeted.\n\n"
    "2) Memory:\n"
    "- Write down jargon and ask later\n"
    "- Ask for analogies and simulate them\n"
    "- I need spatial reasoning to understand and retain\n\n"
    "3) Real World Application:\n"
    "- Ask for a scaffold or steps tailored to your project\n"
    "- Don’t get lost in theory — convert it to action!\n\n"
    "AGENT IS FOR GAINING MOMENTUM\n\n."
)

CONCEPTUALIZATION_TIPS = (
    "1) Focus:\n"
    "- WHY AM I ASKING THIS?\n"
    "- WHAT AM I TRYING TO SOLVE?\n"
    "- Be clear on what you want to build\n\n"
    "2) Memory:\n"
    "- Simulate the outcome in your head\n"
    "- Think in systems → then in actionable steps\n"
    "- Use your spatial/visual strengths\n\n"
    "3) Process:\n"
    "- Use nonlinear methods: mind maps, paper\n"
    "- Write the next actionable steps\n\n"
    "GOOD CONCEPTS SAVE TIME.\n\n"
)

DELIBERATE_WORK_TIPS = (
    "1) Build Momentum:\n"
    "- Do the easiest things first\n"
    "- Break tasks into microscopic steps\n\n"
    "2) No Target, No Work:\n"
    "- Vague tasks = friction → clarify your goals\n"
    "- Use conceptualization to define unclear work\n"
    "- Dump what you're doing into your pad immediately\n\n"
    "3) Be a Sniper:\n"
    "- One task at a time\n"
    "- Don’t zoom out — execute micro\n"
    "- You’re not naturally a doer \n\n"
)


# --- Dataclass Definition ---
@dataclass
class TaskProfile:
    tips: str
    sound_url: str


# --- Central Registry ---
categories_tasks = {
    "book research": TaskProfile(tips=BOOK_RESEARCH_TIPS, sound_url=BROWN_NOISE),
    "agent research": TaskProfile(tips=AGENT_TIPS, sound_url=BROWN_NOISE),
    "conceptualization": TaskProfile(
        tips=CONCEPTUALIZATION_TIPS, sound_url=ALPHA_BINAURAL
    ),
    "deliberate work": TaskProfile(tips=DELIBERATE_WORK_TIPS, sound_url=CHILLPOP),
    "stabilization": TaskProfile(tips=None, sound_url=STABILIZATION),
}
