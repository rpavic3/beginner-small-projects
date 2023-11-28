from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.geometry('300x200')

def gett():
    Label(root, text=pw_entry.get()).pack()

password = StringVar()

pw_entry = Entry(root, textvariable = password, show="*")
pw_entry.pack()

buton = Button(root, text="clik", command=gett).pack()

root.mainloop()
