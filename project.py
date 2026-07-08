import tkinter as tk
import math

# ---------------------------- CONSTANTS & THEME ------------------------------- #
# Modern Dark Mode Palette
BG_DARK = "#1A1A24"      # Deep dark background
TEXT_LIGHT = "#E2E2EC"   # Off-white for labels
CYAN = "#00ADB5"         # Electric Cyan for Work
MAGENTA = "#FF2E93"      # Neon Magenta for Breaks
CARD_BG = "#252538"      # Slightly lighter dark for inputs
FONT_NAME = "Courier"

# Global Variables
reps = 0
timer = None
work_min = 25
short_break_min = 5

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=CYAN)
    check_marks.config(text="")
    reps = 0
    # Re-enable inputs when reset
    work_input.config(state="normal")
    break_input.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, work_min, short_break_min
    reps += 1

    # Capture custom times from the input boxes. If empty, fall back to defaults.
    try:
        work_min = float(work_input.get())
    except ValueError:
        work_min = 25

    try:
        short_break_min = float(break_input.get())
    except ValueError:
        short_break_min = 5

    # Disable inputs while timer is running so user can't change them mid-session
    work_input.config(state="disabled")
    break_input.config(state="disabled")

    work_sec = work_min * 60
    short_break_sec = short_break_min * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=MAGENTA)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=CYAN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Custom Pomodoro Timer")
window.config(padx=40, pady=40, bg=BG_DARK)

# 1. Main Title
title_label = tk.Label(text="Timer", fg=CYAN, bg=BG_DARK, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

# 2. Input Fields Layout
# Work Time Input
work_label = tk.Label(text="Work Minutes:", fg=TEXT_LIGHT, bg=BG_DARK, font=(FONT_NAME, 12))
work_label.grid(column=0, row=1, sticky="e", pady=5)
work_input = tk.Entry(width=10, font=(FONT_NAME, 12), bg=CARD_BG, fg=TEXT_LIGHT, insertbackground=TEXT_LIGHT, bd=0)
work_input.insert(0, "25") # Default value
work_input.grid(column=1, row=1, sticky="w", padx=10, pady=5)

# Break Time Input
break_label = tk.Label(text="Break Minutes:", fg=TEXT_LIGHT, bg=BG_DARK, font=(FONT_NAME, 12))
break_label.grid(column=0, row=2, sticky="e", pady=5)
break_input = tk.Entry(width=10, font=(FONT_NAME, 12), bg=CARD_BG, fg=TEXT_LIGHT, insertbackground=TEXT_LIGHT, bd=0)
break_input.insert(0, "5") # Default value
break_input.grid(column=1, row=2, sticky="w", padx=10, pady=5)

# 3. Digital Clock Canvas
canvas = tk.Canvas(width=220, height=100, bg=BG_DARK, highlightthickness=0)
timer_text = canvas.create_text(110, 50, text="00:00", fill=TEXT_LIGHT, font=(FONT_NAME, 45, "bold"))
canvas.grid(column=0, row=3, columnspan=2, pady=20)

# 4. Buttons (Styled to look modern)
start_button = tk.Button(text="START", font=(FONT_NAME, 12, "bold"), bg=CYAN, fg=BG_DARK, activebackground=TEXT_LIGHT, bd=0, padx=15, pady=5, command=start_timer)
start_button.grid(column=0, row=4, pady=10)

reset_button = tk.Button(text="RESET", font=(FONT_NAME, 12, "bold"), bg=MAGENTA, fg=BG_DARK, activebackground=TEXT_LIGHT, bd=0, padx=15, pady=5, command=reset_timer)
reset_button.grid(column=1, row=4, pady=10)

# 5. Checkmarks
check_marks = tk.Label(fg=CYAN, bg=BG_DARK, font=(FONT_NAME, 18, "bold"))
check_marks.grid(column=0, row=5, columnspan=2, pady=10)

window.mainloop()




