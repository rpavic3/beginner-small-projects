from tkinter import *


root = Tk()
root.geometry("600x400-700+300")
screen_width = root.winfo_screenwidth()

# place a label on the root window
message = Label(root, text="heeasyyasd")
message.pack()

root.resizable(False, False)
root.attributes('-alpha', 0.98)


# keep the window displaying
root.mainloop()