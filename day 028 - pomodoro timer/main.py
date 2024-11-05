from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 1
window_timer = None
click_amount = 0

# ---------------------------- TIMER RESET ---------------------------- # 
def reset_timer():
    global reps
    global click_amount
    window.after_cancel(window_timer)
    timer_label.config(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 60, "normal"))
    canvas.itemconfig(time, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
    check_marks.config(text="")
    reps = 1
    click_amount = 0

# ---------------------------- TIMER MECHANISM ------------------------ # 
def click_start():
    global click_amount
    work_reps_list = [1, 3, 5, 7]
    short_break_reps_list = [2, 4, 6]

    if click_amount == 0:
        if reps in work_reps_list:
            count_down(WORK_MIN * 60)
            timer_label.config(text="WORK", fg=GREEN)
        elif reps in short_break_reps_list:
            count_down(SHORT_BREAK_MIN * 60)
            timer_label.config(text="BREAK", fg=PINK)
        elif reps == 8:
            count_down(LONG_BREAK_MIN * 60)
            timer_label.config(text="BREAK", fg=RED)
        click_amount += 1

def add_rep():
    global reps
    reps += 1
    if reps > 8:
        reps == 1
    if reps == 2:
        check_marks.config(text="✔")
    elif reps == 4:
        check_marks.config(text="✔ ✔")
    elif reps == 6:
        check_marks.config(text="✔ ✔ ✔")
    elif reps == 8:
        check_marks.config(text="✔ ✔ ✔ ✔")


# ---------------------------- COUNTDOWN MECHANISM -------------------- # 
def count_down(number):
    global window_timer
    number_minutes = math.floor(number / 60)
    number_seconds = number % 60
    if number_minutes < 10:
        m = number_minutes
        number_minutes = f"0{m}"
    if number_seconds < 10:
        s = number_seconds
        number_seconds = f"0{s}"

    canvas.itemconfig(time, text=f"{number_minutes}:{number_seconds}")
    if number > 0:
        window_timer = window.after(1000, count_down, number-1)
    else:
        add_rep()
        click_start()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(440, 440)
window.config(padx=100 , pady=50, bg=YELLOW)

canvas = Canvas(width=240, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato = canvas.create_image(120, 150, image=tomato_img)
time = canvas.create_text(120, 170, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 60, "normal"))
timer_label.grid(column=1, row=0)

check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
check_marks.grid(column=1, row=3)

start_button = Button(text="Start", bg="white", fg="black", font=(FONT_NAME, 10, "normal"), command=click_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", fg="black", font=(FONT_NAME, 10, "normal"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()