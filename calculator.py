from tkinter import *


class Calculator:
    def __init__(self) -> None:
        self.num1 = 0
        self.num2 = 0
        self.op = ''

        self.root = Tk()
        self.root.title('Calculator')

        self.display = Entry(self.root, font=('Arial', 24), width=12, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

        # first row
        self.btn7 = Button(self.root, text="7", height=3, width=6, command=lambda: self.btn_click(7))
        self.btn7.grid(row=1, column=0)

        self.btn8 = Button(self.root, text="8", height=3, width=6, command=lambda: self.btn_click(8))
        self.btn8.grid(row=1, column=1)

        self.btn9 = Button(self.root, text="9", height=3, width=6, command=lambda: self.btn_click(9))
        self.btn9.grid(row=1, column=2)

        self.btn_div = Button(self.root, text="/", height=3, width=6, command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=1, column=3)


        # second row
        self.btn4 = Button(self.root, text="4", height=3, width=6, command=lambda: self.btn_click(4))
        self.btn4.grid(row=2, column=0)

        self.btn5 = Button(self.root, text="5", height=3, width=6, command=lambda: self.btn_click(5))
        self.btn5.grid(row=2, column=1)

        self.btn6 = Button(self.root, text="6", height=3, width=6, command=lambda: self.btn_click(6))
        self.btn6.grid(row=2, column=2)

        self.btn_mul = Button(self.root, text="x", height=3, width=6, command=lambda: self.btn_click('*'))
        self.btn_mul.grid(row=2, column=3)


        # third row
        self.btn1 = Button(self.root, text="1", height=3, width=6, command=lambda: self.btn_click(1))
        self.btn1.grid(row=3, column=0)

        self.btn2 = Button(self.root, text="2", height=3, width=6, command=lambda: self.btn_click(2))
        self.btn2.grid(row=3, column=1)

        self.btn3 = Button(self.root, text="3", height=3, width=6, command=lambda: self.btn_click(3))
        self.btn3.grid(row=3, column=2)

        self.btn_sub = Button(self.root, text="-", height=3, width=6, command=lambda: self.btn_click('-'))
        self.btn_sub.grid(row=3, column=3)

        # fourth row
        self.btnc = Button(self.root, text="C", height=3, width=6, command=lambda: self.btn_click('c'))
        self.btnc.grid(row=4, column=0)

        self.btn0 = Button(self.root, text="0", height=3, width=6, command=lambda: self.btn_click(0))
        self.btn0.grid(row=4, column=1)

        self.btn_eq = Button(self.root, text="=", height=3, width=6, command=lambda: self.btn_click('='))
        self.btn_eq.grid(row=4, column=2)

        self.btn_add = Button(self.root, text="+", height=3, width=6, command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=4, column=3)

        # . backspace +/- % 
        self.btnsign = Button(self.root, text="+/-", height=3, width=6, command=lambda: self.btn_click('+/-'))
        self.btnsign.grid(row=5, column=0)

        self.btndot = Button(self.root, text=".", height=3, width=6, command=lambda: self.btn_click('.'))
        self.btndot.grid(row=5, column=1)

        self.btn_bs = Button(self.root, text="x <=", height=3, width=6, command=lambda: self.btn_click('bs'))
        self.btn_bs.grid(row=5, column=2)

        self.btn_p = Button(self.root, text="%", height=3, width=6, command=lambda: self.btn_click('%'))
        self.btn_p.grid(row=5, column=3)

        self.root.mainloop()

    def btn_click(self, val):
        if val == 'c':
            self.display.delete(0, END)
        elif val == '+' or val == '-' or val == '*' or val == '/':
            self.num1 = float(self.display.get())
            self.op = val
            self.display.delete(0, END)
        elif val == '=':
            self.num2 = float(self.display.get())
            self.display.delete(0, END)
            self.display.insert(END, self.calculate())
        elif val == '+/-':
            num = self.display.get()
            if num[0] == '-':
                self.display.delete(0)
            else:
                self.display.insert(0, '-')
        else:
            self.display.insert(END, val)

    def calculate(self):
        if self.op == '+':
            result = self.num1 + self.num2
        elif self.op == '-':
            result = self.num1 - self.num2
        elif self.op == '*':
            result = self.num1 * self.num2
        elif self.op == '/':
            result = self.num1 / self.num2
        return result

Calculator()