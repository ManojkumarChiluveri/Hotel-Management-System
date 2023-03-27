
from tkinter import *

import tkinter as tk

window = Tk()
#window.geometry("600x800")
window.title("school management")
# frame = Frame(window)
# frame.pack()



menu = Menu(window)
window.config(menu = menu)

filemenu =Menu(menu)
editmenu = Menu(menu)



menu.add_cascade(label="student",menu = filemenu)
menu.add_cascade(label="teacher",menu = editmenu)
menu.add_cascade(label="principle")


filemenu.add_command(label="New")
filemenu.add_command(label="open")
filemenu.add_command(label="save")


editmenu.add_command(label="copy")
editmenu.add_command(label="cut")
editmenu.add_command(label="paste")



window.mainloop()