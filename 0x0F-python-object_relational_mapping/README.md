0x0F. Python - Object-relational mapping
Python
OOP
SQL
MySQL
ORM
SQLAlchemy
 By: Guillaume
 Weight: 1
 Ongoing second chance project - started Jun 16, 2023 6:00 AM, must end by Jun 25, 2023 6:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 0.0/165 mandatory & 0.0/32 optional
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%
Before you start…
Please make sure your MySQL server is in 8.0 -> How to install MySQL 8.0 in Ubuntu 20.04

Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
