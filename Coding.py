#Assign Variable
x = 0
SumGrade = 0
SumCredit = 0
Count = int(input("Enter Number Of Subject: "))

#While Loop
while x < Count:
    Subject = input("Enter Subject: ")
    Credit = int(input("Enter Credit: "))
    SumCredit = SumCredit + Credit
    Grade = float(input("Enter Grade: "))
    SumGrade = SumGrade + (Grade * Credit)

    #Increment
    x +=1

    #Formula
    Formula = SumGrade  / SumCredit

#Function 
def Cal_Value(Formula):
  "This function calculate CGPA by input user"
  if Formula >= 3.67 and Formula <=4.00: return "Dean List"
  elif Formula >= 2.75 and Formula <=3.66: return "Pass"
  elif Formula >= 2.00 and Formula <=2.74: return "Conditional Pass"
  else : return "Fail"

#Output
print("CGPA is {:0.2f} and Result is {}. Total Credit is {}".format(Formula,Cal_Value(Formula),SumCredit))



#Coding Combine With Python tkinter
import tkinter as tk

# Assign Tkinter
wd = tk.Tk()

# Window Size
wd.geometry("850x250")

# Assign Title
wd.title("MINI PROJECT")
title1=tk.Label(text="CGPA CALCULATOR",bg="#80ff00")
title1.grid(column=2,row=0)

# Function Grade
def Display():

    # Declare Objects For Entering Data 
    D0 = tk.Entry(wd) # Name
    D1 = tk.Entry(wd) # Matric
    D2 = tk.Entry(wd) # Number Of Subject
    D3 = tk.Entry(wd) # Subject
    D4 = tk.Entry(wd) # Credit
    D5 = tk.Entry(wd) # Grade
    D6 = tk.Entry(wd) # Total Credit // Entry Location
    D7 = tk.Entry(wd) # Total CGPA // Entry Location
    D8 = tk.Entry(wd) # Result // Entry Location

    # Assign Variables
    x = 0
    SumGrade = 0
    SumCredit = 0
    Credit = 0
    Grade = 0.00
    while x == D2:
        #Subject = input("Enter Subject: ") *D3
        #Credit = int(input("Enter Credit: ")) *D4
        #SumCredit = SumCredit + D4
        #Grade = float(input("Enter Grade: ")) *D5
        ## SumGrade = SumGrade + (D5 * D4) *Location Entry *D7 ##
        x +=1
        ## Formula = SumGrade  / SumCredit *Location Entry ##
    
    # D2 [NUMBER OF SUBJECT]
    if D2.get() == D2 :
        tk.Label(wd, text = D2).grid(row=5, column=4) 
        D2 = D2
    
    # D4 [CREDIT]
    if D4.get() == D4 : 
        tk.Label(wd, text = SumCredit).grid(row=5, column=4) 
        SumCredit = SumCredit + Credit

    # D5 [GRADE]
    if D5.get() == "A": 
        tk.Label(wd, text =4.00).grid(row=5, column=4) 
        SumGrade += 4.00
    if D5.get() == "A-": 
        tk.Label(wd, text =3.75).grid(row=5, column=4) 
        SumGrade += 3.75
    if D5.get() == "B+": 
        tk.Label(wd, text =3.50).grid(row=5, column=4) 
        SumGrade += 3.50
    if D5.get() == "B": 
        tk.Label(wd, text =3.00).grid(row=5, column=4) 
        SumGrade += 3.00
    if D5.get() == "B-": 
        tk.Label(wd, text =2.75).grid(row=5, column=4) 
        SumGrade += 2.75
    if D5.get() == "C+": 
        tk.Label(wd, text =2.50).grid(row=5, column=4) 
        SumGrade += 250
    if D5.get() == "C": 
        tk.Label(wd, text =2.00).grid(row=5, column=4) 
        SumGrade += 2.00
    if D5.get() == "C-": 
        tk.Label(wd, text =1.75).grid(row=5, column=4) 
        SumGrade += 1.75
    if D5.get() == "D": 
        tk.Label(wd, text =1.50).grid(row=5, column=4) 
        SumGrade += 1.50
    if D5.get() == "E": 
        tk.Label(wd, text =1.00).grid(row=5, column=4) 
        SumGrade += 1.00
    if D5.get() == "F": 
        tk.Label(wd, text =0.00).grid(row=5, column=4) 
        SumGrade += 0.00
    
    # Label [CREDIT]
    tk.Label(wd, text="Credit").grid(row=3, column=0)
    D4 = tk.Entry(wd).grid(row=3, column=1)

    # Label [GRADE]
    tk.Label(wd, text="Grade").grid(row=4, column=0)
    D5 = tk.Entry(wd).grid(row=4, column=1)

    # Label [TOTAL CREDIT]
    tk.Label(wd, text="Total Credit :").grid(row=3, column=3)
    tk.Label(wd, text=SumCredit + Credit).grid(row=3, column=4)
    #D6 = tk.Entry(wd).grid(row=3, column=4)

    # Label [TOTAL CGPA]
    tk.Label(wd, text="Total CGPA :").grid(row=4, column=3)
    tk.Label(wd, text=SumGrade + Grade).grid(row=4, column=4)
    #D7 = tk.Entry(wd).grid(row=4, column=4)

    # Label [RESULT]
    tk.Label(wd, text="Result :").grid(row=5, column=3)
    tk.Label(wd, text=(SumGrade/SumCredit)).grid(row=5, column=4)
    #D8 = tk.Entry(wd).grid(row=5, column=4)

#Function Result
#def Cal_Value():
    #"This function calculate CGPA by input user"
    #if SumGrade/SumCredit >= 3.67 and SumGrade/SumCredit <=4.00: return "Dean List"
    #elif SumGrade/SumCredit >= 2.75 and SumGrade/SumCredit <=3.66: return "Pass"
    #elif SumGrade/SumCredit >= 2.00 and SumGrade/SumCredit <=2.74: return "Conditional Pass"
    #else : return "Fail"

# Label [NAME]
tk.Label(wd, text="Name").grid(row=1, column=0)
D0 = tk.Entry(wd).grid(row=1, column=1)

# Label [MATRIC]
tk.Label(wd, text="Matric").grid(row=1, column=3)
D1 = tk.Entry(wd).grid(row=1, column=4)

# Label [NUMBER OF SUBJECT]
tk.Label(wd, text="Number of Subject").grid(row=2, column=0)
D2 = tk.Entry(wd).grid(row=2, column=1)

# Label [BUTTON]
button=tk.Button(wd, text="submit", bg="#ffbf00", command=Display) 
button.grid(row=9, column=5)

# Label [BUTTON1]
button1=tk.Button(wd, text="Exit", bg="#E74C3C", command=exit) 
button1.grid(row=9, column=7)

# Label [BUTTON2]
#button2=tk.Button(wd, text="Back", bg="#FF00FF", command=) 
#button2.grid(row=9, column=6)

wd.mainloop()


#helmy latest update 3 button with 3windows
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root = Tk()
    application=Rental_Inventory(root)
    root.mainloop()

#blank windows 1
class Window1:
    def __init__ (self,master):
        self.master.title("CGPA Calculator")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()

#3 buttons 
        self.btnLogin = Button(self.frame,text ="login", width =17, command =self.new_windows)
        self.btnlogin.grid(row=3,column=0)

        self.btnReset = Button(self.frame,text ="login", width =17, command =self.new_windows)
        self.btnReset.grid(row=3,column=0)

        self.btnExit = Button(self.frame,text ="login", width =17, command =self.new_windows)
        self.btnExit.grid(row=3,column=0)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)


class Window2:
    def __init__ (self,master):
        self.master.title("CGPA Calculator")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()

if __name__ == "_main_":
    main()


#latest update 19/8/20 at 4.14 P.M.
#by helmy

#from tkinter import*
import tkinter as tk
import tkinter.messagebox 
#from tkinter import tk


def main ():
    root =tk.Tk()
    app = Window1(root)
    #application = Rental_Inventory(root)
    #root.mainloop()

    
    
#blank windows 1
class Window1:
    def __init__ (self, master):
        self.master = master
        self.master.title("MINI PROJECT")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame = tk.Frame(self.master, bg="powder blue")
        self.frame.pack()

#2 buttons will pop up
# buttons about us and cgpa calculator

        self.lblTitle = tk.Label(self.frame, text= " WELCOME TO CGPA CALCULATOR", font=("arial",50,"bold"), bg="powder blue", fg="black")
        self.lblTitle.grid(row=0, columnspan=3, pady=40)


        self.btncgpa = tk.Button(self.frame,text ="CGPA CALCULATOR", width =17, command =self.new_window2)
        self.btncgpa.grid(row=2,column=1)
        
    def new_window2(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow)

#this windows will be open if the button click
class Window2:
    def __init__ (self, master):
        self.master = master
        self.master.title("MINI PROJECT")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = tk.Frame(self.master, bg="powder blue") 
        self.frame.pack()




#suspect this is might be the error
if __name__ == "__main__":

    main()



#Calculate Credit Code 19/8/2020 @ 5:01 PM
from tkinter import *
 
def cal_credit():
    res=int(r9.get())+int(r10.get())+int(r11.get())+int(r12.get())+int(r13.get())
    count.set(res)
 
window = Tk()
count=StringVar();
Label(window, text="Credit Input 1").grid(row=0, column=0)
Label(window, text="Credit Input 2").grid(row=1, column=0)
Label(window, text="Credit Input 3").grid(row=2, column=0)
Label(window, text="Credit Input 4").grid(row=3, column=0)
Label(window, text="Credit Input 5").grid(row=4, column=0)
Label(window, text="Total Credit: ").grid(row=5, column=0)
result=Label(window, text="", textvariable=count).grid(row=6, column=0)
 
r9 = Entry(window)
r10 = Entry(window)
r11 = Entry(window)
r12 = Entry(window)
r13 = Entry(window)
 
r9.grid(row=0, column=1)
r10.grid(row=1, column=1)
r11.grid(row=2, column=1)
r12.grid(row=3, column=1)
r13.grid(row=4, column=1)
 
b = Button(window, text="Calculate", command=cal_credit)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
window.mainloop()


#Latest Update: Full Coding CGPA [Long Coding] @22/8/2020 @17:46
#But did not show the result

from tkinter import*

#Assign Tk As Window
window = Tk()
window.title("MINI PROJECT")
window.geometry("1200x700")

#Total Credit Label
count = IntVar()
Grade = 0
Invert = count.get()

Label(window, text="Number").grid(row=0, column=0)
Label(window, text="1").grid(row=1, column=0)
Label(window, text="2").grid(row=3, column=0)
Label(window, text="3").grid(row=5, column=0)
Label(window, text="4").grid(row=7, column=0)
Label(window, text="5").grid(row=9, column=0)
Label(window, text="6").grid(row=11, column=0)
Label(window, text="7").grid(row=13, column=0)
Label(window, text="8").grid(row=15, column=0)

#Entry Credit
r0=Entry(window)
r8=Entry(window)
r9=Entry(window)
r10=Entry(window) 
r11=Entry(window) 
r12=Entry(window) 
r13=Entry(window)
r15=Entry(window)

#Entry Grade
r1=Entry(window) 
r2=Entry(window)
r3=Entry(window) 
r4=Entry(window) 
r5=Entry(window) 
r6=Entry(window) 
r7=Entry(window)
r14=Entry(window)

#Entry Subject
r16 = Entry(window)
r17 = Entry(window)
r18 = Entry(window)
r19 = Entry(window)
r20 = Entry(window)
r21 = Entry(window)
r22 = Entry(window)
r23 = Entry(window)

#Entry Boarder
r24 = Entry(window)
r25 = Entry(window)
r26 = Entry(window)

#Grade Value
r27 = Entry(window)
r28 = Entry(window)
r29 = Entry(window)
r30 = Entry(window)
r31 = Entry(window)
r32 = Entry(window)
r33 = Entry(window)
r34 = Entry(window)


def calculate():
    global Grade
    
    #Grade [r1]
    if r1.get() == "A": 
        Label(window)
        Grade += 4.00
    if r1.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r1.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r1.get() == "B": 
        Label(window)
        Grade += 3.00
    if r1.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r1.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r1.get() == "C": 
        Label(window)
        Grade += 2.00
    if r1.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r1.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r1.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r1.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r1.get() == "F": 
        Label(window) 
        Grade += 0.00

    #Grade [r2]
    if r2.get() == "A": 
        Label(window)
        Grade += 4.00
    if r2.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r2.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r2.get() == "B": 
        Label(window)
        Grade += 3.00
    if r2.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r2.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r2.get() == "C": 
        Label(window)
        Grade += 2.00
    if r2.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r2.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r2.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r2.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r2.get() == "F": 
        Label(window) 
        Grade += 0.00

    #Grade [r3]
    if r3.get() == "A": 
        Label(window)
        Grade += 4.00
    if r3.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r3.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r3.get() == "B": 
        Label(window)
        Grade += 3.00
    if r3.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r3.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r3.get() == "C": 
        Label(window)
        Grade += 2.00
    if r3.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r3.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r3.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r3.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r3.get() == "F": 
        Label(window) 
        Grade += 0.00

    #Grade [r4]
    if r4.get() == "A": 
        Label(window)
        Grade += 4.00
    if r4.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r4.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r4.get() == "B": 
        Label(window)
        Grade += 3.00
    if r4.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r4.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r4.get() == "C": 
        Label(window)
        Grade += 2.00
    if r4.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r4.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r4.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r4.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r4.get() == "F": 
        Label(window) 
        Grade += 0.00

    #Grade [r5]
    if r5.get() == "A": 
        Label(window)
        Grade += 4.00
    if r5.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r5.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r5.get() == "B": 
        Label(window)
        Grade += 3.00
    if r5.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r5.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r5.get() == "C": 
        Label(window)
        Grade += 2.00
    if r5.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r5.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r5.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r5.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r5.get() == "F": 
        Label(window) 
        Grade += 0.00

    #Grade [r6]
    if r6.get() == "A": 
        Label(window)
        Grade += 4.00
    if r6.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r6.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r6.get() == "B": 
        Label(window)
        Grade += 3.00
    if r6.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r6.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r6.get() == "C": 
        Label(window)
        Grade += 2.00
    if r6.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r6.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r6.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r6.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r6.get() == "F": 
        Tk.Label(window) 
        Grade += 0.00

    #Grade [r7]
    if r7.get() == "A": 
        Label(window)
        Grade += 4.00
    if r7.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r7.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r7.get() == "B": 
        Label(window)
        Grade += 3.00
    if r7.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r7.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r7.get() == "C": 
        Label(window)
        Grade += 2.00
    if r7.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r7.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r7.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r7.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r7.get() == "F": 
        Label(window) 
        Grade += 0.00
    
    #Grade [r14]
    if r14.get() == "A": 
        Label(window)
        Grade += 4.00
    if r14.get() == "A-": 
        Label(window)
        Grade += 3.75
    if r14.get() == "B+": 
        Label(window)
        Grade += 3.50
    if r14.get() == "B": 
        Label(window)
        Grade += 3.00
    if r14.get() == "B-": 
        Label(window) 
        Grade += 2.75
    if r14.get() == "C+": 
        Label(window) 
        Grade += 2.50
    if r14.get() == "C": 
        Label(window)
        Grade += 2.00
    if r14.get() == "C-": 
        Label(window)
        Grade += 1.75
    if r14.get() == "D+": 
        Label(window) 
        Grade += 1.50
    if r14.get() == "D": 
        Label(window) 
        Grade += 1.00
    if r14.get() == "D-": 
        Label(window) 
        Grade += 0.75
    if r14.get() == "F": 
        Label(window) 
        Grade += 0.00

    #Boarder
    #displayGrade = StringVar()
    #displayCredit = StringVar()
    #displayStatus = StringVar()

    #Boarder Entry
    #Total Credit
    #r24 = Entry(window, width=10, state=DISABLED, textvariable=displayCredit)
    #r24.grid(row=17, column=4)

    #Total Grade
    #r25 = Entry(window,width=10, state=DISABLED, textvariable=displayGrade)
    #r25.grid(row=18, column=4)

    #Status
    #r26 = Entry(window,width=10, state=DISABLED, textvariable=displayStatus)
    #r26.grid(row=19, column=4)
  

    #Display Grade
    Label(window, text="Total Grade :").grid(row=18,column=2)
    Label(window, text=str(Grade)).grid(row=18, column=4)

    #Display Credit
    Label(window, text="   Total Unit :").grid(row=17, column=2)
    Label(window, text="", textvariable=count).grid(row=17, column=4)
    
    #Convert
    
    "This function calculate CGPA by input user"
    #elif (Grade*counter)/counter >= 2.75 and (Grade*counter)/counter <=3.66: return "Pass"
    #elif (Grade*counter)/counter >= 2.00 and (Grade*counter)/counter <=2.74: return "Conditional Pass"
    #else : return "Fail"

    #Display Status
    Label(window, text="         Status :").grid(row=19, column=2)
    Label(window, text=(Score)).grid(row=19, column=4)   

    #Total Credit
    total=int(r0.get())+int(r8.get())+int(r9.get())+int(r10.get())+int(r11.get())+int(r12.get())+int(r13.get())+int(r15.get())
    count.set(total)

    #Button [EXIT]
    button2=Button(window, text="Exit", bg="lightgreen", command=exit) 
    button2.grid(row=21, column=15)

#Entry Credit
r0 = Entry(window)
r8 = Entry(window)
r9 = Entry(window)
r10 = Entry(window)
r11 = Entry(window)
r12 = Entry(window)
r13 = Entry(window)
r15 = Entry(window)

#Entry Grade
r1 = Entry(window)
r2 = Entry(window)
r3 = Entry(window)
r4 = Entry(window)
r5 = Entry(window)
r6 = Entry(window)
r7 = Entry(window)
r14 = Entry(window)

#Entry Subject
r16 = Entry(window)
r17 = Entry(window)
r18 = Entry(window)
r19 = Entry(window)
r20 = Entry(window)
r21 = Entry(window)
r22 = Entry(window)
r23 = Entry(window)

#Grade Value
r27 = Entry(window)
r28 = Entry(window)
r29 = Entry(window)
r30 = Entry(window)
r31 = Entry(window)
r32 = Entry(window)
r33 = Entry(window)
r34 = Entry(window)

#Guideline
Label(window, text="Guideline Grade \n& Grade Value").grid(row=0,column=13)
Label(window, text="Grade:").grid(row=2,column=11)
Label(window, text="Grade:").grid(row=3,column=11)
Label(window, text="Grade:").grid(row=4,column=11)
Label(window, text="Grade:").grid(row=5,column=11)
Label(window, text="Grade:").grid(row=6,column=11)
Label(window, text="Grade:").grid(row=7,column=11)
Label(window, text="Grade:").grid(row=8,column=11)
Label(window, text="Grade:").grid(row=9, column=11)
Label(window, text="Grade:").grid(row=10, column=11)
Label(window, text="Grade:").grid(row=11, column=11)
Label(window, text="Grade:").grid(row=12, column=11)
Label(window, text="Grade:").grid(row=13, column=11)

Label(window, text="A ").grid(row=2,column=12)
Label(window, text="A-").grid(row=3,column=12)
Label(window, text="B+").grid(row=4,column=12)
Label(window, text="B ").grid(row=5,column=12)
Label(window, text="B-").grid(row=6,column=12)
Label(window, text="C+").grid(row=7,column=12)
Label(window, text="C ").grid(row=8,column=12)
Label(window, text="C-").grid(row=9, column=12)
Label(window, text="D+").grid(row=10, column=12)
Label(window, text="D ").grid(row=11, column=12)
Label(window, text="D-").grid(row=12, column=12)
Label(window, text="F ").grid(row=13, column=12)

Label(window, text="Grade Value:").grid(row=2,column=14)
Label(window, text="Grade Value:").grid(row=3,column=14)
Label(window, text="Grade Value:").grid(row=4,column=14)
Label(window, text="Grade Value:").grid(row=5,column=14)
Label(window, text="Grade Value:").grid(row=6,column=14)
Label(window, text="Grade Value:").grid(row=7,column=14)
Label(window, text="Grade Value:").grid(row=8,column=14)
Label(window, text="Grade Value:").grid(row=9, column=14)
Label(window, text="Grade Value:").grid(row=10, column=14)
Label(window, text="Grade Value:").grid(row=11, column=14)
Label(window, text="Grade Value:").grid(row=12, column=14)
Label(window, text="Grade Value:").grid(row=13, column=14)

Label(window, text="4.00").grid(row=2,column=15)
Label(window, text="3.75").grid(row=3,column=15)
Label(window, text="3.50").grid(row=4,column=15)
Label(window, text="3.00").grid(row=5,column=15)
Label(window, text="2.75").grid(row=6,column=15)
Label(window, text="2.50").grid(row=7,column=15)
Label(window, text="2.00").grid(row=8,column=15)
Label(window, text="1.75").grid(row=9, column=15)
Label(window, text="1.50").grid(row=10, column=15)
Label(window, text="1.00").grid(row=11, column=15)
Label(window, text="0.75").grid(row=12, column=15)
Label(window, text="0.00").grid(row=13, column=15)

#Organizing [Grade Value]
Label(window, text="Grade Value").grid(row=0,column=8)
r27.grid(row=1, column=8)
r28.grid(row=3, column=8)
r29.grid(row=5, column=8)
r30.grid(row=7, column=8)
r31.grid(row=9, column=8)
r32.grid(row=11, column=8)
r33.grid(row=13, column=8)
r34.grid(row=15, column=8)

#Organizing [Unit]
Label(window, text="Unit").grid(row=0,column=6)
r0.grid(row=1, column=6)
r8.grid(row=3, column=6)
r9.grid(row=5, column=6)
r10.grid(row=7, column=6)
r11.grid(row=9, column=6)
r12.grid(row=11, column=6)
r13.grid(row=13, column=6)
r15.grid(row=15, column=6)

#Orgainizing [Grade]
Label(window, text="Grade").grid(row=0,column=4)
r1.grid(row=1, column=4)
r2.grid(row=3, column=4)
r3.grid(row=5, column=4)
r4.grid(row=7, column=4)
r5.grid(row=9, column=4)
r6.grid(row=11, column=4)
r7.grid(row=13, column=4)
r14.grid(row=15, column=4)

#Organizing [Subject]
Label(window, text="Subject").grid(row=0,column=2)
r16.grid(row=1, column=2)
r17.grid(row=3, column=2)
r18.grid(row=5, column=2)
r19.grid(row=7, column=2)
r20.grid(row=9, column=2)
r21.grid(row=11, column=2)
r22.grid(row=13, column=2)
r23.grid(row=15, column=2)

#Gap
Label(window, text="   ").grid(row=2,column=3)
Label(window, text="   ").grid(row=4,column=3)
Label(window, text="   ").grid(row=6,column=3)
Label(window, text="   ").grid(row=8,column=3)
Label(window, text="   ").grid(row=10,column=3)
Label(window, text="   ").grid(row=12,column=3)
Label(window, text="   ").grid(row=14,column=3)
Label(window, text="   ").grid(row=16, column=3)
Label(window, text="   ").grid(row=2,column=5)
Label(window, text="   ").grid(row=4,column=5)
Label(window, text="   ").grid(row=6,column=5)
Label(window, text="   ").grid(row=8,column=5)
Label(window, text="   ").grid(row=10,column=5)
Label(window, text="   ").grid(row=12,column=5)
Label(window, text="   ").grid(row=14,column=5)
Label(window, text="   ").grid(row=16, column=5)
Label(window, text="   ").grid(row=2,column=7)
Label(window, text="   ").grid(row=4,column=7)
Label(window, text="   ").grid(row=6,column=7)
Label(window, text="   ").grid(row=8,column=7)
Label(window, text="   ").grid(row=10,column=7)
Label(window, text="   ").grid(row=12,column=7)
Label(window, text="   ").grid(row=14,column=7)
Label(window, text="   ").grid(row=16, column=7)
Label(window, text="   ").grid(row=2,column=10)
Label(window, text="   ").grid(row=3,column=10)
Label(window, text="   ").grid(row=4,column=10)
Label(window, text="   ").grid(row=5,column=10)
Label(window, text="   ").grid(row=6,column=10)
Label(window, text="   ").grid(row=7,column=10)
Label(window, text="   ").grid(row=8,column=10)
Label(window, text="   ").grid(row=9,column=10)
Label(window, text="   ").grid(row=10, column=10)
Label(window, text="   ").grid(row=11,column=10)
Label(window, text="   ").grid(row=12,column=10)
Label(window, text="   ").grid(row=13,column=10)


#Button [SUBMIT]
button1=Button(window, text="Submit", bg="yellow", command=calculate) 
button1.grid(row=21, column=14)

#button3 = Button(window, text="Calculate", command=addNumbers)
#button3.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

window.mainloop()


#Latest Update: Full Coding CGPA [Short Coding] @22/8/2020 @17:48
#Still did not get the result/status
from tkinter import*
window = Tk()

window.geometry("1200x500")

#Unit
r0 = Entry (window) 
r8 = Entry (window) 
r9 = Entry (window) 
r10 = Entry (window) 
r11 = Entry (window) 
r12 = Entry (window) 
r13 = Entry (window) 
r15 = Entry (window) 

#Value Grade
r27 = Entry (window) 
r28 = Entry (window) 
r29 = Entry (window) 
r30 = Entry (window) 
r31 = Entry (window) 
r32 = Entry (window) 
r33 = Entry (window) 
r34 = Entry (window)

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

    Answer = (float(v1)*int(v9)) + (float(v2)*int(v10)) + (float(v3)*int(v11)) + (float(v4)*int(v12)) + (float(v5)*int(v13)) + (float(v6)*int(v14)) + (float(v7)*int(v15)) + (float(v8)*int(v16))
    Total_Unit = int(v9) + int(v10) + int(v11) + int(v12) + int(v13) + int(v14) + int(v15) + int(v16)
    Total_Grade = float(v1) + float(v2) + float(v3) + float(v4) + float(v5) + float(v6) + float(v7) + float(v8)
    Status = Answer / Total_Unit

    Label(window, text="Total Grade:").grid(row=16,column=1)
    Label(window, text=(Total_Grade)).grid(row=16, column=3)

    Label(window, text="Total Unit:").grid(row=17,column=1)
    Label(window, text=(Total_Unit)).grid(row=17, column=3)

    Label(window, text="CGPA:").grid(row=18,column=1)
    Label(window, text=(Status)).grid(row=18, column=3)

    Label(window, text="Status:").grid(row=19,column=1)
    #Label(window, text=(result)).grid(row=19, column=3)

#Organizing [Grade Value]
Label(window, text="Grade Value").grid(row=0,column=1)
r27.grid(row=1, column=1)
r28.grid(row=3, column=1)
r29.grid(row=5, column=1)
r30.grid(row=7, column=1)
r31.grid(row=9, column=1)
r32.grid(row=11, column=1)
r33.grid(row=13, column=1)
r34.grid(row=15, column=1)

#Organizing [Unit]
Label(window, text="Unit").grid(row=0,column=3)
r0.grid(row=1, column=3)
r8.grid(row=3, column=3)
r9.grid(row=5, column=3)
r10.grid(row=7, column=3)
r11.grid(row=9, column=3)
r12.grid(row=11, column=3)
r13.grid(row=13, column=3)
r15.grid(row=15, column=3)

button1=Button(window, text="Submit", bg="yellow", command=answer) 
button1.grid(row=21, column=3)

window.mainloop()

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

    #Covert Decimal Place
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

    #Codition ResultS
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


#from tkinter import*
import tkinter as tk
import tkinter.messagebox 
#from tkinter import tk
#using import tkinter as tk


def main ():
    root =tk.Tk()
    app = Window1(root)
    #application = Rental_Inventory(root)
    #root.mainloop()

    
    
#blank windows 1
class Window1:
    def __init__ (self, master):
        self.master = master
        self.master.title("MINI PROJECT")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="powder blue")
        self.frame = tk.Frame(self.master, bg="powder blue")
        self.frame.pack()

#2 buttons will pop up
# buttons about us and cgpa calculator

        self.lblTitle = tk.Label(self.frame, text= " WELCOME TO CGPA CALCULATOR", font=("arial",50,"bold"), bg="powder blue", fg="black")
        self.lblTitle.grid(row=0, columnspan=3, pady=40)


        self.btncgpa = tk.Button(self.frame,text ="CGPA CALCULATOR", width =17, command =self.new_window2)
        self.btncgpa.grid(row=2,column=1)
        
    def new_window2(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Window2(self.newWindow)

#this windows will be open if the button click
class Window2:
    def __init__ (self, master):
        self.master = master
        self.master.title("MINI PROJECT")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = tk.Frame(self.master, bg="powder blue") 
        self.frame.pack()




#suspect this is might be the error
if __name__ == "__main__":

    main()


#log in by helmy
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
    Button(login_success_screen, bg="yellow",text="CGPA CALCULATOR",pady=10).pack()

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