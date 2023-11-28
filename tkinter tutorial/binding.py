from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.geometry("650x450")
def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)

def bog(event):
    print("gay")



btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>', log, add="+")
btn.bind("<KeyRelease-A>", bog)



btn.focus()
btn.pack(expand=True)
root.mainloop()
