#from asyncio.windows_events import NULL
import mysql.connector
import csv
db=mysql.connector.connect(host="localhost", user="root", password="password",database="EMPLOYEE")
c=db.cursor()
# Sorting based on 2 characters of name
#c.execute("select ename, job from emp order by substr(job, length(job)-1)")

# Sorting of null value column
#c.execute("select ename, job, comm from emp order by 3")
#Sorting of null value column and other 

# c.execute("select ename, sal, comm from (select ename, sal, comm ,case when comm is null then 0 else 1 end as is_null from emp) order by is_null desc, comm")
c.execute("select ename , job, sal, comm from emp order by case when job ='salesman' then comm else sal end")
res=c.fetchall()
l=[]
for x in res:
    l.append(x)

file = open('sqlQueryToExcel.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(l)
#print(l)
#db.commit()
#c.execute("CREATE DATABASE EMPLOYEE")
db.close()  