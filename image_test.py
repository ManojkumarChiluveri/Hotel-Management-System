# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:34:02 2022

@author: durga
"""

from tkinter import *
from PIL import Imag
eTk,Image

window = Tk()

frame1 = Frame(window)
frame1.pack(side = TOP, fill = X)

image1 = Image.open("reg.png")
image1 = ImageTk.PhotoImage(file="reg.png")


label1 = Label(frame1, image=image1)
label1.pack(side= LEFT, padx=20)

window.mainloop()