#Update table 

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "my_database"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Prashanti vihar' WHERE address = 'Kalinga Nagar 2'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")