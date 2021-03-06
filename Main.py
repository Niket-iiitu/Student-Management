#-------------------------------------import-------------------------------------------------------
import datetime
import sys
import os
#--------------------------------------classes-----------------------------------------------------
#**************************************student*****************************************************
class student:
    def __init__ (self,name,gen,roll):
        self.name=name
        self.roll=roll
        self.gen=gen
        if roll[2]=='1':
            self.branch="CSE"
        elif roll[2]=="2":
            self.branch="ECE"
        elif roll[2]=="0":
            self.branch="IT"
        else:
            print("Incorrect roll number.")
            sys.exit()
#-------------------------------------FUNCTION-----------------------------------------------------
def op(rol,t): #t=0:Only the student information is given; t=1:Only the student grades are given;t=2:Grade line is given back as it is.
    with open(f"/home/niket/Desktop/Student_Management/Students/{rol}.txt") as data:
        data_=data.read()
    data_=data_.split("\n")
    id=data_[0].split("$")
    id_=student(id[0],id[1],id[2])
    if data_[1]!="":
        grade=data_[1].split("$")
    else:
        grade=None
    if t==0:
        return id_
    elif t==1:
        return grade
    elif t==2:
        return data_[1]
    elif t==3:
        return data_[0]
#-------------------------------------FRUNT--------------------------------------------------------
print("Welcome to IIITU student management software.")
print(datetime.datetime.now())
print("Task:")
print("A:Add a new student.")
print("G:Enter grades to a student.")
print("L:List of roll no.")
print("C:Compare students marks.")
print("E:Edit student profile.")
print("V:View a student's result.")
print("R:Remove a student.")
task=input("Code of your task:")
#-------------------------------------BACK---------------------------------------------------------
if task=="A":
    p=student(
        input("Name of the sbtudent(Full):"),
        input("Gender of student(M/F):"),
        input("Roll number assigned:")
    )
    with open(f"/home/niket/Desktop/Student_Management/Students/{p.roll}.txt",mode="w+") as stu_write:
        stu_write.write(f"{p.name}${p.gen}${p.roll}${p.branch}\n")
    print("Entry Done")
elif task=="R":
    p=input("Enter the roll number of student:")
    p_=input("Are you sure you want to remove the student(Y/N):")
    if p_=="Y":
        os.remove(f"/home/niket/Desktop/Student_Management/Students/{p}.txt")
        print("Student removed.")
    else:
        sys.exit()
elif task=="G":
    p=input("Enter the roll no of the student:")
    s=op(p,0)
    if s.branch=="CSE":
        in_bic=input("Biotechnology Marks:")
        in_ece=input("ECE Marks:")
        in_mat=input("Mathematics Marks:")
        in_che=input("Chemistry Marks:")
        with open(f"/home/niket/Desktop/Student_Management/Students/{p}.txt",mode="a") as stu_a:
            stu_a.write(f"{in_bic}${in_ece}${in_mat}${in_che}")
        print("Total marks:"+str(int(in_bic)+int(in_che)+int(in_ece)+int(in_mat)))
        print("Marks Added Sucessfully.")
    elif s.branch=="IT":
        in_bic=input("Biotechnology Marks:")
        in_evc=input("EVC Marks:")
        in_phy=input("Physics Marks:")
        in_mat=input("Mathematics Marks:")
        in_eng=input("English Marks:")
        with open(f"/home/niket/Desktop/Student_Management/Students/{p}.txt",mode="a") as stu_a:
            stu_a.write(f"{in_bic}${in_evc}${in_phy}${in_mat}${in_eng}")
        print("Total marks:"+str(int(in_bic)+int(in_evc)+int(in_phy)+int(in_mat)+int(in_eng)))
        print("Marks Added Sucessfully.")
    else:
        in_ee=input("EE Marks:")
        in_mat=input("Mathematics Marks:")
        in_eng=input("English Marks:")
        in_evc=input("EVC Marks:")
        in_phy=input("Physics marks:")
        with open(f"/home/niket/Desktop/Student_Management/Students/{p}.txt",mode="a") as stu_a:
            stu_a.write(f"{in_ee}${in_mat}${in_eng}${in_evc}${in_phy}")
        print("Total marks:"+str(int(in_ee)+int(in_mat)+int(in_eng)+int(in_evc)+int(in_phy)))
        print("Marks Added Sucessfully.")
elif task=="V":
    p=input("Roll no. of the student:")
    id_=op(p,0)
    grade=op(p,1)
    print(f"Roll no:{id_.roll}")
    print(f"Name:{id_.name}")
    print(f"Gender:{id_.gen}")
    print(f"Stream:{id_.branch}")
    if grade!=None:
        grade=[int(_) for _ in grade]
        print("Marks:-")
        if id_.branch=="CSE":
            print(f"Biotechnology:{grade[0]}")
            print(f"ECE:{grade[1]}")
            print(f"Mathematics:{grade[2]}")
            print(f"Chemistry:{grade[3]}")
            print(f"Total:{sum(grade)}")
        elif id_.branch=="IT":
            print(f"Biotechnology:{grade[0]}")
            print(f"EVC:{grade[1]}")
            print(f"Physics:{grade[2]}")
            print(f"Mathematics:{grade[3]}")
            print(f"English:{grade[4]}")
            print(f"Total:{sum(grade)}")
        else:
            print(f"EE:{grade[0]}")
            print(f"Mathematics:{grade[1]}")
            print(f"English:{grade[2]}")
            print(f"EVC:{grade[3]}")
            print(f"Physics:{grade[4]}")
            print(f"Total:{sum(grade)}")
    else:
        print("Markes not entered")
    print("Process Complete")
elif task=="E":
    p=input("Enter the student roll no.:")
    p_0=op(p,0)
    p_1=op(p,1)
    p_2=op(p,2)
    p_3=op(p,3)
    edit=input("Field to be edited:\n1:Name\n2:Grade\nN:None\n")
    if edit=="N":
        sys.exit()
    elif edit=="1":
        p_0.name=input("Enter new name:")
        res=input("Do you want to keep the changes(Y/N):")
        if res=="N":
            sys.exit()
        elif res=="Y":
            os.remove(f"/home/niket/Desktop/Student_Management/Students/{p}.txt")
            with open(f"/home/niket/Desktop/Student_Management/Students/{p}.txt",mode="w+") as p_add:
                p_add.write(f"{p_0.name}${p_0.gen}${p_0.roll}${p_0.branch}\n")
            with open(f"/home/niket/Desktop/Student_Management/Students/{p}.txt",mode="a") as p_add:
                print(p_1)
                if p_1!=None:
                    p_add.write(p_2)
        print("Editing Complete")
    elif edit=="2":
        if p_1==None:
            print("No result entered.")
            sys.exit()
        else:
            if p_0.branch=="CSE":
                branch=input("Subject->\n1:Biotechnology\n2:ECE\n3:Mathmetics\n4:Chemistry\n")
                p_1[int(branch)-1]=input("Enter the new marks:")
            elif p_0.branch=="IT":
                branch=input("Subject->\n1:Biotechnology\n2:EVC\n3:Physics\n4:Mathmetics\n5:English\n")
                p_1[int(branch)-1]=input("Enter the new marks:")
            else:
                branch=input("Subject->\n1:EE\n2:Mathemetics\n3:English\n4:EVC\n5:Physics\n")
                p_1[int(branch)-1]=input("Enter the new marks:")
            res=input("Do you want to keep the changes(Y/N):")
            if res=="Y":
                os.remove(f"/home/niket/Desktop/Student_Management/Students/{p}.txt")
                with open(f"/home/niket/Desktop/Student_Management/Students/{p}.txt",mode="w+") as res_w:
                    res_w.write(p_3)
                    res_w.write("\n")
                    n=0
                    while n<len(p_1):
                        res_w.write(f"{p_1[n]}")
                        n=n+1
                        if n!=len(p_1):
                            res_w.write("$")
    else:
        print("Wrong Entry")
elif task=="L":
    lis_p=os.listdir("/home/niket/Desktop/Student_Management/Students")
    lis_p.sort()
    lis_p=[_[0:5] for _ in lis_p]
    for _ in lis_p:
        print(_)
    print("List Complete")
elif task=="C":
    lis_p=os.listdir("/home/niket/Desktop/Student_Management/Students")
    lis_p.sort()
    branch=input("Enter the stream:\n1:CSE\n2:IT\n3:ECE\n")
    lis_p=[_[0:5] for _ in lis_p]
    if branch=="1":
        lis_p=list(filter(lambda s:s[2]=="1",lis_p))
        lis_val=[]
        sub=input("Subject->\n1:Biotechnology\n2:ECE\n3:Mathmetics\n4:Chemistry\n")
        operator=input("1:Marks in assending order\n2:Marks greater then a value\n3:markes less then a value\n")
        for _ in lis_p:
            lis_val.append(tuple([_,int(op(_,1)[int(sub)-1])]))
        lis_val.sort(key=lambda  x: x[1])
        if operator=="1":
            for (a,b) in lis_val:
                print(f"{a}:\t{b}")
        elif operator=="2":
            val=int(input("Enter the value:"))
            n=0
            while n<len(lis_val):
                if lis_val[n][1]<val:
                    lis_val.pop(n)
                n+=1
            print(f"Number of students:{len(lis_val)}")
            for (a,b) in lis_val:
                print(f"{a}:\t{b}")
        elif operator=="3":
            val=int(input("ENter the value:"))
            n=0
            while n<len(lis_val):
                if lis_val[n][1]>val:
                    lis_val.pop(n)
                n+=1
            print(f"Number of students:{len(lis_p)}")
            for (a,b) in lis_val:
                print(f"{a}:\t{b}")
        else:
            print("Wrong Entry")
else:
    print("Wrong Entry")




    '''
    Line entry 
    Infinite loop
    '''