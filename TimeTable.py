import random
import numpy as np
from fpdf import FPDF

first = []
d = 0
p = 0

my_pdf = FPDF()
my_pdf.add_page()
my_pdf.set_font('Arial','B',16)
my_pdf.cell(200,10,txt="This time table is for Computer Science Students for 1st semester",ln=1,align="C")

print("This time table is for Computer Science Students for 1st semester \n")
print("ADRS20")
print("You can use the following abbrevations for the subjects:")
print("""[CFA115D : Computing Fundamentals A\n COH115D : Computational Mathematics \n PPA115D : Principles of Programming A 
    \n ADS216D : Advanced Discrete Structures \n CAO216D : Computer Architectiure and Organisation] \n DTP216D : Database Principles \n
      OOP216D Object Orineted Programming \n INT316D : Internet Programming \n MOB316D : Mobile Computing \n
       SWP316D : Software Project \n DBP316D : Database Programming """)
subnum = int(input("Enter number of subjects: "))
for i in range(0,subnum):
    sub= input("Enter Subjects:")
    f = int(input("Enter frequency"))
    d = d+f
    for i in range(0,f):
        first.append(sub)
if(d > 30):
    print("Invlaid input")
else:
    for i in range(0,30-d):
        lol = ""
        first.append(lol)
R = 6
C = 5
k = int(input("Enter number of time tables"))
for p in range(k):
    first1 = []
    matrix = []
    m = []
    time = ["8-9 ","9-10 ","10-11 ","11-12 ","12-1 ","1-2 "]
    for i in range(R):
        a = []
        for j in range(C):
            item = first[0]
            a.append(item)
            first.remove(item)
            first1.append(item)
        matrix.append(a)
        m = np.array(matrix)
        matrix1 = m.T
        for e in range(5):
            random.shuffle(matrix1[e])
        m1 = np.array(matrix1)
        matrix2 = m1.T
    for m in range(30):
        first.append(first1[m])
    print("-------TIME TABLE",end="")
    print(p+1,end="")
    print("------------")
    print("TIME \tMONDAY\tTUESDAY\tWEDNESDAY\tTHURSDAY\tFRIDAY")
    for i in range(R):
        my_pdf.cell(200, 10, (time[i] + "\t"), ln=1)
        print(time[i], end="\t")
        for j in range(C):
            print(matrix2[i][j], end=" ")

            my_pdf.cell(200, 10, matrix2[i][j] + " ", ln=1)
        print()
    my_pdf.output("myPDF.pdf")

