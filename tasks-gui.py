import webbrowser as wb
import hashlib
from tkinter import *
import sys


def command1(event):
    # hashvalue = str('4b9e36a08ab8a88d361639c95cdaae8238bca5de5fbd8094595c655827bb64c8')
    # password = hashlib.sha256(hashvalue.encode('utf8')).hexdigest()
    # print(password)
    if entry1.get() == 'Danny' and entry2.get() == '123456':
        root.deiconify()
        top.destroy()
        return True


def command2():
    top.destroy()
    root.destroy()
    sys.exit()


root = Tk()
top = Toplevel()
top.geometry('300x260')
top.title('LOGIN SCREEN')
top.configure(background='white')
photo2 = PhotoImage(file='lock.png')
photo = Label(top, image=photo2, bg='white')
lbl1 = Label(top, text='Username:', font={'Helvetica', 10})
entry1 = Entry(top)
lbl2 = Label(top, text='Password:', font={'Helvetica', 10})
entry2 = Entry(top, show="*")
button2 = Button(top, text='cancel', command=lambda: command2())
lbl3 = Label(top, text='Copyright to Wh0am3y3 2019', font={'Arial', 9})
entry2.bind('<Return>', command1)

photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()

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

root.title('main screen')
root.geometry('400x200')
root.withdraw()
root.mainloop()
