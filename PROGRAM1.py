#Read a text file line by line and display each word separated by a #
file1=open('testfile.txt','r')
var1=file1.read()
okk=var1.split()
for i in okk:
    print(i,end='#')
