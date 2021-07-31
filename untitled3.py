# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:07:21 2021

@author: joyab
"""

from tkinter import*

root = Tk()
root.title("Identity Card")
root.geometry("300x400")

root.configure(bg="white")
canvas = Canvas(root, width=400, height=250)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#1463B0")

label_heading = canvas.create_text(200, 20, font=('Times', '24', 'bold italic'), text="Drivers license: ")
label_name_tag = canvas.create_text(30, 300, font=('Times', '16', 'bold'), text="Name :")
label_id_tag = canvas.create_text(25, 60, font=('Times', '16', 'bold'), text="ID :")
label_dob_tag = canvas.create_text(52, 120, font=('Times', '16', 'bold'), text="DOB :")
label_pin_tag = canvas.create_text(32, 140, font=('Times', '16', 'bold'), text="Pin number :")
label_address_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="Address :")
label_vehicle_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Vehicle type :")

label_name = Label(root)
label_id = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle = Label(root)

def function_identity():
    id_value = 4921549390
    print(type (id_value))
    name = "Hank J. Wimbleton"
    print(type (name))
    dob="09,22,1996"
    print(type(dob))
    pin=("092296")
    print(type(pin))
    address=("Address: 92296, Nevada")
    print(type(address))
    vehicle=("Vehicle: Four Wheeler")
    print(type(vehicle))

btn1 = Button(root, text="Show my driving license", command = function_identity)

btn1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
btn1_window = canvas.create_window(150, 330, anchor = CENTER, window=btn1)
label_id_window =canvas.create_window(80, 60, anchor = CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor = CENTER, window=label_name)
label_dob_window =canvas.create_window(140, 120, anchor = CENTER, window=label_dob)
label_pin_window =canvas.create_window(85, 140, anchor = CENTER, window=label_pin)
label_address_window =canvas.create_window(130, 160, anchor = CENTER, window=label_address)
label_vehicle_window =canvas.create_window(140, 120, anchor = CENTER, window=label_vehicle)
canvas.pack()

root.mainloop()