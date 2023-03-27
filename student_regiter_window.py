from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import pymysql


# conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
# cursor1 = conn.cursor()
# print(cursor1)

mydb = pymysql.connect( host="localhost",  user="root",  password="")
mycursor = mydb.cursor()
a = mycursor.execute("CREATE DATABASE school_management")
if a ==1:
    print("database created successfully")
else:
    print("database already exists")


# =============================================================================
# creating tables
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='school_management')
cursor1 = conn.cursor()
cursor1.execute("CREATE TABLE student_table ( sno int,\
                    student_name varchar(255) ,\
                    student_admission_number int,\
                    student_gender varchar(255) ,\
                    student_father varchar(255) ,\
                    student_mother varchar(255) ,\
                    student_dob  varchar(255) ,\
                    student_standard int,\
                    student_contact varchar(255) ,\
                    student_doa varchar(255) ,\
                    student_section int,\
                    student_address varchar(255)) ")


def student_add():
    student_name_text               = student_name_entry.get()
    student_admission_number_text   = student_admission_number_entry.get()
    student_gender_text             = student_gender_entry.get() 
    student_father_text             = student_father_entry.get() 
    student_mother_text             = student_mother_entry.get()
    student_dob_text                = student_dob_entry.get()
    student_standard_text           = student_standard_entry.get()
    student_contact_text            = student_contact_entry.get()
    student_doa_text                =   student_doa_entry.get()
    student_section_text            =   student_section_entry.get()
    student_address_text            = student_address_entry.get()
    
    print(student_name_text)
    print(student_admission_number_text ,student_gender_text ,student_father_text )
    print(student_mother_text ,student_dob_text ,student_standard_text )
    print(student_contact_text ,student_doa_text ,student_section_text )
    print(student_address_text)

st_reg_win = Tk()
st_reg_win.title("school management system")
st_reg_win.geometry("1200x800")

#header block
heading_frame =Frame(st_reg_win)
heading_frame.place(x =0,y=0,width =1200,height=60)

header = Label(heading_frame,text="Student registration form",bg="#00bfff",fg="white",font=("arial",20))
header.pack(side=TOP,fill=X)

#student entry block
#st_entry_fr = Frame(st_reg_win,padx =20,bg ="red")
st_entry_fr = Frame(st_reg_win,padx =20)
st_entry_fr.place(x=40,y=80,width =1200,height=300)

#student_name
student_name = Label(st_entry_fr,text="Student Name")
student_name.grid(row =1,column =1,padx = 20, pady = 6)

#admission number
student_admission =  Label(st_entry_fr,text=" Admission Number")
student_admission .grid(row =2,column =1,padx = 20, pady = 6)

#gender
student_gender = Label(st_entry_fr,text="Gender")
student_gender.grid(row =3,column =1,padx = 20, pady = 6)
#email id
student_email = Label(st_entry_fr,text="Email")
student_email.grid(row =4,column =1,padx = 20, pady = 6)
#father name
student_father_name = Label(st_entry_fr,text="Father Name")
student_father_name.grid(row =1,column =3,padx = 20, pady = 6)
#mother name
student_mother_name = Label(st_entry_fr,text="Mother Name")
student_mother_name.grid(row =2,column =3,padx = 20, pady = 6)
#DOB
student_dob = Label(st_entry_fr,text="Date of birth")
student_dob .grid(row =3,column =3,padx = 20, pady = 6)
#standard/class
student_standard = Label(st_entry_fr,text="standard")
student_standard.grid(row =4,column =3,padx = 20, pady = 6)
#contact number
student_contact = Label(st_entry_fr,text="Contact number")
student_contact.grid(row =1,column =5,padx = 20, pady = 6)
#Date of admission
student_doa = Label(st_entry_fr,text="Date of Admission")
student_doa.grid(row =2,column =5,padx = 20, pady = 6)
#section
student_section = Label(st_entry_fr,text="section")
student_section.grid(row =3,column =5,padx = 20, pady = 6)
#address
student_address = Label(st_entry_fr,text="Address")
student_address.grid(row =4,column =5,padx = 20, pady = 6)



#variables for stroing entries
student_name_value         = StringVar()
student_admission_value    = IntVar()
student_gender_value       = StringVar()
student_email_value        = StringVar()
student_father_name_value  =    StringVar()
student_mother_name_value  =    StringVar()
student_dob_val            =    IntVar()
student_standard_value     =    IntVar()
student_contact_value      =    IntVar()
student_doa_value          =    IntVar()
student_section_value      =    StringVar()
student_address_value      =    StringVar()



#entries entry block
student_name_entry = Entry(st_entry_fr,textvariable=student_name_value,width =30)
student_name_entry.grid(row =1,column =2)

#admission number
student_admission_number_entry = Entry(st_entry_fr,textvariable=student_admission_value ,width =30)
student_admission_number_entry.grid(row =2,column =2)


#gender
student_gender_entry = Entry(st_entry_fr,textvariable=student_gender_value,width =30)
student_gender_entry.grid(row =3,column =2)
#email id
student_email_entry = Entry(st_entry_fr,textvariable=student_email_value,width =30)
student_email_entry.grid(row =4,column =2)
#father name
student_father_entry = Entry(st_entry_fr,textvariable=student_father_name_value,width =30)
student_father_entry.grid(row =1,column =4)
#mother name
student_mother_entry = Entry(st_entry_fr,textvariable=student_mother_name_value,width =30)
student_mother_entry.grid(row =2,column =4)
#DOB
student_dob_entry = Entry(st_entry_fr,textvariable=student_dob_val,width =30)
student_dob_entry.grid(row =3,column =4)
#standard/class
student_standard_entry = Entry(st_entry_fr,textvariable=student_standard_value,width =30)
student_standard_entry.grid(row =4,column =4)
#contact number
student_contact_entry = Entry(st_entry_fr,textvariable=student_contact_value,width =30)
student_contact_entry.grid(row =1,column =6)
#Date of admission
student_doa_entry = Entry(st_entry_fr,textvariable=student_doa_value,width =30)
student_doa_entry.grid(row =2,column =6)
#section
student_section_entry = Entry(st_entry_fr,textvariable=student_section_value,width =30)
student_section_entry.grid(row =3,column =6)
#address
student_address_entry = Entry(st_entry_fr,textvariable=student_address_value,width =30)
student_address_entry.grid(row =4,column =6)


#Button(st_entry_fr,text="submit",command=student_add).grid(row=5,column=2)


app2 = Frame(st_reg_win, padx=10)
app2.place(x=100, y=290, width=710, height=100)

#Button & packing it and assigning it a command
Button(app2, text="ADD", command=student_add, bg="#E6E6FA", pady=3, padx=40).grid(row=5, column=1, padx=20)
#Button(app2, text="DELETE", command=delete, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=2, padx=10)
#Button(app2, text="CANCEL", command=back_register, bg="#E6E6FA", pady=3, padx=30).grid(row=5, column=3,padx=20)

# Search Teacher's
search = Label(app2, text="Search student's")
search.grid(row=5, column=4, pady=6, padx=15)
searchvalue = StringVar()

searchentry = Entry(app2, textvariable=searchvalue, width=30)
searchentry.grid(row=5, column=5)


#view of the students
view_frame= Frame(st_reg_win,bg ="red", bd=2, relief=RIDGE)
view_frame.place(x=20,y=350,width =1200,height=400)

#tree view
#view_fram_in = ttk.Treeview(view_frame)

style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right'}),  # , 'sticky': ''
            ("Custom.Treeheading.text", {'sticky': 'we'})
        ]})
    ]}),
])

style.configure("Custom.Treeview.Heading", background="lightgrey", foreground="black", relief="groove")
style.map("Custom.Treeview.Heading", relief=[('active', 'flat'), ('pressed', 'sunken')])

xscroll = Scrollbar(view_frame,orient=HORIZONTAL)
yscroll = Scrollbar(view_frame,orient = VERTICAL)

columns = ("student_name","student_admission_no","student_gender",
               "student_email","student_father_name","student_mother_name",
               "student_dob","student_standard","student_contact_no",
               "student_doa","student_section","student_address" )

student_table = ttk.Treeview(view_frame,style="Custom.Treeview",columns=columns,
                             show = "headings",xscrollcommand=xscroll.set,
                             yscrollcommand=yscroll.set)

#setting scrollbar from two side x, y directions
yscroll.config(command=student_table.yview)
xscroll.config(command= student_table.xview)

yscroll.pack(side=BOTTOM,fill=X)
xscroll.pack(side=RIGHT,fill=Y)


#headings
student_table.heading("student_name",text = "student name")
student_table.heading("student_admission_no",text = "student_admission_no")
student_table.heading("student_gender",text = "student_gender")
student_table.heading("student_email",text = "student_email")
student_table.heading("student_father_name",text = "student_father_name")
student_table.heading("student_mother_name",text = "student_mother_name")
student_table.heading("student_dob",text = "student_dob")
student_table.heading("student_standard",text = "student_standard")
student_table.heading("student_contact_no",text = "student_contact_no")
student_table.heading("student_doa",text = "student_doa")
student_table.heading("student_section",text = "student_section")
student_table.heading("student_address",text = "student_address")


#columns
student_table.column("student_name", width=80)
student_table.column("student_admission_no", width=50,anchor=CENTER)
student_table.column("student_gender", width=50,anchor= CENTER)
student_table.column("student_email", width=150,anchor= CENTER)
student_table.column("student_father_name", width=120,anchor= CENTER)
student_table.column("student_mother_name", width=100,anchor= CENTER)
student_table.column("student_dob", width=100,anchor= CENTER)
student_table.column("student_standard", width=100,anchor= CENTER)
student_table.column("student_contact_no", width=100,anchor= CENTER)
student_table.column("student_doa", width=100,anchor= CENTER)
student_table.column("student_section", width=100,anchor= CENTER)
student_table.column("student_address", width=100,anchor= CENTER)

student_table.pack(fill=BOTH,expand=TRUE)

st_reg_win.mainloop()



