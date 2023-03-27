# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:31:29 2022

@author: durga
"""

from tkinter import *

import tkinter as tk

#install PIL library
#pip install pillow

from PIL import ImageTk,Image


#from individual_registration_page import *

# =============================================================================
# dir(PIL)
# ['GimpGradientFile', 'GimpPaletteFile', 'Image',
#  'ImageChops', 'ImageColor', 'ImageFile', 'ImageMode', 'ImagePalette',
#  'ImageSequence', 'PaletteFile', 'PngImagePlugin', 'TiffTags',
#  'UnidentifiedImageError', '__builtins__',
#  '__cached__', '__doc__', '__file__', '__loader__',
#  '__name__', '__package__', '__path__', '__spec__', '__version__', 
#  '_binary', '_imaging', '_plugins', '_util']
# 
# =============================================================================

#functions for opening new windows
def registration():
    #registration_details()
    pass
  
    
    
def login():
    print("this should redirected to login window")

main_window = Tk()
main_window.geometry("1080x800")
main_window.title("School management system")


headingframe = Frame(main_window)
headingframe.place(x=0, y=0, width=1200, height=50)
Label(headingframe, text="School management system",font=("Times", "50", "bold italic"),background="blue").place()


#to separate the window into block/frame
frame1 = Frame(main_window, padx=80)
frame1.place(x=80, y=160, width=1200, height=300)


#reading the images from the folder
reg_image = ImageTk.PhotoImage(file ="registration.png")
login_image = ImageTk.PhotoImage(file ="login.png")
exit_image = ImageTk.PhotoImage(file ="exit.png")

#to display the image on the window
#registration image label
reg_image_label = Label(frame1,image= reg_image)
reg_image_label.pack(side=LEFT, padx=20)

#login image label
login_image_label = Label(frame1,image= login_image)
login_image_label.pack(side=LEFT, padx=20)

#exit image label
exit_image_label = Label(frame1,image= exit_image)
exit_image_label.pack(side=LEFT, padx=20)

frame2  = Frame(main_window, padx=80)
frame2.place(x=80, y=400, width=1000, height=100)


#registration
button = tk.Button(frame2,text="Registration",pady=3,padx =60,command=registration)
button.grid(column=2, row=2,padx=20)

#login
button = tk.Button(frame2,text="Login",pady=3,padx =60,command=login)
button.grid(column=4, row=2,padx=40)

#exit
button = tk.Button(frame2,text="Exit",pady=3,padx =60,command=main_window.destroy)
button.grid(column=10, row=2,padx=60)


main_window.mainloop()