import sqlite3 
conn = sqlite3.connect('assigenment')   #conn as connection handle object
cursor = conn.cursor()   #cursor object as a channel bet Python code and database file test
print cursor
#cursor.execute("create table users(id INTEGER PRIMARY KEY, name TEXT,phone TEXT, email TEXT unique, password TEXT)")
#cursor.execute("insert into users(name ,phone ,email, password ) values(?,?,?,?)",("Sham verma", "4546485446","sham_verma@gmail.com","tough123@password!!"))
#cursor.execute("insert into users(name ,phone ,email, password ) values(?,?,?,?)",("Ravi verma", "9923849335","ravi_verma@gmail.com","tough@password!!"))
#cursor.execute("insert into users(name ,phone ,email, password ) values(?,?,?,?)",("Sham1 verma", "4565565666","sham1_verma@gmail.com","tough1234@password!!"))
#cursor.execute("insert into users(name ,phone ,email, password ) values(?,?,?,?)",("Ravi1 verma", "9923355455","ravi1_verma@gmail.com","tough78787@password!!"))
result = cursor.execute("select * from users")
print "Result = ", result
print(result.fetchall())
"""
[(1, u'Sham verma', u'4546485446', u'sham_verma@gmail.com', u'tough123@password!!'), (2, u'Ravi verma', u'9923849335', u'ravi_verma@gmail.com', u'tough@password!!'), (3, u'Sham1 verma', u'4565565666', u'sham1_verma@gmail.com', u'tough1234@password!!'), (4, u'Ravi1 verma', u'9923355455', u'ravi1_verma@gmail.com', u'tough78787@password!!')]
"""
name=raw_input("Enter person name you want to search")
res=cursor.execute("select * from users where name=(?)",(name,))
print (res.fetchall())
conn.commit()
conn.close()
