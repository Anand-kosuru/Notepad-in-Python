from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Notepad')
root.geometry('450x350')
file_path = ""

def set_file_path(path):
    global file_path
    file_path = path

yscrollbar = Scrollbar(root)
yscrollbar.pack(side="right", fill='y')

xscrollbar = Scrollbar(root, orient=HORIZONTAL)
xscrollbar.pack(side="bottom", fill='x')

editor= Text(width=450, height=350, font=('aerial', 20, 'bold'), wrap="none",yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
editor.pack()

yscrollbar.config(command=editor.yview)
xscrollbar.config(command=editor.xview)

def new_file():
    global editor
    code = editor.get(1.0, END)
    editor.delete(1.0, END)

def openfile():
    path = filedialog.askopenfilename(filetypes=[('text files', '*.txt'), ('Python files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        set_file_path(path)

def save_file():
    if file_path == '':
        path = filedialog.asksaveasfilename(filetypes=[('Text files', '*.txt'), ('Python files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get(1.0, END)
        file.write(code)
        set_file_path(path)

def copy():
    editor.event_generate('<<Copy>>')

def cut():
    editor.event_generate('<<Cut>>')

def paste():
    editor.event_generate('<<Paste>>')

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=openfile)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit')
menu_bar.add_cascade(label='File', menu=file_menu)
root.config(menu=menu_bar)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
root.config(menu=menu_bar)
root.mainloop()
