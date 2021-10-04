#Delete a table

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)


