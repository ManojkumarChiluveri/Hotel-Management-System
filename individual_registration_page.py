

# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:31:29 2022
@author: durga
file name: individual_registration_page.py
"""

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image



#functions for opening new windows
def student_registration():
    student_register_window()
    
    
def teacher_registration():
    print("Here we need to pass to another window")

def employee_registration():
    print("Here we need to pass to another window")
    


def registration_details():
    
    registration_window = Tk()
    registration_window.geometry("1080x800")
    registration_window.title("School management system")
    
    
    headingframe = Frame(registration_window)
    headingframe.place(x=0, y=0, width=1200, height=50)
    Label(headingframe, text="School management system",font=("Times", "50", "bold italic"),background="blue").place()
    
    print("reached upto here")
    #to separate the window into block/frame
    frame1 = Frame(registration_window, padx=100)
    frame1.place(x=100, y=160, width=1200, height=300)
    
    
    #reading the images from the folder
    student_reg_image = ImageTk.PhotoImage(file ="registration.png")
    
    teacher_reg_image = ImageTk.PhotoImage(file ="registration.png")
    employee_reg_image = ImageTk.PhotoImage(file ="registration.png")
    exit_image = ImageTk.PhotoImage(file ="exit.png")
    
    #to display the image on the window
    #registration image label
    student_reg_image_label = Label(frame1,image= student_reg_image)
    student_reg_image_label.pack(side=LEFT, padx=20)
    
    #login image label
    teacher_reg_image_label = Label(frame1,image= teacher_reg_image)
    teacher_reg_image_label.pack(side=LEFT, padx=40)
    
    # employee_reg_image_label = Label(frame1,image= employee_reg_image)
    # employee_reg_image_label.pack(side=LEFT, padx=60)
    
    #exit image label
    exit_image_label = Label(frame1,image= exit_image)
    exit_image_label.pack(side=LEFT, padx=80)
    
    
    
    
    frame2  = Frame(registration_window, padx=140)
    frame2.place(x=100, y=400, width=1000, height=100)
    
    
    #registration
    button = tk.Button(frame2,text="student",width=20,command=student_registration)
    button.grid(column=2, row=2,padx=20)
    
    #login
    button = tk.Button(frame2,text="Teacher",width=20,command=teacher_registration)
    button.grid(column=4, row=2,padx=40)
    
    # button = tk.Button(frame2,text="Employee",width=20,command=employee_registration)
    # button.grid(column=6, row=2,padx=60)
    
    #exit
    button = tk.Button(frame2,text="Exit",width=20,command=registration_window.destroy)
    button.grid(column=8, row=2,padx=80)
    
    
    registration_window.mainloop()

registration_details()
