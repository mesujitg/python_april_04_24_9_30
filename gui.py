from tkinter import *


def on_btn_click():
    un = entry_un.get()
    print(un)

root = Tk()
root.title('My Window')
# root.geometry('500x500')
root.resizable(False, False)

label = Label(root, text='Hello There', foreground='blue', background='red', 
                font=('Arial', 20))
# grid, place, pack
label.grid(row=0, column=0, columnspan=2)

label_un = Label(root, text="Username", padx=10, pady=10)
label_un.grid(row=1, column=0)

entry_un = Entry(root)
entry_un.grid(row=1, column=1, padx=10, pady=10)

label_pw = Label(root, text='Password')
label_pw.grid(row=2, column=0)

entry_pw = Entry(root, show='*')
entry_pw.grid(row=2, column=1)

btn_login = Button(root, text='Login', command=on_btn_click)
btn_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
