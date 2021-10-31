#Create a binary file with roll number, name and marks. Input a roll number and
#update the marks
import pickle
print('1.Write')
print('2.Update')
print('3.Read')
bye=int(input('Enter choice'))
if bye==1:
    f=open('student5','wb')
    student={}
    ans='y'
    while ans=='y':
        rollno=int(input("Enter your rollno:"))
        name=input("Enter name:")
        marks=int(input("Enter marks:"))
        student['Rollno']=rollno
        student['Name']=name
        student['Marks']=marks
        pickle.dump(student,f)
        ans=input("Do you want to continue: y/n")
    f.close()

if bye==2:
    f=open('student5','rb+')
    stu={}
    lst1=[]
    rno=int(input('Enter Roll no:'))
    marks=int(input('Enter new marks:'))
    lst1.append(rno)
    found =False
    try:
        while True:
            rpos=f.tell()
            stu=pickle.load(f)
            if stu['Rollno'] in lst1:
                stu['Marks']=marks
                f.seek(rpos)
                pickle.dump (stu,f)
                found=True
    except EOFError :
        if found==False:
            print ("sorry ..no record found")
        else:
            print("Marks Updated Successfully")
    f.close()

if bye==3:
    f=open('student5','rb')
    try:
        while True:
            ab=pickle.load(f)
            print(ab)
    except EOFError:
        f.close()

else:
    print('Invalid Choice')
    
