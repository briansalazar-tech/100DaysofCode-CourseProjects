from tkinter import *
import math

# Constants and global variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_marks = ""
timer = None


def reset_timer():
    """Reset values when the reset value is clicked"""
    global check_marks, reps
    window.after_cancel(timer)

    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks = ""
    check_mark_label.config(text=check_marks)
    reps = 0


def start_timer():
    """Starts the countdown timer"""
    global reps, check_marks
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    # Long break
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    
    # Short break
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
   
    # Work
    elif reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)
        print("Work block")
        if reps > 1:
            check_marks += "✅"


def countdown(count):
    """Performs the countdown. Minutes and seconds are displayed in the format of MM:SS"""
    global check_marks, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    # Add a 0 in front of the number if the number = 00 (displayed as MM:0 instead of MM:00)
    if count_sec == 0:
        count_sec = "00"
    
    # Add a 0 in front of the number if the number < 10 (displayed as MM:S instead of MM:0S)
    if int(count_sec) < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_mark_label.config(text=check_marks)


# Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./Day28-PomodoroTImer/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Mark Label
check_mark_label = Label(text="", fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)


window.mainloop()