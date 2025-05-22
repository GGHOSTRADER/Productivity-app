# state.py
def toggle_mode(mode):
    if mode == "Rest":
        return "Work"
    elif mode == "Work":
        return "Rest"
    else:
        raise ValueError("Invalid mode")


def reset_timer():
    return 0


def tick_timer(seconds_elapsed):
    return seconds_elapsed + 1
