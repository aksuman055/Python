#CS PRACTICAL
import pickle
mod='q'
while mod=='q':
    print('------MENU------')
    print('1.Write')
    print('2.Read')
    print('3.Search')
    print('4.Update')
    ch=input('Enter your choice:')
    if ch=='1':
        f=open('student.dat','wb')
        stu={}
        ram='p'
        while ram=='p':
            roll=int(input('Enter roll number:'))
            name=input('Enter name of student:')
            marks=float(input('Enter marks of student:'))
            stu['RollNo']=roll
            stu['Name']=name
            stu['Marks']=marks
            pickle.dump(stu,f)
            ram=input('Press "p" if you want to write more data')
        f.close()
        print('Written Successfully')

    if ch=='2':
        f=open('student.dat','rb')
        try:
            while True:
                var=pickle.load(f)
                print(var)
        except EOFError:
            f.close()

    if ch=='3':
        f=open('student.dat','rb')
        lst1=[]
        a=int(input('Enter roll number to be searched:'))
        lst1.append(a)
        found=False
        try:
            while True:
                stu=pickle.load(f)
                if stu['RollNo'] in lst1:
                    print(stu)
                    found=True
        except EOFError:
            if found==False:
                print('No records found..........')
            else:
                print('Searching Successful')
        f.close()

    if ch=='4':
        f=open('student.dat','rb+')
        stu={}
        lst2=[]
        rno=int(input('Enter Roll no. whose data is to be updated:'))
        mrks=float(input('Enter new marks:'))
        lst2.append(rno)
        found=False
        try:
            while True:
                rpos=f.tell()
                stu=pickle.load(f)
                if stu['RollNo'] in lst2:
                    stu['Marks']=mrks
                    f.seek(rpos)
                    pickle.dump(stu,f)
                    found=True
        except EOFError:
            if found==False:
                print('Sorry roll number not found')
            else:
                print('Marks updated successfully')
        f.close()

    mod=input('Press "q" to perform any task again')
print('--------THANK YOU--------')
