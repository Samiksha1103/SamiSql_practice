#from asyncio.windows_events import NULL
import mysql.connector
import csv
db=mysql.connector.connect(host="localhost", user="root", password="password",database="EMPLOYEE")
c=db.cursor()
c.execute("select ename, job from emp order by substr(job, length(job)-1)")
res=c.fetchall()
l=[]
for x in res:
    l.append(x)

file = open('g4g.csv', 'w+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(l)
#print(l)
#db.commit()
#c.execute("CREATE DATABASE EMPLOYEE")
db.close()