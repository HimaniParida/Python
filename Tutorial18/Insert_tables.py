#Inserting tables 

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")


#Inserting Multiple rows 
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Himani', 'Highschool para'),
  ('Nitya', 'Prashanti vihar'),
  ('Vicky', 'Amby valley'),
  ('Shakti', 'Ekamra Nagar'),
  ('Taps', 'Kalinga Nagar'),
  ('Chandan', 'Jaydev Vihar')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")