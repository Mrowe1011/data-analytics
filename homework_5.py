import sqlite3

from sqlite3 import Error

conn = sqlite3.connect("data/homework_05.db")

cursor = conn.cursor()

sql = "insert into faculty values (19,'Dexter');"   
cursor.execute(sql)
sql = "insert into department values (3,'Criminology');"   
cursor.execute(sql)
sql = "insert into course values (24166,'Culture and Crime',19,3);"   
cursor.execute(sql)
sql = "insert into course values (24167,'Police and Society',19,3);"   
cursor.execute(sql)
sql = "insert into registration values (3,44040,'SPRING 2022');"
cursor.execute(sql)
sql = "insert into registration values (8,25385,'FALL 2023');"
cursor.execute(sql)
sql = "insert into registration values (11,25385,'SPRING 2022');"
cursor.execute(sql)
sql = "insert into registration values (2,25385,'SPRING 2023');"
cursor.execute(sql)
sql = "insert into registration values (11,44040,'SPRING 2022');"
cursor.execute(sql)
sql = "insert into registration values (8,44040,'SPRING 2022');"
cursor.execute(sql)
sql = "insert into registration values (2,44043,'SPRING 2022');"
cursor.execute(sql)
sql = "insert into registration values (8,44043,'SPRING 2022');"
cursor.execute(sql)
sql = "insert into registration values (3,24166,'FALL 2023');"
cursor.execute(sql)
sql = "insert into registration values (9,24166,'FALL 2022');"
cursor.execute(sql)
sql = "insert into registration values (4,24166,'FALL 2022');"
cursor.execute(sql)

sql = "delete from student where sid=6;"
cursor.execute(sql)
sql = "delete from registration where sid=6;"
cursor.execute(sql)
sql = "update course set fid=(select fid from faculty where name='Dragan') where cid = 25385"
cursor.execute(sql)

conn.commit()

conn.close()