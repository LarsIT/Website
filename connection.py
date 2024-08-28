import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="photos"
)

cursor = connection.cursor()
cursor.close()
connection.close()
