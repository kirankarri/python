from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def time_reset():
    global reps
    reps = 1
    #canvas.itemconfig(timer_text,text='new')
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text,text=f'00:00')
    label.config(text='Timer', fg=GREEN)
    checkmark_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def call_timer():
    global reps
    if reps % 2 != 0:
        label.config(text='Work', fg=GREEN)
        time_count(WORK_MIN*60)
    elif reps % 2 == 0:
        if reps % 8 == 0:
            label.config(text='Long Break', fg=RED)
            time_count(LONG_BREAK_MIN*60)
        else: 
            label.config(text='Short Break', fg=PINK)
            time_count(SHORT_BREAK_MIN*60)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def time_count(count):
    if count > 0:
        min = math.floor(count / 60)
        sec = round(count % 60,2)
        if sec < 10:
            sec = f'0{sec}'
        canvas.itemconfig(timer_text,text=f'{min}:{sec}')
        global timer
        timer = screen.after(1000,time_count,count-1)
    if count == 0:
        call_timer()
        num_of_checks = math.floor(reps/2)
        print(num_of_checks)
        checkmark_label.config(text='✔️'*num_of_checks)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title('Pomodoro')
#screen.minsize(400,400)
screen.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(width=220, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = 'tomato.png')
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110,130, text='00:00',fill='white',font=(FONT_NAME,30,'bold'))
canvas.grid(row=2,column=2)
label = Label(text='Timer', font=(FONT_NAME,30,'bold'),fg=GREEN,bg=YELLOW)
label.grid(row=1,column=2)

start_label = Button(text='Start', font=(FONT_NAME,30,'bold'),command=call_timer)
start_label.grid(row=3,column=1)

reset_label = Button(text='Reset',fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,'bold'),command=time_reset)
reset_label.grid(row=3,column=3)

checkmark_label = Label(fg=GREEN,bg=YELLOW, font=(FONT_NAME,15))
checkmark_label.grid(row=3,column=2)

screen.mainloop()