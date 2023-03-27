# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:14:01 2022

@author: durga
"""

# =============================================================================
# teacher registration form
# =============================================================================

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image


def teacher_add():
    
    if ((teacher_name_entry.get() == '') or (teacher_admission_number_entry.get() == '' 
                                             or (teacher_gender_entry.get() ==''))):
        messagebox.showerror('required fields',"please include all the  fields")
        
    teacher_name_text               =   teacher_name_entry.get()
    teacher_admission_number_text   =   teacher_admission_number_entry.get()
    teacher_gender_text             =   teacher_gender_entry.get() 
    teacher_father_text             =   teacher_father_entry.get() 
    teacher_mother_text             =   teacher_mother_entry.get()
    teacher_dob_text                = teacher_dob_entry.get()
    teacher_standard_text           = teacher_standard_entry.get()
    teacher_contact_text            = teacher_contact_entry.get()
    teacher_doa_text                =   teacher_doa_entry.get()
    teacher_section_text            =   teacher_section_entry.get()
    teacher_address_text            = teacher_address_entry.get()
    
    print(teacher_name_text)
    print(teacher_admission_number_text ,teacher_gender_text ,teacher_father_text )
    print(teacher_mother_text ,teacher_dob_text ,teacher_standard_text )
    print(teacher_contact_text ,teacher_doa_text ,teacher_section_text )
    print(teacher_address_text)

st_reg_win = Tk()
st_reg_win.title("school management system")
st_reg_win.geometry("1200x800")

#header block
heading_frame =Frame(st_reg_win)
heading_frame.place(x =0,y=0,width =1200,height=60)

header = Label(heading_frame,text="teacher registration form",bg="#00bfff",fg="white",font=("arial",20))
header.pack(side=TOP,fill=X)

#teacher entry block
#st_entry_fr = Frame(st_reg_win,padx =20,bg ="red")
st_entry_fr = Frame(st_reg_win,padx =20)
st_entry_fr.place(x=40,y=80,width =1200,height=300)

#teacher_name
teacher_name = Label(st_entry_fr,text="teacher Name")
teacher_name.grid(row =1,column =1,padx = 20, pady = 6)

#admission number
teacher_admission =  Label(st_entry_fr,text=" Admission Number")
teacher_admission .grid(row =2,column =1,padx = 20, pady = 6)

#gender
teacher_gender = Label(st_entry_fr,text="Gender")
teacher_gender.grid(row =3,column =1,padx = 20, pady = 6)
#email id
teacher_email = Label(st_entry_fr,text="Email")
teacher_email.grid(row =4,column =1,padx = 20, pady = 6)
#father name
teacher_father_name = Label(st_entry_fr,text="Father Name")
teacher_father_name.grid(row =1,column =3,padx = 20, pady = 6)
#mother name
teacher_mother_name = Label(st_entry_fr,text="Mother Name")
teacher_mother_name.grid(row =2,column =3,padx = 20, pady = 6)
#DOB
teacher_dob = Label(st_entry_fr,text="Date of birth")
teacher_dob .grid(row =3,column =3,padx = 20, pady = 6)
#standard/class
teacher_standard = Label(st_entry_fr,text="standard")
teacher_standard.grid(row =4,column =3,padx = 20, pady = 6)
#contact number
teacher_contact = Label(st_entry_fr,text="Contact number")
teacher_contact.grid(row =1,column =5,padx = 20, pady = 6)
#Date of admission
teacher_doa = Label(st_entry_fr,text="Date of Admission")
teacher_doa.grid(row =2,column =5,padx = 20, pady = 6)
#section
teacher_section = Label(st_entry_fr,text="section")
teacher_section.grid(row =3,column =5,padx = 20, pady = 6)
#address
teacher_address = Label(st_entry_fr,text="Address")
teacher_address.grid(row =4,column =5,padx = 20, pady = 6)



#variables for stroing entries
teacher_name_value         = StringVar()
teacher_admission_value    = IntVar()
teacher_gender_value       = StringVar()
teacher_email_value        = StringVar()
teacher_father_name_value  =    StringVar()
teacher_mother_name_value  =    StringVar()
teacher_dob_val            =    IntVar()
teacher_standard_value     =    IntVar()
teacher_contact_value      =    IntVar()
teacher_doa_value          =    IntVar()
teacher_section_value      =    StringVar()
teacher_address_value      =    StringVar()



#entries entry block
teacher_name_entry = Entry(st_entry_fr,textvariable=teacher_name_value,width =30)
teacher_name_entry.grid(row =1,column =2)

#admission number
teacher_admission_number_entry = Entry(st_entry_fr,textvariable=teacher_admission_value ,width =30)
teacher_admission_number_entry.grid(row =2,column =2)


#gender
teacher_gender_entry = Entry(st_entry_fr,textvariable=teacher_gender_value,width =30)
teacher_gender_entry.grid(row =3,column =2)
#email id
teacher_email_entry = Entry(st_entry_fr,textvariable=teacher_email_value,width =30)
teacher_email_entry.grid(row =4,column =2)
#father name
teacher_father_entry = Entry(st_entry_fr,textvariable=teacher_father_name_value,width =30)
teacher_father_entry.grid(row =1,column =4)
#mother name
teacher_mother_entry = Entry(st_entry_fr,textvariable=teacher_mother_name_value,width =30)
teacher_mother_entry.grid(row =2,column =4)
#DOB
teacher_dob_entry = Entry(st_entry_fr,textvariable=teacher_dob_val,width =30)
teacher_dob_entry.grid(row =3,column =4)
#standard/class
teacher_standard_entry = Entry(st_entry_fr,textvariable=teacher_standard_value,width =30)
teacher_standard_entry.grid(row =4,column =4)
#contact number
teacher_contact_entry = Entry(st_entry_fr,textvariable=teacher_contact_value,width =30)
teacher_contact_entry.grid(row =1,column =6)
#Date of admission
teacher_doa_entry = Entry(st_entry_fr,textvariable=teacher_doa_value,width =30)
teacher_doa_entry.grid(row =2,column =6)
#section
teacher_section_entry = Entry(st_entry_fr,textvariable=teacher_section_value,width =30)
teacher_section_entry.grid(row =3,column =6)
#address
teacher_address_entry = Entry(st_entry_fr,textvariable=teacher_address_value,width =30)
teacher_address_entry.grid(row =4,column =6)


Button(st_entry_fr,text="submit",command=teacher_add).grid(row=5,column=2)


st_reg_win.mainloop()