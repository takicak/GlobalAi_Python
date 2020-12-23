# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:52:38 2020

@author: takic
"""
fname =      input("Enter User First Name : ")
lname =      input("Enter User Last Name : ")
age   = int( input("Enter User Age : ") )
byear = int( input("Enter User Birthdate (Year) : ") )

ulist = [fname, lname, age, byear]
utag  = ["FirstName", "LastName", "Age", "Birthdate"]



print() 

for id in range(len(ulist)):
    print(utag[id], ":", ulist[id])
    
if int(ulist[2]) < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")
