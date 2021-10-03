#Creating a database

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_database")


#Checking if database exists

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
  