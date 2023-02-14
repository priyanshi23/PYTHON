# This is a sample Python script.
import random
import numpy as np
first = []
d = 0
p = 0
print("This time table is for Computer Science 1st year Students for 1st semester")
print("ADRS20")
print("You can use the following abbrevations for the subjects:")
print("""[Computing Fundamentals A :CFA115D \nComputational Mathematics :COH115D
          \nPrinciples of Programming A PPA115D]""")
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
    time = ["8-9 ","9-10 ","10-11 ","11-12 ","12-1 ","1-2 ","2-3 ","3-4 "]
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
    print("TIME MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY")
    for i in range(R):
        print(time[i],end="")
        for j in range(C):
            print(matrix2[i][j],end="")
        print()



