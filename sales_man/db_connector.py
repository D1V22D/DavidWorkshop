import mysql.connector
import sqlite3
# Connect to MySQL
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@2004",
    database="sales_data"
)

sqlite_conn = sqlite3.connect('sales_data.db')
sqlite_cursor = sqlite_conn.cursor()
# Check if the "sales_data" database exists
def checkDb():
    mysql_cursor = mysql_conn.cursor()
    mysql_cursor.execute("SHOW DATABASES")
    databases = [db[0] for db in mysql_cursor.fetchall()]

    if "sales_data" not in databases:
        # Create the "sales_data" database if it doesn't exist
        mysql_cursor.execute("CREATE DATABASE sales_data")
        print("Database 'sales_data' created successfully.")
    else:
        print("Database 'sales_data' already exists.")
    
    mysql_conn.close()

checkDb()
sqlite_conn.commit()
sqlite_conn.close()