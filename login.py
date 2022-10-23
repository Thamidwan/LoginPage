from cProfile import label
from tkinter import *
from unicodedata import name
root = Tk()
root.geometry("300x300")

def getvals():
    print("Accepted")

#eading
Label(root, text="registration form",font="ar 15 bold").grid(row=0,column=3)

#field Name
name = Label(root, text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")

#packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)

#declaring values
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
checkvalue = IntVar

#Creating entryField
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)

#packing entry
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2 ,column=3)
genderentry.grid(row=3 ,column=3)

#creating checkbox
checkbtn = Checkbutton (text="remember me ?",  variable=checkvalue)
checkbtn.grid(row=4 , column=3)

#submit
Button(text="Submit",command=getvals).grid(row=5,column=3)




root.mainloop()