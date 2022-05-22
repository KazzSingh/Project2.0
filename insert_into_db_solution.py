import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()
# host = os.environ.get("mysql_host")
# user = os.environ.get("mysql_user")
# password = os.environ.get("mysql_pass")
# database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    mysql_host=localhost
    mysql_user=root
    mysql_pass=password
    mysql_db=test
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record
sql = "INSERT INTO customers (f_name, l_name, cust_phone) VALUES (%s, %s, %s)"
val = [
    ("Jayson", "Cooper", "07656756752"),
    ("Leon", "Grundmann", "07123098123"),
    ("Greg", "Plant", "07098123098")
]
cursor.executemany(sql, val)
connection.commit()
print(cursor.rowcount, "was inserted")

cursor.execute("SELECT f_name, l_name, cust_phone FROM customers")
rows = cursor.fetchall()
for row in rows:
    print(f'First Name: {row[0]}, Last Name: {row[1]}, Age: {row[2]}')

cursor.close()
connection.close()
