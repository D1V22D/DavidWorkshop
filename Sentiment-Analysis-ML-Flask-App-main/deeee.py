import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Admin@123")

# creating the cursor object
cur = myconn.cursor()

try:
    # Creating a table with name Employee having four columns i.e., name, id, salary, and department id
    dbs = cur.execute("show databases")
       # "create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
except:
    myconn.rollback()

myconn.close()