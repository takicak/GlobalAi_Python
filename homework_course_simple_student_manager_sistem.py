# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 04:08:45 2020

@author: takic
"""
import sys
import random
#----------------------------------------------------------------
#  LOGIN OLABILECEK USER LISTESI
#----------------------------------------------------------------
userlist = [ ["ömer", "cengiz"], ["elif", "yiğit"], ["kutay", "akalın"], ["aysuda","ceylan"] ]

def display_grade_str(score):
    if score >= 90:
        return("AA")
    elif 70 <= score < 90:
        return("BB")
    elif 50 <= score < 70:
        return("CC")
    elif 30 <= score < 50:
        return("DD")
    else:
        return("FF You Fail")
    


login = False
logintry = 0
login_fname = ""
login_lname = ""

while not login:
    login_fname = input("Enter Student Firstname : ")
    login_lname = input("Enter Student Lastname  : ")
    
    for user in userlist:
        if user[0] == login_fname and user[1] == login_lname:
            login = True
            break
            
    if not login:
        logintry += 1

        if logintry == 3:
            print("Please Try Again Later...")
            sys.exit()
        else:
            print("Information is Wrong! Try Again")
print()
print()
print()
print("--------------------------------------------")
print("         GLOBAL AI HUB UNIVERSITY")
print("--------------------------------------------")
print("Welcome", login_fname.upper(), login_lname.upper())
print()
print("Please Enter 5 Lesson Name")

lessoncount = 1
lessons = []

while lessoncount < 6:
    lessons.append(input("Input " + str(lessoncount) + ". Lesson Name : " ))
    lessoncount += 1
    
print("Main Lesson List is saved...")
print()
for lesson in lessons:
    print(str(lessons.index(lesson)+1) + ".)", lesson, "Lesson")
    
    
print("Please Select min 3, max 5 lesson for Yourself.")

selectedlessonscount = 0
selectedlessons = []
selectedlesson = -1

while not (selectedlesson == 0 and 3 <= selectedlessonscount <= 5 ):
    selectedlesson = input("(press 0 (zero) to quit) Lesson Number : ")
    try:
        selectedlesson = int(selectedlesson)
    except:
        print("Wrong selection...")
        continue
    
    if selectedlesson in (1,2,3,4,5) and lessons[selectedlesson-1] in lessons:
        if lessons[selectedlesson-1] not in selectedlessons: 
            selectedlessons.append(lessons[selectedlesson-1])
            selectedlessonscount += 1
            print("Selected Lessons ("+str(selectedlessonscount)+") : ", end="")
            for seles in selectedlessons:
                print(seles, ", ", end="")
        else:
            print("You Select This Lesson Before")
                
    elif selectedlesson == 0:
        if not (3 <= selectedlessonscount <= 5):
            print("You Should Select min 3, max 5 lesson for Yourself.")
            print("You failed in Class")
            continue

grades = {"midterm":random.randint(0, 100), 
          "final":random.randint(0, 100),
          "project":random.randint(0, 100)}

score = 0
print()
print("--------------------------------------------")
print("Your", selectedlessons[0], "Lesson Exam Grades")
score += grades["midterm"]*30/100
score += grades["final"]*50/100
score += grades["project"]*20/100
print("MidTerm Exam: ", grades["midterm"], "Score Percent(30%) :", grades["midterm"]*30/100)
print("Final   Exam: ", grades["final"],   "Score Percent(50%) :", grades["final"]*50/100)
print("Project Exam: ", grades["project"], "Score Percent(20%) :", grades["project"]*20/100)
print("Total Score :", score, "Note is", display_grade_str(score))  