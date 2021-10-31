#Remove all the lines that contain the character 'a' in a file and write it to another file
file1=open('testfile1.txt','r')
file2=open('testfile1copy.txt','w')
lst1=file1.readlines()
lst2=[]
for i in lst1:
    for j in i:
        if j=='a':
            lst2.append(i)
            break
lst3 = list(set(lst1) - set(lst2))
file2.writelines(lst3)
file2.close()


