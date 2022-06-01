from tkinter import *

num1 = 0
num2 = 0
op = ''

def btn_click(val):
    global num1, num2, op
    if val == 'c':
        display.delete(0, END)
    elif val == '+' or val == '-' or val == '*' or val == '/':
        num1 = float(display.get())
        op = val
        display.delete(0, END)
    elif val == '=':
        num2 = float(display.get())
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        
        display.delete(0, END)
        display.insert(END, result)
    else:
        display.insert(END, val)


root = Tk()
root.title('Calculator')

display = Entry(root, font=('Arial', 24), width=12)
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# first row
btn7 = Button(root, text="7", height=3, width=6, command=lambda: btn_click(7))
btn7.grid(row=1, column=0)

btn8 = Button(root, text="8", height=3, width=6, command=lambda: btn_click(8))
btn8.grid(row=1, column=1)

btn9 = Button(root, text="9", height=3, width=6, command=lambda: btn_click(9))
btn9.grid(row=1, column=2)

btn_div = Button(root, text="/", height=3, width=6, command=lambda: btn_click('/'))
btn_div.grid(row=1, column=3)


# second row
btn4 = Button(root, text="4", height=3, width=6, command=lambda: btn_click(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", height=3, width=6, command=lambda: btn_click(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, text="6", height=3, width=6, command=lambda: btn_click(6))
btn6.grid(row=2, column=2)

btn_mul = Button(root, text="x", height=3, width=6, command=lambda: btn_click('*'))
btn_mul.grid(row=2, column=3)


# third row
btn1 = Button(root, text="1", height=3, width=6, command=lambda: btn_click(1))
btn1.grid(row=3, column=0)

btn2 = Button(root, text="2", height=3, width=6, command=lambda: btn_click(2))
btn2.grid(row=3, column=1)

btn3 = Button(root, text="3", height=3, width=6, command=lambda: btn_click(3))
btn3.grid(row=3, column=2)

btn_sub = Button(root, text="-", height=3, width=6, command=lambda: btn_click('-'))
btn_sub.grid(row=3, column=3)

# fourth row
btnc = Button(root, text="C", height=3, width=6, command=lambda: btn_click('c'))
btnc.grid(row=4, column=0)

btn0 = Button(root, text="0", height=3, width=6, command=lambda: btn_click(0))
btn0.grid(row=4, column=1)

btn_eq = Button(root, text="=", height=3, width=6, command=lambda: btn_click('='))
btn_eq.grid(row=4, column=2)

btn_add = Button(root, text="+", height=3, width=6, command=lambda: btn_click('+'))
btn_add.grid(row=4, column=3)


# . backspace +/- % 

root.mainloop()