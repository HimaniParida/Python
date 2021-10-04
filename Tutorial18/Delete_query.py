#Deleting a record 

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Highschool para'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")



#Preventing SQL injection

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Kalinga Nagar", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")