from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk
from tkinter import colorchooser


root=Tk()
root.title("Textitor™")
root.iconbitmap("todoist.ico")
root.geometry("1200x690")
root.resizable(False, False)

#root.config(background="#4a5758")

global open_status_name
open_status_name = False

global selected
selected = False

#create new file function
def new_file():
	#delete previous text
	my_text.delete("1.0", END)
	#update status bars
	root.title("New File")
	status_bar.config(text="New File        ")

	global open_status_name
	open_status_name = False

def open_file():
	#delete previous text
	my_text.delete("1.0", END)
	#grab filename
	text_file = filedialog.askopenfilename(initialdir="d:/Programming/My Python projects/text editor", title="Open File", filetypes=(("Text Files", "*.txt"),("HTML Files", "*.html"),("Python Files", "*.py"),("All Files", "*.*")))
	#check to see if there is file name
	if text_file:
		#make filename global so we can access it later
		global open_status_name
		open_status_name = text_file
	# update status bars
	name = text_file
	status_bar.config(text=f"{name}")
	name = name.replace("d:/Programming/My Python projects/text editor/", "")
	root.title(f"{name} - Editor")

	#open the file
	text_file = open(text_file, "r")
	stuff = text_file.read()
	#add file to text box
	my_text.insert(END, stuff)
	#close the opened file
	text_file.close()

def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="d:/Programming/My Python projects/", title ="Save File", filetypes=(("Text Files","*.txt"),("HTML Files", "*.html"),("Python Files", "*.py"),("All Files", "*.*")))
	if text_file:
		#upadte status bars
		name = text_file
		status_bar.config(text=f"Saved: {name}        ")
		name = name.replace("d:/Programming/My Python projects/", "")
		root.title(f"{name} - Editor")

		#save the file
		text_file = open(text_file, "w")
		text_file.write(my_text.get("1.0", END))
		#close the file
		text_file.close()


def save_file():
	global open_status_name
	if open_status_name:
		text_file = open(open_status_name, "w")
		text_file.write(my_text.get("1.0", END))
		text_file.close()

		status_bar.config(text=f"Saved: {open_status_name}        ")
	else:
		save_as_file()

def cut_text(e):
	global selected
	#check to see if keyboard shortcut used
	if e:
		selected = root.clipboard_get()
	else:
		if my_text.selection_get():
			# grab selected text from text box
			selected = my_text.selection_get()
			# delete that text bcuz we're cutting
			my_text.delete("sel.first", "sel.last")
			root.clipboard_clear()
			root.clipboard_append(selected)


def copy_text(e):
	global selected
	#check to see if we used keyboard shortcuts
	if e:
		selected = root.clipboard_get()


	if my_text.selection_get():
		selected = my_text.selection_get()
		root.clipboard_clear()
		root.clipboard_append(selected)

def paste_text(e):
	global selected
	#check to see if keyboard shortcut used
	if e:
		selected = root.clipboard_get()
	else:
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position, selected)

def bold_it():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	my_text.tag_configure("bold", font=bold_font)

	#define current tags
	current_tags = my_text.tag_names("sel.first")
	# if statement to see if tag has been set
	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		my_text.tag_add("bold", "sel.first", "sel.last")

def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	my_text.tag_configure("italic", font=italics_font)

	#define current tags
	current_tags = my_text.tag_names("sel.first")
	# if statement to see if tag has been set
	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		my_text.tag_add("italic", "sel.first", "sel.last")

#change selected text color
def text_color():
	#pick a color
	my_color=colorchooser.askcolor()[1]
	if my_color:
		status_bar.config(text=my_color)


		color_font = font.Font(my_text, my_text.cget("font"))
		color_font.configure(slant="italic")

		my_text.tag_configure("colored", font=color_font, foreground=my_color)

		#define current tags
		current_tags = my_text.tag_names("sel.first")
		# if statement to see if tag has been set
		if "colored" in current_tags:
			my_text.tag_remove("colored", "sel.first", "sel.last")
		else:
			my_text.tag_add("colored", "sel.first", "sel.last")

#change bg color
def bg_color():
	my_color=colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

#change ALL text color
def all_text_color():
	my_color=colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)

def font_size(dir):
	if dir=="increase":
		font1[1] = font1[1]+1
	elif dir=="decrease":
		font1[1] = font1[1]-1
	my_text.config(font=font1)


# create toolbar
toolbar_frame = Frame(root, background="#474747")
toolbar_frame.pack(fill=X)


my_frame = Frame(root, width=1920, height=1280)
my_frame.pack()
my_frame.pack_propagate(0)




#scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

font1 = ["Bahnschrift", 12]

my_text = Text(my_frame, width=1, height=1, font=font1, selectbackground="#7a7ad8", selectforeground="#eeeeee", undo=True, yscrollcommand=text_scroll.set, background="#61615f", foreground="white")
my_text.pack(fill=BOTH, expand=True)




text_scroll.config(command=my_text.yview)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)




#add file menu
file_menu = Menu(my_menu, tearoff=False, activebackground="#2a4747")
my_menu.add_cascade(label="File", menu=file_menu, activebackground="#2a4747")
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#add edit menu
edit_menu = Menu(my_menu, tearoff=False, activebackground="#2a4747")
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="<ctrl+x>")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="<ctrl+c>")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="<ctrl+v>")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="<ctrl+z>")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="<ctrl+y>")

#add color menu
color_menu = Menu(my_menu, tearoff=False, activebackground="#2a4747")
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected text", command=text_color)
color_menu.add_command(label="All text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

#status bar to bottom
status_bar = ttk.Label(my_frame, text="Ready        ", anchor=E, relief=SUNKEN, background="#d2b746", foreground="black")
status_bar.pack(fill=X, side=BOTTOM, ipady=5, ipadx=2, padx=2, pady=(1,3))


#edit bindings
root.bind("<Control-x>", cut_text)
root.bind("<Control-c>", copy_text)
root.bind("<Control-v>", paste_text)

bold_button = Button(toolbar_frame, text="Bold", command=bold_it, background="#d2b746", foreground="#565656", font=["Bahnschrift", 11, "bold"])
bold_button.grid(row=0, column=0, sticky=W, padx=(3.2,1))


italics_button = Button(toolbar_frame, text="Italics", command=italics_it, background="#d2b746", foreground="#565656", font=["Bahnschrift", 11, "bold"])
italics_button.grid(row=0, column=1)

#text color
color_text_button = Button(toolbar_frame, text= "Text Color", command=text_color, background="#d2b746", foreground="#565656", font=["Bahnschrift", 11, "bold"])
color_text_button.grid(row=0, column=4, padx=1)

#font size
size_plus_button = Button(toolbar_frame, text="Font +", command=lambda: font_size("increase"), background="#d2b746", foreground="#565656", font=["Bahnschrift", 11, "bold"])
size_plus_button.grid(row=0, column=5, padx=1)
size_minus_button = Button(toolbar_frame, text="Font -", command=lambda: font_size("decrease"), background="#d2b746", foreground="#565656", font=["Bahnschrift", 11, "bold"])
size_minus_button.grid(row=0, column=6, padx=1)







root.mainloop()