from tkinter import *

users = [
    {'name':'bigyan', 'username':'bigyan', 'password':'12345', 'balance':125000},
    {'name':'bini', 'username':'bini', 'password':'11111', 'balance':75000},
    {'name':'bhoomiksha', 'username':'bhoomi', 'password':'54321', 'balance':100000},
    {'name':'arpana', 'username':'arpana', 'password':'22222', 'balance':90000},
    {'name':'deepak', 'username':'deepak', 'password':'deepak1', 'balance':215000},
    ]


def withdraw():
    amt = amount.get()
    users[user_index]['balance'] = users[user_index]['balance'] - amt
    print(users[user_index]['balance'])

def deposite():
    global user_index
    amt = amount.get()
    users[user_index]['balance'] = users[user_index]['balance'] + amt
    print(users[user_index]['balance'])


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
            global user_index
            user_index = users.index(user)
            print('aa', user_index)
            root.destroy()

            root1 = Tk()
            root1.title('Dashboard')
            root1.geometry('300x300')

            global amount
            amount = IntVar()

            label_msg = Label(root1, text=f'Welcome { user["name"] }', font=('Arial', 18))
            label_msg.grid(row=0, column=0, padx=20)

            label_bal = Label(root1, text=f'You balance is: { user["balance"] }', font=('Arial', 18))
            label_bal.grid(row=1, column=0, padx=20)

            entry_amt = Entry(root1, textvariable=amount)
            entry_amt.grid(row=2, column=0, padx=20)

            btn_w = Button(root1, text="Withdraw", command=withdraw)
            btn_w.grid(row=3, column=0, padx=20, pady=10)

            btn_d = Button(root1, text="Deposite", command=deposite)
            btn_d.grid(row=4, column=0, padx=20, pady=10)

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