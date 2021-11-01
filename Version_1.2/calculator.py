#Kalkylator project
from tkinter import*

## main
window = Tk()

#title
window.title("Kalkylator")

#width and height
window.geometry("355x465")

#bg=background, background color
window.configure(bg="#33C4FF")

#icon from https://www.flaticon.com/ -- convert .png to .ico on https://icoconvert.com/
window.iconbitmap(r'calc.ico')

#the first false stands for width and the second height - so you cant rezise the window
window.resizable(False,False)


##functions

#press function
expression = ""
def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

#equalpress function
def equalpress():
    global expression

    try:
        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:
        equation.set("error")
        expression = ""

#clear function
def clear():
    global expression

    expression = ""
    equation.set("0")


#buttons
button_frame = Frame(window,bg="#33C4FF")
button_frame.pack()

equation = StringVar()
equation.set("0")
expression_field = Entry(button_frame,textvariable=equation,
                         justify="right",font=("arial",20,"bold"))

button1 = Button(button_frame,text="1",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(1))

button1 = Button(button_frame,text="1",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(1))

button2 = Button(button_frame,text="2",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(2))

button3 = Button(button_frame,text="3",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(3))

addition = Button(button_frame,text="+",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press("+"))

button4 = Button(button_frame,text="4",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(4))

button5 = Button(button_frame,text="5",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(5))

button6 = Button(button_frame,text="6",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(6))

subtract = Button(button_frame,text="-",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press("-"))

button7 = Button(button_frame,text="7",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(7))

button8 = Button(button_frame,text="8",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(8))

button9 = Button(button_frame,text="9",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(9))

multiply = Button(button_frame,text="*",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press("*"))

button0 = Button(button_frame,text="0",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press(0))

decimal = Button(button_frame,text=".",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press("."))

clear = Button(button_frame,text="C",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=clear)

division = Button(button_frame,text="/",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=8,height=3,command=lambda:press("/"))

equal = Button(button_frame,text="=",font=("times new roman",12),relief="ridge",
                 borderwidth=1,bg="#6CDBFF",width=35,height=3,command=equalpress)

expression_field.grid(row=0,column=0,columnspan=4,ipadx=10,ipady=22,pady=15)

#first row
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
addition.grid(row=1,column=3)

#second row
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
subtract.grid(row=2,column=3)

#third row
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
multiply.grid(row=3,column=3)

#fourth row
button0.grid(row=4,column=0)
decimal.grid(row=4,column=1)
clear.grid(row=4,column=2)
division.grid(row=4,column=3)

#row five
equal.grid(row=5,column=0,columnspan=4)



## run the main loop
window.mainloop()