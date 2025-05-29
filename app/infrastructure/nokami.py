import os
import re
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
from dataclasses import dataclass
from . import shared_state
from infrastructure.presenters.task_profile import categories_tasks


@dataclass
class state_chosed_task:
    task_number: str
    difficulty: str
    est_time: str
    urgency: str
    priority: str
    status: str
    description: str
    process: str
    to_do: str
    type_task: str
    current_project: str
    current_project_priority: str
    current_task_number: str
    current_task_title: str


def trace(func):
    def wrapper(*args, **kwargs):
        print(f"[TRACE] → {func.__name__} args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[TRACE] ← {func.__name__} returned {result}")
        return result

    return wrapper


# Scoring maps
project_priority_score = {"high": 3, "medium": 2, "low": 1}
task_priority_score = {"high": 3, "medium": 2, "low": 1}
status_score = {"working on it": 2, "nothing started": 1, "complete": 0}
difficulty_score = {"medium": 2, "easy": 3, "hard": 1}
time_score = {"hours": 3, "day": 2, "several days": 3}
urgency_score = {"yes": 1, "no": 0}

# Valid values
valid_priorities = {"high", "medium", "low", "none"}
valid_statuses = {"nothing started", "working on it", "complete"}
valid_diff = ["easy", "medium", "hard"]
valid_time = ["hours", "day", "several days"]
valid_urgency = ["yes", "no"]
valid_type_task = list(categories_tasks.keys())


class LoadAndValidate:
    def __init__(self):
        self.errors = []
        self.lines = []
        self.current_project = None
        self.current_project_priority = None
        self.current_task_number = None
        self.current_task_title = None
        self.tasks = []

    def load_doc(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            self.lines = f.readlines()

    def checking_load(self):
        self.errors = []
        self.tasks = []

        for idx, line in enumerate(self.lines):
            stripped = line.strip().lower()
            bracket_errors = []

            if stripped.startswith("# project:"):
                self.current_project = stripped.replace("# project:", "").strip()

            elif stripped.startswith("priority:"):
                self.current_project_priority = stripped.replace(
                    "priority:", ""
                ).strip()

            elif stripped.startswith("## task"):
                raw_task = stripped.replace("## task", "").strip()
                if ":" in raw_task:
                    task_number, task_title = raw_task.split(":", 1)
                else:
                    task_number, task_title = "", raw_task
                self.current_task_number = task_number.strip()
                self.current_task_title = task_title.strip()

            elif stripped.startswith("-["):
                match = re.match(
                    r"-\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]",
                    stripped,
                )

                if match:
                    brackets = list(match.groups())
                    task_number, difficulty, est_time, urgency = brackets[0:4]
                    priority, status, description, process, to_do, task_type = brackets[
                        4:
                    ]

                    try:
                        int(task_number)
                    except ValueError:
                        bracket_errors.append((idx, 0, "Task Number", task_number))

                    if difficulty not in valid_diff:
                        bracket_errors.append((idx, 1, "Difficulty", difficulty))
                    if est_time not in valid_time:
                        bracket_errors.append((idx, 2, "Estimated Time", est_time))
                    if urgency not in valid_urgency:
                        bracket_errors.append((idx, 3, "Urgency", urgency))
                    if priority not in valid_priorities:
                        bracket_errors.append((idx, 4, "Priority", priority))
                    if status not in valid_statuses:
                        bracket_errors.append((idx, 5, "Status", status))
                    if task_type not in valid_type_task:
                        bracket_errors.append((idx, 9, "Task Type", task_type))

                    if bracket_errors:
                        self.errors.extend(bracket_errors)
                    else:
                        self.tasks.append(
                            (
                                task_number,
                                difficulty,
                                est_time,
                                urgency,
                                priority,
                                status,
                                description.strip(),
                                process.strip(),
                                to_do.strip(),
                                task_type,
                                self.current_project,
                                self.current_project_priority,
                                self.current_task_number,
                                self.current_task_title,
                            )
                        )


class NokamiApp:
    def __init__(self, root, on_done=None):
        self.root = tk.Toplevel(root)
        self.root.title("Nokami Task Manager")
        self.text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.on_done = on_done

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base_dir, "nok_data.md")
        self.lv = LoadAndValidate()

        if not os.path.exists(self.file_path):
            messagebox.showerror("File Error", f"File not found: {self.file_path}")
            return

        self.reload_and_fix_errors()
        self.scored_tasks = self.score_tasks()
        self.idx = 0
        self.display_task(self.idx)

    def reload_and_fix_errors(self):
        self.lv.load_doc(self.file_path)
        self.lv.checking_load()

        while self.lv.errors:
            for error in self.lv.errors:
                line_num, bracket_index, error_type, error_value = error
                current_line = self.lv.lines[line_num].strip()
                new_value = simpledialog.askstring(
                    "Correction Required",
                    f"Line {line_num + 1}: Invalid {error_type} → '{error_value}'\nCurrent Line:\n{current_line}\n\nEnter corrected {error_type}:",
                    parent=self.root,
                )

                brackets = re.findall(r"\[(.*?)\]", self.lv.lines[line_num])
                if len(brackets) >= 10:

                    brackets[bracket_index] = new_value
                    new_line = "-[" + "][".join(brackets) + "]\n"
                    self.lv.lines[line_num] = new_line
                    with open(self.file_path, "w", encoding="utf-8") as f:
                        f.writelines(self.lv.lines)

            self.lv.errors = []
            self.lv.checking_load()

    def score_tasks(self):
        scored = []
        for task in self.lv.tasks:
            (
                number,
                difficulty,
                est_time,
                urgency,
                priority,
                status,
                description,
                process,
                to_do,
                type_task,
                proj,
                proj_priority,
                task_number,
                task_title,
            ) = task

            if status.lower() == "complete":
                continue

            score = (
                project_priority_score.get(proj_priority, 0)
                + task_priority_score.get(priority, 0)
                + status_score.get(status, 0) * 0.8
                + difficulty_score.get(difficulty, 0) * 0.8
                + time_score.get(est_time, 0) * 0.5
                + urgency_score.get(urgency, 0)
            )

            scored.append(
                (
                    score,
                    proj,
                    proj_priority,
                    task_number,
                    task_title,
                    number,
                    difficulty,
                    est_time,
                    urgency,
                    priority,
                    status,
                    description,
                    process,
                    to_do,
                    type_task,
                )
            )

        return sorted(scored, key=lambda x: x[0], reverse=True)

    def display_task(self, idx):
        if 0 <= idx < len(self.scored_tasks):
            task = self.scored_tasks[idx]
            text = f"Task #{idx + 1}\n\n"
            text += f"Project: {task[1]} (Priority: {task[2]})\n"
            text += f"Task {task[3]}: {task[4]}\nScore: {task[0]}\n"
            text += f"Difficulty: {task[6]} | Time: {task[7]} | Urgency: {task[8]}\n"
            text += f"Task Priority: {task[9]} | Status: {task[10]}\n\n"
            text += f"Description: {task[11]}\nProcess: {task[12]}\nTo do: {task[13]}"
            self.text.config(state="normal")
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, text)
            self.text.config(state="disabled")
            self.root.geometry("")  # Auto-resize to content
            self.create_controls()

    def create_controls(self):
        if hasattr(self, "btn_frame"):
            self.btn_frame.destroy()
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=10)

        tk.Button(self.btn_frame, text="Next", command=self.next_task).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(self.btn_frame, text="Back", command=self.prev_task).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(
            self.btn_frame,
            text="Choose",
            command=lambda: self.choose_task(self.on_done),
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="List", command=self.list_tasks).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(self.btn_frame, text="Exit", command=self.root.destroy).pack(
            side=tk.LEFT, padx=5
        )

    def next_task(self):
        self.idx += 1
        if self.idx >= len(self.scored_tasks):
            self.idx = len(self.scored_tasks) - 1
        self.display_task(self.idx)

    def prev_task(self):
        self.idx -= 1
        if self.idx < 0:
            self.idx = 0
        self.display_task(self.idx)

    def choose_task(self, on_done=None):
        self.idx = max(self.idx, 0)
        (
            score,
            proj,
            proj_priority,
            task_number,
            task_title,
            number,
            difficulty,
            est_time,
            urgency,
            priority,
            status,
            description,
            process,
            to_do,
            type_task,
        ) = self.scored_tasks[self.idx]

        shared_state.state_from_chosen = state_chosed_task(
            task_number=number,
            difficulty=difficulty,
            est_time=est_time,
            urgency=urgency,
            priority=priority,
            status=status,
            description=description,
            process=process,
            to_do=to_do,
            type_task=type_task,
            current_project=proj,
            current_project_priority=proj_priority,
            current_task_number=task_number,
            current_task_title=task_title,
        )
        messagebox.showinfo("Task Chosen", f"Task #{self.idx + 1} locked in.")
        if on_done:
            on_done()

        self.root.destroy()

    def list_tasks(self):
        lines = ["All Tasks by Score:\n"]
        for i, t in enumerate(self.scored_tasks):
            lines.append(
                f"\nRank {i+1}\n - Project: {t[1]} \n - Task {t[3]}: {t[4]}\n - Description: {t[-3]} \n - Score: {t[0]}"
            )
        self.text.config(state="normal")
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, "\n".join(lines))
        self.text.config(state="disabled")
        self.root.geometry("")
        self.root.attributes("-topmost", True)  # Keep on top


def launch_nokami_gui(root, on_done=None):
    try:
        NokamiApp(root, on_done)
    except Exception as e:
        print(f"[CRITICAL] Nokami GUI failed to launch: {e}")
        messagebox.showerror("Launch Error", f"Failed to launch Nokami:\n{e}")
