import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user='root',
    password='password',
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS basicCRM")

print("Database created successfully")