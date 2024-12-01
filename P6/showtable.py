import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_penjualann'
)

mycursor = mydb.cursor()
mycursor.execute('desc kategori')

for x in mycursor:
    print(x)