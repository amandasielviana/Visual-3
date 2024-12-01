import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_penjualann'
)

mycursor = mydb.cursor()
sql = "DELETE FROM kategori where id ='4'"
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record(s) deleted successfully!")