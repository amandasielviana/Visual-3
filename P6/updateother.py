import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_penjualann'
)

mycursor = mydb.cursor()
sql = "UPDATE kategori SET name = %s WHERE id = %s"
adr = ("Snacks", "5")
mycursor.execute(sql, adr)

mydb.commit()
print(mycursor.rowcount, "record(s) updated successfully!")