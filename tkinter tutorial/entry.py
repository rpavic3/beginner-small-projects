from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.geometry('300x200')

def gett():
    mylab = Label(root, text=textbox.get()).pack()


textbox = ttk.Entry(root)
textbox.pack()
textbox.focus()
buton = Button(root, text="click", command=gett).pack()

root.mainloop()
