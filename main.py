import tkinter as tk
from tkinter import *

# declares a global variable
expression = ""


# functions for numbers, equal, and clearing out
# function for numbers
def btn_click(item):
    global expression

    # con of string
    expression = expression + str(item)

    # updates the expression
    input_text.set(expression)


# this clears the input field
def clear():
    global expression

    expression = ""

    input_text.set("")


# the equal button
def equal():
    global expression

    result = str(eval(expression))
    input_text.set(result)
    expression = ""


# designing UI of the calculator
ui = Tk()
# title
ui.title("Calculator")
# size
ui.geometry("450x750")
# prevents it from being resized
ui.resizable(False, False)
# background color of the calculator
ui.config(bg="Black")

# import StringVar() from tkinter, or use tk.StringVar()
# StringVar() holds string data - used for widgets like entry
input_text = StringVar()

# a box for the top half to display number selected
display = tk.Frame(ui, width=312, height=50, bg="Black", highlightbackground="Black", highlightcolor="Black",
                   highlightthickness=1)
display.pack(side="top")
# input field inside the frame
display = tk.Entry(display, font=('arial', 30), textvariable=input_text, width=30, bg="black", fg="white", bd=0,
                   justify='right',)
display.grid(row=0, column=0)
display.pack(padx=50, pady=75)

# frames for each row of buttons
top = tk.Frame(ui, bg="Black")
top.pack(padx=10, pady=1, anchor='center')

# buttons for each different functions + numbers
# lambda = used to define an anonymous functions in python
all_clear = tk.Button(ui, text="AC", bg="grey", width=10, height=5, command=lambda: clear())
all_clear.pack(padx=5, pady=5, in_=top, side='left')

neg_button = tk.Button(ui, text="-", bg="grey", width=10, height=5, command=lambda: btn_click("-"))
neg_button.pack(padx=5, pady=5, in_=top, side='left')

mod_button = tk.Button(ui, text="%", bg="grey", width=10, height=5, command=lambda: btn_click("%"))
mod_button.pack(padx=5, pady=5, in_=top, side='left')

division_button = tk.Button(ui, text="/", bg="orange", width=10, height=5, command=lambda: btn_click("/"))
division_button.pack(padx=5, pady=5, in_=top, side='left')

# frames for each row of buttons
top = tk.Frame(ui, bg="Black")
top.pack(padx=10, pady=1, anchor='center')

seven = tk.Button(ui, text="7", bg="grey", width=10, height=5, command=lambda: btn_click("7"))
seven.pack(padx=5, pady=5, in_=top, side='left')

eight = tk.Button(ui, text="8", bg="grey", width=10, height=5, command=lambda: btn_click("8"))
eight.pack(padx=5, pady=5, in_=top, side='left')

nine = tk.Button(ui, text="9", bg="grey", width=10, height=5, command=lambda: btn_click("9"))
nine.pack(padx=5, pady=5, in_=top, side='left')

multi_button = tk.Button(ui, text="x", bg="orange", width=10, height=5, command=lambda: btn_click("*"))
multi_button.pack(padx=5, pady=5, in_=top, side='left')

# frames for each row of buttons
top = tk.Frame(ui, bg="Black")
top.pack(padx=10, pady=1, anchor='center')

four = tk.Button(ui, text="4", bg="grey", width=10, height=5, command=lambda: btn_click("4"))
four.pack(padx=5, pady=5, in_=top, side='left')

five = tk.Button(ui, text="5", bg="grey", width=10, height=5, command=lambda: btn_click("5"))
five.pack(padx=5, pady=5, in_=top, side='left')

six = tk.Button(ui, text="6", bg="grey", width=10, height=5, command=lambda: btn_click("6"))
six.pack(padx=5, pady=5, in_=top, side='left')

sub_button = tk.Button(ui, text="-", bg="orange", width=10, height=5, command=lambda: btn_click("-"))
sub_button.pack(padx=5, pady=5, in_=top, side='left')

# frames for each row of buttons
top = tk.Frame(ui, bg="Black")
top.pack(padx=10, pady=1, anchor='center')

one = tk.Button(ui, text="1", bg="grey", width=10, height=5, command=lambda: btn_click("1"))
one.pack(padx=5,  pady=5, in_=top, side='left')

two = tk.Button(ui, text="2", bg="grey", width=10, height=5, command=lambda: btn_click("2"))
two.pack(padx=5, pady=5, in_=top, side='left')

three = tk.Button(ui, text="3", bg="grey", width=10, height=5, command=lambda: btn_click("3"))
three.pack(padx=5, pady=5, in_=top, side='left')

add_button = tk.Button(ui, text="+", bg="orange", width=10, height=5, command=lambda: btn_click("+"))
add_button.pack(padx=5, pady=5, in_=top, side='left')

# frames for each row of buttons
top = tk.Frame(ui, bg="Black")
top.pack(padx=10, pady=1, anchor='center')

zero = tk.Button(ui, text="0", bg="grey", width=23, height=5, command=lambda: btn_click("0"))
zero.pack(padx=5, pady=5, in_=top, side='left')

period = tk.Button(ui, text=".", bg="grey", width=10, height=5, command=lambda: btn_click("."))
period.pack(padx=5, pady=5, in_=top, side='left')

equals_button = tk.Button(ui, text="=", bg="orange", width=10, height=5, command=lambda: equal())
equals_button.pack(padx=5, pady=5, in_=top, side='left')


# this runs the UI
ui.mainloop()
