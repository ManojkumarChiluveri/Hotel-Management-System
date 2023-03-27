# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:18:28 2022

@author: durga
"""



# =============================================================================
# Employee registration form
# =============================================================================

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image


def employee_add():
    employee_name_text               = employee_name_entry.get()
    employee_admission_number_text   = employee_admission_number_entry.get()
    employee_gender_text             = employee_gender_entry.get() 
    employee_father_text             = employee_father_entry.get() 
    employee_mother_text             = employee_mother_entry.get()
    employee_dob_text                = employee_dob_entry.get()
    employee_standard_text           = employee_standard_entry.get()
    employee_contact_text            = employee_contact_entry.get()
    employee_doa_text                =   employee_doa_entry.get()
    employee_section_text            =   employee_section_entry.get()
    employee_address_text            = employee_address_entry.get()
    
    print(employee_name_text)
    print(employee_admission_number_text ,employee_gender_text ,employee_father_text )
    print(employee_mother_text ,employee_dob_text ,employee_standard_text )
    print(employee_contact_text ,employee_doa_text ,employee_section_text )
    print(employee_address_text)

st_reg_win = Tk()
st_reg_win.title("school management system")
st_reg_win.geometry("1200x800")

#header block
heading_frame =Frame(st_reg_win)
heading_frame.place(x =0,y=0,width =1200,height=60)

header = Label(heading_frame,text="employee registration form",bg="#00bfff",fg="white",font=("arial",20))
header.pack(side=TOP,fill=X)

#employee entry block
#st_entry_fr = Frame(st_reg_win,padx =20,bg ="red")
st_entry_fr = Frame(st_reg_win,padx =20)
st_entry_fr.place(x=40,y=80,width =1200,height=300)

#employee_name
employee_name = Label(st_entry_fr,text="employee Name")
employee_name.grid(row =1,column =1,padx = 20, pady = 6)

#admission number
employee_admission =  Label(st_entry_fr,text=" Admission Number")
employee_admission .grid(row =2,column =1,padx = 20, pady = 6)

#gender
employee_gender = Label(st_entry_fr,text="Gender")
employee_gender.grid(row =3,column =1,padx = 20, pady = 6)
#email id
employee_email = Label(st_entry_fr,text="Email")
employee_email.grid(row =4,column =1,padx = 20, pady = 6)
#father name
employee_father_name = Label(st_entry_fr,text="Father Name")
employee_father_name.grid(row =1,column =3,padx = 20, pady = 6)
#mother name
employee_mother_name = Label(st_entry_fr,text="Mother Name")
employee_mother_name.grid(row =2,column =3,padx = 20, pady = 6)
#DOB
employee_dob = Label(st_entry_fr,text="Date of birth")
employee_dob .grid(row =3,column =3,padx = 20, pady = 6)
#standard/class
employee_standard = Label(st_entry_fr,text="standard")
employee_standard.grid(row =4,column =3,padx = 20, pady = 6)
#contact number
employee_contact = Label(st_entry_fr,text="Contact number")
employee_contact.grid(row =1,column =5,padx = 20, pady = 6)
#Date of admission
employee_doa = Label(st_entry_fr,text="Date of Admission")
employee_doa.grid(row =2,column =5,padx = 20, pady = 6)
#section
employee_section = Label(st_entry_fr,text="section")
employee_section.grid(row =3,column =5,padx = 20, pady = 6)
#address
employee_address = Label(st_entry_fr,text="Address")
employee_address.grid(row =4,column =5,padx = 20, pady = 6)



#variables for stroing entries
employee_name_value         = StringVar()
employee_admission_value    = IntVar()
employee_gender_value       = StringVar()
employee_email_value        = StringVar()
employee_father_name_value  =    StringVar()
employee_mother_name_value  =    StringVar()
employee_dob_val            =    IntVar()
employee_standard_value     =    IntVar()
employee_contact_value      =    IntVar()
employee_doa_value          =    IntVar()
employee_section_value      =    StringVar()
employee_address_value      =    StringVar()



#entries entry block
employee_name_entry = Entry(st_entry_fr,textvariable=employee_name_value,width =30)
employee_name_entry.grid(row =1,column =2)

#admission number
employee_admission_number_entry = Entry(st_entry_fr,textvariable=employee_admission_value ,width =30)
employee_admission_number_entry.grid(row =2,column =2)


#gender
employee_gender_entry = Entry(st_entry_fr,textvariable=employee_gender_value,width =30)
employee_gender_entry.grid(row =3,column =2)
#email id
employee_email_entry = Entry(st_entry_fr,textvariable=employee_email_value,width =30)
employee_email_entry.grid(row =4,column =2)
#father name
employee_father_entry = Entry(st_entry_fr,textvariable=employee_father_name_value,width =30)
employee_father_entry.grid(row =1,column =4)
#mother name
employee_mother_entry = Entry(st_entry_fr,textvariable=employee_mother_name_value,width =30)
employee_mother_entry.grid(row =2,column =4)
#DOB
employee_dob_entry = Entry(st_entry_fr,textvariable=employee_dob_val,width =30)
employee_dob_entry.grid(row =3,column =4)
#standard/class
employee_standard_entry = Entry(st_entry_fr,textvariable=employee_standard_value,width =30)
employee_standard_entry.grid(row =4,column =4)
#contact number
employee_contact_entry = Entry(st_entry_fr,textvariable=employee_contact_value,width =30)
employee_contact_entry.grid(row =1,column =6)
#Date of admission
employee_doa_entry = Entry(st_entry_fr,textvariable=employee_doa_value,width =30)
employee_doa_entry.grid(row =2,column =6)
#section
employee_section_entry = Entry(st_entry_fr,textvariable=employee_section_value,width =30)
employee_section_entry.grid(row =3,column =6)
#address
employee_address_entry = Entry(st_entry_fr,textvariable=employee_address_value,width =30)
employee_address_entry.grid(row =4,column =6)


Button(st_entry_fr,text="submit",command=employee_add).grid(row=5,column=2)


st_reg_win.mainloop()