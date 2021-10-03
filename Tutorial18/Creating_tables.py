#Creating a table

import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


#Primary key 
import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

