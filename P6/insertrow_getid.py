import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_penjualann'
)

mycursor = mydb.cursor()
sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
val = ("10", "Sayur")
mycursor.execute(sql, val)

mydb.commit()
print("1 record inserted, ID: ", mycursor.lastrowid)