from tkinter import *
from tkinter import ttk

root = Tk()
root.title('My Window')
root.geometry('500x500')
root.resizable(False, False)

label_un = Label(root, text='Username')
label_un.grid(row=0, column=0)

entry_un = Entry(root)
entry_un.grid(row=0, column=1)

label_pw = Label(root, text='Password')
label_pw.grid(row=1, column=0)

entry_pw = Entry(root, show='*')
entry_pw.grid(row=1, column=1)

label_co = Label(root, text='Country')
label_co.grid(row=2, column=0)

combo_co = ttk.Combobox(root, values=('Nepal', 'India', 'China', 'UK', 'USA'), 
                    state="readonly", width=17)
combo_co.set('Nepal')
combo_co.grid(row=2, column=1)

label_gen = Label(root, text='Gender')
label_gen.grid(row=3, column=0)

frame_gen = Frame(root)
frame_gen.grid(row=3, column=1)

radio_m = ttk.Radiobutton(frame_gen, text="Male")
radio_m.grid(row=0, column=1)

radio_f = ttk.Radiobutton(frame_gen, text="Female")
radio_f.grid(row=0, column=2)

radio_o = ttk.Radiobutton(frame_gen, text="Other")
radio_o.grid(row=0, column=3)

label_hob = Label(root, text='Hobbies')
label_hob.grid(row=4, column=0)

frame_hob = Frame(root)
frame_hob.grid(row=4, column=1)

radio_m = ttk.Checkbutton(frame_hob, text="Music")
radio_m.grid(row=0, column=1)

radio_f = ttk.Checkbutton(frame_hob, text="Travel")
radio_f.grid(row=0, column=2)

radio_o = ttk.Checkbutton(frame_hob, text="Other")
radio_o.grid(row=0, column=3)

label_cmt = Label(root, text='Comment')
label_cmt.grid(row=5, column=0)

text_cmt = Text(root, height=5, width=17)
text_cmt.grid(row=5, column=1)

btn_login = Button(root, text='Login')
btn_login.grid(row=6, column=0)

btn_reg = Button(root, text='Register')
btn_reg.grid(row=6, column=1)

# label.place(x=50, y=50)
# label.pack(side='right')

# Label(root, text="Test").place(x=60, y=70)
# Label(root, text="Test").grid(row=0, column=1)
# Label(root, text="Test").pack(side='left')


root.mainloop()

