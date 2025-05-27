# gui.py
import tkinter as tk
import ttkbootstrap as tb
from datetime import timedelta
from infrastructure.effects import open_url
from domain.state import toggle_mode as toggle_mode_state, reset_timer, tick_timer
from infrastructure.presenters.cli import get_questions


class FocusApp:
    def __init__(self, root, data, stabilization_url, task_url, hook=None):
        self.root = root
        self.data = data
        self.mode = "Rest"
        self.seconds_elapsed = 0
        self.timer_running = True
        self.alarm_triggered = False  # ← track if alarm has already gone off
        self.stabilization_url = stabilization_url
        self.task_url = task_url
        self.hook = hook
        self.cycle_counter_flag = True
        self.cycle_counter_storing = 0

        self.setup_window()
        self.create_user_data_display()
        self.create_control_buttons()
        self.create_timer()
        self.create_cycle_counter()
        self.update_cycle_counter()
        self.update_timer()

    def setup_window(self):
        self.root.title("Focus Tracker")
        self.root.resizable(True, True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="black")

    def create_user_data_display(self):
        for label in get_questions():
            frame = tk.Frame(self.root, bg="black")
            frame.pack(pady=5, anchor="w")
            tk.Label(frame, text=f"{label}:", width=25, fg="white", bg="black").pack(
                side="left"
            )
            tk.Label(
                frame,
                text=self.data[label],
                width=70,
                fg="white",
                bg="black",
                anchor="w",
            ).pack(side="left", fill="x", expand=True)

    def create_control_buttons(self):
        tb.Button(
            self.root,
            text="Tips",
            width=20,
            bootstyle="success",
            command=self.hook,
        ).pack(pady=6)

        tb.Button(
            self.root,
            text="Stabilization",
            width=20,
            bootstyle="success",
            command=lambda: open_url(self.stabilization_url),
        ).pack(pady=6)

        tb.Button(
            self.root,
            text="Project Music",
            width=20,
            bootstyle="success",
            command=lambda: open_url(self.task_url),
        ).pack(pady=3)

        self.toggle_btn = tb.Button(
            self.root,
            text=self.mode,
            width=20,
            bootstyle="success",
            command=self.toggle_mode,
        )
        self.toggle_btn.pack(pady=5)

    def create_timer(self):
        self.timer_label = tb.Label(
            self.root,
            text=self.format_time(self.seconds_elapsed),
            font=("Helvetica", 24),
        )
        self.timer_label.pack(pady=10)

    def format_time(self, seconds):
        return str(timedelta(seconds=seconds))[2:7]

    def toggle_mode(self):
        self.mode = toggle_mode_state(self.mode)
        self.toggle_btn.config(text=self.mode)
        self.seconds_elapsed = reset_timer()
        self.alarm_triggered = False  # reset alarm when mode changes

    def update_timer(self):
        self.seconds_elapsed = tick_timer(self.seconds_elapsed)
        self.timer_label.config(text=self.format_time(self.seconds_elapsed))

        if self.mode == "Work" and not self.alarm_triggered:
            self.cycle_counter_flag = True  # reset cycle counter flag
            if self.seconds_elapsed >= 240:  # Change seconds
                self.trigger_alarm()
                self.alarm_triggered = True  # prevent retriggering
        if self.mode == "Rest" and self.cycle_counter_flag == True:
            self.cycle_counter_storing += 1
            self.cycle_counter_flag = False
            self.update_cycle_counter()

        self.root.after(1000, self.update_timer)

    def trigger_alarm(self):
        print("🔔 Time’s up! Take a break.")  # or use winsound
        try:
            import winsound

            for _ in range(6):
                winsound.Beep(1000, 800)
        except:
            pass  # cross-platform fallback

    def create_cycle_counter(self):
        self.cycle_counter = tb.Label(
            self.root,
            text=f"Cycle: {(self.cycle_counter_storing)}",
            font=("Helvetica", 24),
        )
        self.cycle_counter.pack(pady=10)

    def update_cycle_counter(self):
        self.cycle_counter.config(text=f"Cycle: {(self.cycle_counter_storing)}")


def launch_app(root, data, stabilization_url, task_url, hook=None):
    root.deiconify()
    FocusApp(root, data, stabilization_url, task_url, hook=hook)
