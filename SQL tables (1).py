import mysql.connector as a
con = a.connect(host="localhost",
              user="root",
              passwd="root")
c = con.cursor()
sql1 = "create database school1"
c.execute(sql1)
sql2 = "use school1"
c.execute(sql2)
sql3 = "create table cattendance (date varchar(10),class varchar(5), absent varchar(500))"
c.execute(sql3)
sql4 = "create table fees (name varchar(50),class varchar(5), roll varchar(5), month varchar(10) , fees varchar(10) , date varchar(10))"
c.execute(sql4)
sql5 = "create table salary (name varchar(50), month varchar(10), paid varchar(5))"
c.execute(sql5)
sql6 = "create table student (name varchar(50), class varchar(5), roll varchar(5), address varchar(50), ph varchar(10))"
c.execute(sql6)
sql7 = "create table tattendance (date varchar(10), absent varchar(500))"
c.execute(sql7)
sql8 = "create table teacher (name varchar(50), class varchar(5), roll varchar(5), address varchar(50), ph varchar(10), acno varchar(20))"
c.execute(sql8)
con.commit()
