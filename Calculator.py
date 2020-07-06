from tkinter import *

from tkinter import messagebox


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    calcInput.set(operator)

def backspace():
    global operator
    operator = operator[:-1]
    calcInput.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    calcInput.set(operator)


def btnEquals():
    global operator
    sum = str(eval(operator))
    calcInput.set(sum)
    operator = ""


calculator = Tk()
calculator.title("python Calculator")
operator = ""
calcInput = StringVar()

img1 = PhotoImage(file='images/1.png')
img2 = PhotoImage(file='images/2.png')
img3 = PhotoImage(file='images/3.png')
img4 = PhotoImage(file='images/4.png')
img5 = PhotoImage(file='images/5.png')
img6 = PhotoImage(file='images/6.png')
img7 = PhotoImage(file='images/7.png')
img8 = PhotoImage(file='images/8.png')
img9 = PhotoImage(file='images/9.png')
img0 = PhotoImage(file='images/0.png')
imgdot = PhotoImage(file='images/dot.png')
imgeq = PhotoImage(file='images/equal.png')
imgper = PhotoImage(file='images/per.png')
imgac = PhotoImage(file='images/ac.png')
imgc = PhotoImage(file='images/c.png')
imgadd = PhotoImage(file='images/plus.png')
imgsub = PhotoImage(file='images/sub.png')
imgdiv = PhotoImage(file='images/div.png')
imgmult = PhotoImage(file='images/x.png')
imgsq = PhotoImage(file='images/square.png')

calcDisplay = Entry(calculator, font=("arial", 40, "bold"), textvariable=calcInput, border=0,
                    width=13, justify="right")
calcDisplay.grid(columnspan=4)
calcDisplay.config(highlightthickness=5)
calcDisplay.config(highlightbackground="black")

# Number & Operator Keys
# ac,c,%,x
btnac = Button(calculator, border=0, image=imgac, command=lambda: btnClearDisplay())
btnac.grid(row=1, column=0)

btnClr = Button(calculator, border=0, image=imgc, command=lambda: backspace())
btnClr.grid(row=1, column=1)

btn_percentage = Button(calculator, border=0, image=imgper, command=lambda: btnClick())
btn_percentage.grid(row=1, column=2)

btnMult = Button(calculator, border=0, image=imgmult, command=lambda: btnClick("*"))
btnMult.grid(row=1, column=3)

# 7,8,9,+
# btn7 = Button(calculator, padx=16, fg="#181818", bd=5, font=("arial", 30, "bold"), text="7",
#               command=lambda: btnClick(7))
btn7 = Button(calculator, border=0, image=img7, command=lambda: btnClick(7))
btn7.grid(row=2, column=0)

btn8 = Button(calculator, border=0, image=img8, command=lambda: btnClick(8))
btn8.grid(row=2, column=1)

btn9 = Button(calculator, border=0, image=img9, command=lambda: btnClick(9))
btn9.grid(row=2, column=2)

btnDiv = Button(calculator, border=0, image=imgdiv, command=lambda: btnClick("/"))
btnDiv.grid(row=2, column=3)

# 4,5,6,-
btn4 = Button(calculator, border=0, image=img4, command=lambda: btnClick(4))
btn4.grid(row=3, column=0)

btn5 = Button(calculator, border=0, image=img5, command=lambda: btnClick(5))
btn5.grid(row=3, column=1)

btn6 = Button(calculator, border=0, image=img6, command=lambda: btnClick(6))
btn6.grid(row=3, column=2)

btnSubs = Button(calculator, border=0, image=imgsub, command=lambda: btnClick("-"))
btnSubs.grid(row=3, column=3)

# 1,2,3,x
btn1 = Button(calculator, border=0, image=img1, command=lambda: btnClick(1))
btn1.grid(row=4, column=0)

btn2 = Button(calculator, border=0, image=img2, command=lambda: btnClick(2))
btn2.grid(row=4, column=1)

btn3 = Button(calculator, border=0, image=img3, command=lambda: btnClick(3))
btn3.grid(row=4, column=2)

btnAdd = Button(calculator, border=0, image=imgadd, command=lambda: btnClick("+"))
btnAdd.grid(row=4, column=3)

# .,0,equal
btn0 = Button(calculator, border=0, image=img0, command=lambda: btnClick(0))
btn0.grid(row=5, column=0)

btnDot = Button(calculator, border=0, image=imgdot, command=lambda: btnClick("."))
btnDot.grid(row=5, column=1)

btn_sq = Button(calculator, border=0, image=imgsq, command=lambda: btnClick("**2"))
btn_sq.grid(row=5, column=2)

btnEq = Button(calculator, border=0, image=imgeq, command=lambda: btnEquals())
btnEq.grid(row=5, column=3)

calculator.mainloop()


