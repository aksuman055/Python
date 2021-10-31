#Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message
import pickle
print('1.Write')
print('2.Search')
bye=int(input('Enter your choice:'))

if bye==1:
    file1=open('student.dat','wb')
    dict1={}
    che='y'
    while che=='y':
        name=input('Enter name of the student:')
        rollno=int(input('Enter roll number'))
        dict1['Name']=name
        dict1['RollNo']=rollno
        pickle.dump(dict1,file1)
        che=input('Press y to continue writing')
    file1.close()    
    print('Written')

if bye==2:
    file1=open('student.dat','rb')
    a=int(input('Enter Roll no. of student to search:'))
    lst1=[]
    lst1.append(a)
    found=False
    try:
        while True:
            stu=pickle.load(file1)
            if stu['RollNo'] in lst1:
                print(stu)
                found=True
    except EOFError:
        if found==False:
            print('No record found')
        else:
            print('Search successful')
    file1.close()
    


