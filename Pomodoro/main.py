import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps,marks
    window.after_cancel(timer)
    reps = 0
    label.config(text="Timer")
    canvas.itemconfig(time_text, text="00:00")
    marks = ""
    check_mark.config(text=marks)
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(fg=RED,text="Long break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(fg=PINK, text="Short break")
    else:
        count_down(WORK_MIN * 60)
        label.config(fg=GREEN, text="Work")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps,marks,timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"{0}{seconds}"
    canvas.itemconfig(time_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks += "✅"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=False)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.config(width=10)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"),command=reset_timer)
reset_button.config(width=10)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_mark.grid(row=3, column=1)

window.mainloop()
