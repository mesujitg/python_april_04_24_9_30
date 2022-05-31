from tkinter import *


users = [
    {'name':'bigyan', 'username':'bigyan', 'password':'12345', 'balance':125000},
    {'name':'bini', 'username':'bini', 'password':'11111', 'balance':75000},
    {'name':'bhoomiksha', 'username':'bhoomi', 'password':'54321', 'balance':100000},
    {'name':'arpana', 'username':'arpana', 'password':'22222', 'balance':90000},
    {'name':'deepak', 'username':'deepak', 'password':'deepak1', 'balance':215000},
    ]


def login():
    # un = entry_un.get()
    # pw = entry_pw.get()
    un = username.get()
    pw = password.get()
    
    for user in users:
        if un==user['username'] and pw==user['password']:
            # print('Welcome ', user['name'])
            # print('You balance is: ', user['balance'])
            # label_msg.config(text=f'Welcome { user["name"] }', foreground='green')
            root.destroy()

            root1 = Tk()
            root1.title('Dashboard')
            root1.geometry('300x300')

            label_msg = Label(root1, text=f'Welcome { user["name"] }', font=('Arial', 18))
            label_msg.grid(row=0, column=0, padx=20)

            label_bal = Label(root1, text=f'You balance is: { user["balance"] }', font=('Arial', 18))
            label_bal.grid(row=1, column=0, padx=20)

            root1.mainloop()
            break
    else:
        # print('Wrong credentials')
        label_msg.config(text='Wrong credentials', foreground='red')


root = Tk()
root.title('User Login')
# root.geometry('500x500')
root.resizable(False, False)

username = StringVar()
password = StringVar()

label_un = Label(root, text='Username', padx=20, pady=20)
label_un.grid(row=0, column=0)

entry_un = Entry(root, textvariable=username)
entry_un.grid(row=0, column=1, padx=20, pady=20)

label_pw = Label(root, text='Password')
label_pw.grid(row=1, column=0)

entry_pw = Entry(root, show='*', textvariable=password)
entry_pw.grid(row=1, column=1)

btn_login = Button(root, text='Login', command=login)
btn_login.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

label_msg = Label(root, text='')
label_msg.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()