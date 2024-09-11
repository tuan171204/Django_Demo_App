
import mysql.connector 

database = mysql.connector.connect(
    host = 'localhost',
    user = 'tuan', 
    password = '123456tuan'
    
)

# Create database cursor
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE tuandjango")

print("Successful !!")

