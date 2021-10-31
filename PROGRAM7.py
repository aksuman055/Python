#Create a CSV file by entering user-id and password, read and search the password for given userid.
import csv
with open('usip.csv','a',newline='') as f:
    data={}
    user1=(input("Enter your username:"))
    passw1=input("Enter password:")
    data['Username']=user1
    data['Password']=passw1
    writer=csv.writer(f)
    for key, value in data.items():
        writer.writerows([key,value])

with open('usip.csv','r') as f1:
    creader=csv.reader(f1)
    for red in creader:
        print(red)


    


