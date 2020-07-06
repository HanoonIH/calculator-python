# import all from tKinter for GUI
from tkinter import *

# global variable, entered values are stored in this variable then calculated by the eval function
operator = ""


def error():
    error_msg = "Error"
    calc_input.set(error_msg)


# function for adding entered values to the global variable 'operator' as a string
def btn_click(numbers):
    # introducing globally declared 'operator' to this function
    global operator

    # concatenate entering values to global 'operator'
    operator = operator + str(numbers)

    # update value of 'operator' and show it on calculator display
    calc_input.set(operator)


# function for delete the last entered value from the string 'operator'
def backspace():
    global operator

    # delete the last entered value from the string 'operator' and update it.
    operator = operator[:-1]
    calc_input.set(operator)


# function for clear all values from 'operator' / display
def btn_clear_display():
    global operator

    # change value of string 'operator' to "" (clear all) and update it.
    operator = ""
    calc_input.set(operator)


# function for calculating the values of 'operator' using a built-in function 'eval()'
def btn_equals():
    global operator

    # calculate the values of string by using 'eval' function
    sum_ans = str(eval(operator))
    calc_input.set(sum_ans)

    # to clear all from 'operator' , after a calculation is done.
    # operator = ""

    # to store the answer to 'operator' , and continue calculation.
    operator = sum_ans


# create a gui window for calculator.
calculator = Tk()

# give a title to the window.
calculator.title("python Calculator")

# create a variable to store entering values,
# and make it a string variable using 'StringVar' method.
calc_input = StringVar()

# import images for use as buttons
img_1 = PhotoImage(file='images/1.png')
img_2 = PhotoImage(file='images/2.png')
img_3 = PhotoImage(file='images/3.png')
img_4 = PhotoImage(file='images/4.png')
img_5 = PhotoImage(file='images/5.png')
img_6 = PhotoImage(file='images/6.png')
img_7 = PhotoImage(file='images/7.png')
img_8 = PhotoImage(file='images/8.png')
img_9 = PhotoImage(file='images/9.png')
img_0 = PhotoImage(file='images/0.png')
img_dot = PhotoImage(file='images/dot.png')
img_eq = PhotoImage(file='images/equal.png')
img_per = PhotoImage(file='images/per.png')
img_ac = PhotoImage(file='images/ac.png')
img_c = PhotoImage(file='images/c.png')
img_add = PhotoImage(file='images/plus.png')
img_sub = PhotoImage(file='images/sub.png')
img_div = PhotoImage(file='images/div.png')
img_mult = PhotoImage(file='images/x.png')
img_sq = PhotoImage(file='images/square.png')

# create a display for calculator using Entry widget and show variable 'calc_input' on it.
# customizing calculator display
calc_display = Entry(
                     calculator,
                     font=("arial", 40, "bold"),
                     textvariable=calc_input,
                     border=0,
                     width=13,
                     justify="right"
                    )
calc_display.grid(columnspan=4)
calc_display.config(highlightthickness=5)
calc_display.config(highlightbackground="black")

# Number & Operator Buttons
###########################

# all clear, backspace, %, x
# create a Button widget, set an image as the button, pass a command to a defined function using lambda function
btn_ac = Button(calculator, border=0, image=img_ac, command=lambda: btn_clear_display())
#  set the position of button on the grid
btn_ac.grid(row=1, column=0)

btn_clr = Button(calculator, border=0, image=img_c, command=lambda: backspace())
btn_clr.grid(row=1, column=1)

btn_percentage = Button(calculator, border=0, image=img_per, command=lambda: btn_click("%"))
btn_percentage.grid(row=1, column=2)

btn_mult = Button(calculator, border=0, image=img_mult, command=lambda: btn_click("*"))
btn_mult.grid(row=1, column=3)

# 7, 8, 9, /
btn_7 = Button(calculator, border=0, image=img_7, command=lambda: btn_click(7))
btn_7.grid(row=2, column=0)

btn_8 = Button(calculator, border=0, image=img_8, command=lambda: btn_click(8))
btn_8.grid(row=2, column=1)

btn_9 = Button(calculator, border=0, image=img_9, command=lambda: btn_click(9))
btn_9.grid(row=2, column=2)

btn_div = Button(calculator, border=0, image=img_div, command=lambda: btn_click("/"))
btn_div.grid(row=2, column=3)

# 4, 5, 6, -
btn_4 = Button(calculator, border=0, image=img_4, command=lambda: btn_click(4))
btn_4.grid(row=3, column=0)

btn_5 = Button(calculator, border=0, image=img_5, command=lambda: btn_click(5))
btn_5.grid(row=3, column=1)

btn_6 = Button(calculator, border=0, image=img_6, command=lambda: btn_click(6))
btn_6.grid(row=3, column=2)

btn_sub = Button(calculator, border=0, image=img_sub, command=lambda: btn_click("-"))
btn_sub.grid(row=3, column=3)

# 1, 2, 3, +
btn_1 = Button(calculator, border=0, image=img_1, command=lambda: btn_click(1))
btn_1.grid(row=4, column=0)

btn_2 = Button(calculator, border=0, image=img_2, command=lambda: btn_click(2))
btn_2.grid(row=4, column=1)

btn_3 = Button(calculator, border=0, image=img_3, command=lambda: btn_click(3))
btn_3.grid(row=4, column=2)

btn_add = Button(calculator, border=0, image=img_add, command=lambda: btn_click("+"))
btn_add.grid(row=4, column=3)

# dot, 0, square, =
btn_0 = Button(calculator, border=0, image=img_0, command=lambda: btn_click(0))
btn_0.grid(row=5, column=0)

btn_dot = Button(calculator, border=0, image=img_dot, command=lambda: btn_click("."))
btn_dot.grid(row=5, column=1)

btn_square = Button(calculator, border=0, image=img_sq, command=lambda: btn_click("**2"))
btn_square.grid(row=5, column=2)

btn_equal = Button(calculator, border=0, image=img_eq, command=lambda: btn_equals())
btn_equal.grid(row=5, column=3)

calculator.mainloop()
