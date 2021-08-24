import tkinter
from tkinter import *  # import all the class in tkinter
import math
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
timer = None
"""
How the timer dived 8 sections:
25 minutes work
5 minutes shor break
25 minutes work
5 minutes short break
25 minutes work
5 minutes shor break
25 minutes work
20 minutes long break
"""

# ---------------------------- TIMER RESET ------------------------------- # 
#create a reset function to reset timer and text
def reset_timer():
    window.after_cancel(timer) # can cancel previous timer and restart again
    #change the timer_text = 00:00, canvas
    canvas.itemconfig(timer_text, text="00:00")
    #my_laber = "Timer"
    my_label.config(text="Timer")
    #reset check_marks
    check_marks.config(text="")
    global reps  # in order to restart from work time
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
#this function is just calling the function- count_down()
def start_timer():
    global reps
    reps += 1  # the repetation increasing 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #if it is long break time 20 mins:
    if reps % 8 == 0:
        count_down(long_break_sec)
        #change the label when is on long break
        my_label.config(text="Break", fg=RED)

    #if short time break : 5 mins
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec) #seconds * 60 = mins
        my_label.config(text=" Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#http://tcl.tk/man/tcl8.6/TclCmd/after.htm
#after — Execute a command after a time delay
#create a funtion for after()function to excatued:
#after(milionsecond, function, unlittmed arguments)
def count_down(count):
    #covert millisecond to 00:00 format:
    # math.floor will get the int before the decimal
    count_min = math.floor(count / 60)
    count_sec = count % 60  # will give the reminder of count_min
    # to display better vision:
    if count_sec < 0: # this is dynamic typing: can change the data type
        count_sec = "00" # from int to str
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    #change canvas element:
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1) #1000 is millisecond
    else:
        start_timer() # once the first timer finished, it will start again and reps +1
        #add a checkmark for every two reps
        marks = ""
        work_sessions= math.floor(reps/2) # round down into int
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks) # update the checkmarks


# ---------------------------- UI SETUP ------------------------------- #

#create a window:
window = Tk()
# create a title:
window.title("Pomodoro")   # means tomato in Italian


# to make screen a bigger:
window.config(padx=100, pady=50, bg=YELLOW) # padding x an padding y position, background color

# put image into program, create a Canvas Widget, background color
canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0) #highlightthickness can hide the lins around image

# to read through an image file, and provide the image location:
tomato_img = PhotoImage(file="tomato.png")

# add image into it
canvas.create_image(100, 112, image=tomato_img) # x and y position , half the size of image

#pack the image:
canvas.grid(column=2, row=2)



# create some text:, provide x and y values, these values can change the text position inside the image
#fill is the color, font is the tuple value
# set a variable
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


#create a label class
#font is tuple value, fg = Foreground color
my_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, "50", "bold"))

#use grid to layout:
my_label.grid(column=2, row=1)



#create check_marks label
#fg= Foreground color
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=4)


#creat  button classes:
#command= to call the start_timer function, just the name, not include paratheles
start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, "20", ), command=start_timer) #highlightthickness=0 get rid of white border
start_button.grid(column=1, row=3)

#use grid to layout:
reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, "20", ), command=reset_timer) #command to call the reset function
reset_button.grid(column=3, row=3)



# keep the window open:
window.mainloop()