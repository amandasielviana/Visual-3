import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_penjualann'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM kategori")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)