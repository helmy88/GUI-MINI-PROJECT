
#Part 1 Log In System (Database)
#import modules

from tkinter import *
import os


# Designing window for registration

def register():
  
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details to register", bg="#EC7063", width="300", height="2", font=("Calibri", 13) ).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#F4D03F", command = register_user, ).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login", bg="#EC7063", width="300", height="2", font=("Calibri", 13)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="#F4D03F", command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# 2nd windows pop up,welcome to cgpa

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("MINI PROJECT")
    login_success_screen.geometry("300x250")
    Label(login_success_screen, text=" WELCOME TO CGPA CALCULATOR",bg="blue",width="300", height="2", fg="black",font=("Calibri",50,"bold")).pack()
    Button(login_success_screen, bg="yellow",text="CGPA CALCULATOR").pack()
    window()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="User are not autorised Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found",bg="#5499C7", width="100", height="1", font=("Calibri", 13) ).pack()
    Button(user_not_found_screen, text="OK",bg="#884EA0", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x300")
    main_screen.title("Account Login")
    Label(text="UNIVERSITY MALAYSIA PERLIS", bg="blue", width="300", height="3", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text="CGPA Calculator", bg="yellow", width="300", height="3", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30",bg="#BFC9CA", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30",bg="#BFC9CA", command=register).pack()
    
    main_screen.mainloop()

    
main_account_screen()


#Part 2 CGPA Calculator
#Latest Code Updated [23/08/2020 @12:45AM]

#Import Tkinter
from tkinter import*

#Assign Tk
window = Tk()

#Assign Window Title
window.title("MINI PROJECT VGT123")

#Set Window Size
window.geometry("1200x700")

#Assign Application Name
Label(window, text="CGPA CALCULATOR", bg="#ffff33", font="bold").grid(row=0,column=7)

#Formula CGPA
#(Grade * Unit) / Unit

#Unit
r0 = Entry (window) 
r8 = Entry (window) 
r9 = Entry (window) 
r10 = Entry (window) 
r11 = Entry (window) 
r12 = Entry (window) 
r13 = Entry (window) 
r15 = Entry (window) 

#Subject
r16 = Entry (window)
r17 = Entry (window)
r18 = Entry (window)
r19 = Entry (window)
r20 = Entry (window)
r21 = Entry (window)
r22 = Entry (window)
r23 = Entry (window)

#Value Grade
r27 = Entry (window) 
r28 = Entry (window) 
r29 = Entry (window) 
r30 = Entry (window) 
r31 = Entry (window) 
r32 = Entry (window) 
r33 = Entry (window) 
r34 = Entry (window)

#Function [CLEAR]
def clear():
    r0.delete(0,END)
    r8.delete(0,END) 
    r9.delete(0,END) 
    r10.delete(0,END) 
    r11.delete(0,END) 
    r12.delete(0,END) 
    r13.delete(0,END) 
    r15.delete(0,END)  
    r16.delete(0,END) 
    r17.delete(0,END) 
    r18.delete(0,END) 
    r19.delete(0,END) 
    r20.delete(0,END) 
    r21.delete(0,END) 
    r22.delete(0,END) 
    r23.delete(0,END) 
    r27.delete(0,END)  
    r28.delete(0,END) 
    r29.delete(0,END)  
    r30.delete(0,END)  
    r31.delete(0,END) 
    r32.delete(0,END) 
    r33.delete(0,END) 
    r34.delete(0,END)

#Function [CALCULATION]
def answer():

    #Value Grade
    v1 = r27.get()
    v2 = r28.get()
    v3 = r29.get()
    v4 = r30.get()
    v5 = r31.get()
    v6 = r32.get()
    v7 = r33.get()
    v8 = r34.get()

    #Unit
    v9 = r0.get()
    v10 = r8.get()
    v11 = r9.get()
    v12 = r10.get()
    v13 = r11.get()
    v14 = r12.get()
    v15 = r13.get()
    v16 = r15.get()

    #Calculation
    Answer = (float(v1)*int(v9)) + (float(v2)*int(v10)) + (float(v3)*int(v11)) + (float(v4)*int(v12)) + (float(v5)*int(v13)) + (float(v6)*int(v14)) + (float(v7)*int(v15)) + (float(v8)*int(v16))
    Total_Unit = int(v9) + int(v10) + int(v11) + int(v12) + int(v13) + int(v14) + int(v15) + int(v16)
    Total_Grade = float(v1) + float(v2) + float(v3) + float(v4) + float(v5) + float(v6) + float(v7) + float(v8)
    Status = Answer / Total_Unit
    con_answer = float("{0:.2f}".format(Status)) 

    #Display Total Grade 
    Label(window, text="Total Grade :").grid(row=19,column=3)
    Label(window, text=(Total_Grade)).grid(row=19, column=5)

    #Display Total Unit
    Label(window, text="   Total Unit :").grid(row=20,column=3)
    Label(window, text=(Total_Unit)).grid(row=20, column=5)

    #Display CGPA
    Label(window, text="          CGPA :").grid(row=21,column=3)
    Label(window, text=(con_answer)).grid(row=21, column=5)

    #Display Status Result
    Label(window, text="         Status :").grid(row=22,column=3)

    #Condition ResultS
    "This function calculate CGPA by input user"
    if Status >= 3.67 and Status <=4.00:
        Label(window, text="Dean List", fg="#0000ff", font="bold").grid(row=22, column=5)
    elif Status >= 2.75 and Status <=3.66:
        Label(window, text="Pass", fg="#ff9900", font="bold").grid(row=22, column=5)
    elif Status >= 2.00 and Status <=2.74:
        Label(window, text="Conditional Pass", fg="#00ff00", font="bold").grid(row=22,column=5)
    else :
        Label(window, text="Fail", fg="#ff3300", font="bold").grid(row=22,column=5)

#Entry Subject
r16 = Entry(window)
r17 = Entry(window)
r18 = Entry(window)
r19 = Entry(window)
r20 = Entry(window)
r21 = Entry(window)
r22 = Entry(window)
r23 = Entry(window)

#Organizing [NUMBER]
Label(window, text="Number",bg="#1a8cff").grid(row=2,column=1)
Label(window, text="1").grid(row=3,column=1)
Label(window, text="2").grid(row=5,column=1)
Label(window, text="3").grid(row=7,column=1)
Label(window, text="4").grid(row=9,column=1)
Label(window, text="5").grid(row=11,column=1)
Label(window, text="6").grid(row=13,column=1)
Label(window, text="7").grid(row=15,column=1)
Label(window, text="8").grid(row=17,column=1)

#Organizing [SUBJECT]
Label(window, text="Subject", bg="#d279d2").grid(row=2,column=3)
r16.grid(row=3, column=3)
r17.grid(row=5, column=3)
r18.grid(row=7, column=3)
r19.grid(row=9, column=3)
r20.grid(row=11, column=3)
r21.grid(row=13, column=3)
r22.grid(row=15, column=3)
r23.grid(row=17, column=3)

#Organizing [GRADE VALUE]
Label(window, text="Grade Value", bg="#dfff80").grid(row=2,column=5)
r27.grid(row=3, column=5)
r28.grid(row=5, column=5)
r29.grid(row=7, column=5)
r30.grid(row=9, column=5)
r31.grid(row=11, column=5)
r32.grid(row=13, column=5)
r33.grid(row=15, column=5)
r34.grid(row=17, column=5)

#Organizing [UNIT]
Label(window, text="Unit", bg="#ffb84d").grid(row=2,column=7)
r0.grid(row=3, column=7)
r8.grid(row=5, column=7)
r9.grid(row=7, column=7)
r10.grid(row=9, column=7)
r11.grid(row=11, column=7)
r12.grid(row=13, column=7)
r13.grid(row=15, column=7)
r15.grid(row=17, column=7)

#Guideline [GRADE]
Label(window, text="Guideline",bg="#d98cb3").grid(row=2,column=11)
Label(window, text="Grade :").grid(row=3,column=9)
Label(window, text="Grade :").grid(row=4,column=9)
Label(window, text="Grade :").grid(row=5,column=9)
Label(window, text="Grade :").grid(row=6,column=9)
Label(window, text="Grade :").grid(row=7,column=9)
Label(window, text="Grade :").grid(row=8,column=9)
Label(window, text="Grade :").grid(row=9,column=9)
Label(window, text="Grade :").grid(row=10, column=9)
Label(window, text="Grade :").grid(row=11, column=9)
Label(window, text="Grade :").grid(row=12, column=9)
Label(window, text="Grade :").grid(row=13, column=9)
Label(window, text="Grade :").grid(row=14, column=9)

#Guideline [LETTER]
Label(window, text="A ").grid(row=3,column=10)
Label(window, text="A-").grid(row=4,column=10)
Label(window, text="B+").grid(row=5,column=10)
Label(window, text="B ").grid(row=6,column=10)
Label(window, text="B-").grid(row=7,column=10)
Label(window, text="C+").grid(row=8,column=10)
Label(window, text="C ").grid(row=9,column=10)
Label(window, text="C-").grid(row=10, column=10)
Label(window, text="D+").grid(row=11, column=10)
Label(window, text="D ").grid(row=12, column=10)
Label(window, text="D-").grid(row=13, column=10)
Label(window, text="F ").grid(row=14, column=10)

#Guideline [GRADE VALUE]
Label(window, text="Grade Value :").grid(row=3,column=12)
Label(window, text="Grade Value :").grid(row=4,column=12)
Label(window, text="Grade Value :").grid(row=5,column=12)
Label(window, text="Grade Value :").grid(row=6,column=12)
Label(window, text="Grade Value :").grid(row=7,column=12)
Label(window, text="Grade Value :").grid(row=8,column=12)
Label(window, text="Grade Value :").grid(row=9,column=12)
Label(window, text="Grade Value :").grid(row=10, column=12)
Label(window, text="Grade Value :").grid(row=11, column=12)
Label(window, text="Grade Value :").grid(row=12, column=12)
Label(window, text="Grade Value :").grid(row=13, column=12)
Label(window, text="Grade Value :").grid(row=14, column=12)

#Guideline [FLOATING VALUE]
Label(window, text="4.00").grid(row=3,column=13)
Label(window, text="3.75").grid(row=4,column=13)
Label(window, text="3.50").grid(row=5,column=13)
Label(window, text="3.00").grid(row=6,column=13)
Label(window, text="2.75").grid(row=7,column=13)
Label(window, text="2.50").grid(row=8,column=13)
Label(window, text="2.00").grid(row=9,column=13)
Label(window, text="1.75").grid(row=10, column=13)
Label(window, text="1.50").grid(row=11, column=13)
Label(window, text="1.00").grid(row=12, column=13)
Label(window, text="0.75").grid(row=13, column=13)
Label(window, text="0.00").grid(row=14, column=13)

#Gap
Label(window, text="   ").grid(row=18,column=3)


#Column 0
Label(window, text="   ").grid(row=2,column=0)
Label(window, text="   ").grid(row=4,column=0)
Label(window, text="   ").grid(row=6,column=0)
Label(window, text="   ").grid(row=8,column=0)
Label(window, text="   ").grid(row=10,column=0)
Label(window, text="   ").grid(row=12,column=0)
Label(window, text="   ").grid(row=14,column=0)
Label(window, text="   ").grid(row=16, column=0)

#Column 2
Label(window, text="   ").grid(row=2,column=2)
Label(window, text="   ").grid(row=4,column=2)
Label(window, text="   ").grid(row=6,column=2)
Label(window, text="   ").grid(row=8,column=2)
Label(window, text="   ").grid(row=10,column=2)
Label(window, text="   ").grid(row=12,column=2)
Label(window, text="   ").grid(row=14,column=2)
Label(window, text="   ").grid(row=16, column=2)

#Column 4
Label(window, text="   ").grid(row=2,column=4)
Label(window, text="   ").grid(row=4,column=4)
Label(window, text="   ").grid(row=6,column=4)
Label(window, text="   ").grid(row=8,column=4)
Label(window, text="   ").grid(row=10,column=4)
Label(window, text="   ").grid(row=12,column=4)
Label(window, text="   ").grid(row=14,column=4)
Label(window, text="   ").grid(row=16, column=4)

#Column 6
Label(window, text="   ").grid(row=2,column=6)
Label(window, text="   ").grid(row=3,column=6)
Label(window, text="   ").grid(row=4,column=6)
Label(window, text="   ").grid(row=5,column=6)
Label(window, text="   ").grid(row=6,column=6)
Label(window, text="   ").grid(row=7,column=6)
Label(window, text="   ").grid(row=8,column=6)
Label(window, text="   ").grid(row=9,column=6)

#Column 8
Label(window, text="             ").grid(row=10, column=8)
Label(window, text="             ").grid(row=11,column=8)
Label(window, text="             ").grid(row=12,column=8)
Label(window, text="             ").grid(row=13,column=8)
Label(window, text="             ").grid(row=10, column=8)
Label(window, text="             ").grid(row=11,column=8)
Label(window, text="             ").grid(row=12,column=8)
Label(window, text="             ").grid(row=13,column=8)

#Button [CALCULATE]
button1=Button(window, text="Calculate", bg="#00ff00", command=answer) 
button1.grid(row=25, column=14)

#Button [CLEAR]
button2=Button(window, text="Clear", bg="#00ffff", command=clear) 
button2.grid(row=25, column=15)

#Button [EXIT]
button3=Button(window, text="Exit", bg="#ff1a1a", command=exit) 
button3.grid(row=25, column=16)

window.mainloop()

