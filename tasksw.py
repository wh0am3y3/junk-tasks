#!/usr/bin/env python
import hashlib
import webbrowser as wb
from tkinter import *
import sys


def login_screen():
    # fnames = ['Danny']
    # hashvalue = str('4b9e36a08ab8a88d361639c95cdaae8238bca5de5fbd8094595c655827bb64c8').encode('utf8')
    # if entry1.get() == fnames[0]:
    #     if entry2.get() == hashlib.sha256(str(hashvalue)).hexdigest():
    #         print('password correct')
    #         root.deiconify()
    #         top.destroy()

    if entry1.get() == "Danny" and entry2.get() == "pass":
        print('Password correct')
        root.deiconify()
        top.destroy()
        return True



def exit_window():
    top.destroy()
    root.destroy()
    sys.exit()


root = Tk()
top = Toplevel()

top.geometry('300x260')
top.title('LOGIN SCREEN')
top.configure(background='white')
label1 = Label(top, text='Username: ', font=('Helvetica', 10))
entry1 = Entry(top)
label2 = Label(top, text='Password: ', font=('Helvetica', 10))
entry2 = Entry(top, show="*")
button2 = Button(top, text='Cancel', command=lambda:exit_window())

entry2.bind('<Return>', login_screen)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button2.pack()

if login_screen() is True:
    root.title('Main Screen')
    root.configure(background='white')
    root.geometry('170x80')


OPTIONS = [
    "Favorites",
    "Option 2",
    "Option 3",
    "Option 4",
    "Exit"
]

variable = StringVar(root)
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
w.pack()


def ok():
    if variable.get() == OPTIONS[0]:
        print("Opening favorites!")
        with open('urls.txt') as f:
            for i in f.read().splitlines():
                wb.open_new_tab(i)
    elif variable.get() == OPTIONS[-1]:
        exit(0)


button = Button(root, text="OK", command=ok)
button.pack()

mainloop()
