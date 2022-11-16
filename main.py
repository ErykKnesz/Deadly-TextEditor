import tkinter
from tkinter import *

FONT_NAME = "Courier"
TIMER_START = 5
BLANK = ""

root = Tk()
root.title("Deadly Text Editor")
sheet = StringVar(root, BLANK)
timer = IntVar(root, TIMER_START)


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer(*args):
    root.after_cancel(countdown)
    global timer
    timer.set(TIMER_START)


# ---------------------------- APP MECHANISM ------------------------------- #


def export_to_txt():
    with open('your_text.txt', 'w') as f:
        f.write(sheet.get())


def start():
    root.after(1000, countdown)


def end():
    root.after_cancel(countdown)
    top = Toplevel(root)
    top.geometry("750x250")
    top.title("Typing Over!")
    Label(top,
          text="Time's Up, you can export your work to a file now.",
          font=FONT_NAME,
          ).pack(pady=5)
    Button(top, text="Export", command=export_to_txt).place(x=340, y=100)
    global sheet
    sheet.set(text_area.get('1.0','end-1c'))
    text_area.config(state="disabled")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown():
    global timer
    if timer.get() > 0:
        timer.set(timer.get() - 1)
        root.after(1000, countdown)
    else:
        end()


# ---------------------------- UI SETUP ------------------------------- #


root.config(padx=5, pady=5)

text_area = Text(root, font=FONT_NAME, height=50, width=100)
text_area.bind('<KeyRelease>', lambda *args: reset_timer())
text_area.grid(column=1, row=2, padx=5, pady=5)
text_area.focus()

timer_label = Label(textvariable=str(timer))
timer_label.grid(column=1, row=1, padx=5, pady=5)

start()

tkinter.mainloop()
