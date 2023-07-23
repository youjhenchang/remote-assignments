import mysql.connector

# Create db named assignment
assignment = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CCUEsql78562",
)

cursor = assignment.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS assignment")
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db[0])

# Create Table named user and contain at least 3 columns:id, email, password.
user = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CCUEsql78562",
    database="assignment"
)

cursor = user.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS user( 
        id INTEGER(10) AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255),
        password VARCHAR(255))"""
)

print(cursor)

user.commit()
user.close()
