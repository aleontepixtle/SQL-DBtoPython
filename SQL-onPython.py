##################################################################
# Author: Andrew Leon                                            # 
# Date 10/20/22                                                  #
# Purpose: to establish a connection to an SQL database and      #
# perform SQL queries within a python program                    #
##################################################################
# py -m venv venv to create a new virtual environment

# required modules
# sqlite3
# to view DB created please install extension SQLite Viewer from extensions Tab
# import sqlite3
# con = sqlite3.connect("tutorial.db")
# # cursor to execute SQL statements, like an actual mouse cursor for placement
# cur = con.cursor()

# #cur.execute("CREATE TABLE movie(Title, Year, Score)") # When creating a new table, datatypes are optional thanks to something called Flexible typing
# # YOUR ACTUAL SQL STATEMENT GOES HERE
# # SQLite3 creates a master DB to reference from
# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# res.fetchone() is None


from itertools import count
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("\n\n####################################", '\n',
              "Connection to SQLite DB successful", '\n',
              "####################################\n\n", sep="")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("SmartphoneInventory.db")
 
cur = connection.cursor()
# Only uncomment out this line to create a NEW TABLE
#ur.execute("CREATE TABLE SmartPhone(Brand, Model, InternalMemory, ScreenSize, RAM, Color, Price, Carrier, SKU, UPC)")
#print("Table Successfully Created!")

# Insert ONE set of data into the newly created columns here
# cur.execute("""
#     INSERT INTO SmartPhones VALUES
#         ('Apple', 'iPhone 14', '128GB',  6.1, '8GB', 'Space Grey', 1099.99, 000001, 'AT&T')
# """)
#print("Records have been added, refresh the DB to see changes.")



# insert MANY sets of data into the DB here
##############################################
# rows = [('Apple', 'iPhone 14', '128GB', 6.1, '8GB', 'Space Grey', 1099.99, 'AT&T', 'A10001A', 1000),
#     ('Apple', 'iPhone 14', '128GB', 6.1, '8GB', 'Deep Purple', 1099.99, 'AT&T', 'A10001A', 1001),
#     ('Apple', 'iPhone 14', '128GB', 6.1, '8GB', 'Alpine Green', 1099.99, 'AT&T', 'A10001A', 1002),
#     ('Apple', 'iPhone 14', '128GB', 6.1, '8GB', 'Space Grey', 1099.99, 'Verizon', 'A10001B', 2000),
#     ('Apple', 'iPhone 14', '128GB', 6.1, '8GB', 'Deep Purple', 1099.99, 'Verizon', 'A10001B', 2001),
#     ('Apple', 'iPhone 14', '128GB', 6.1, '8GB', 'Alpine Green', 1099.99, 'Verizon', 'A10001B', 2002),
#     ('Samsung', 'S22', '128GB', 6.6, '8GB', 'Phantom White', 999.99, 'AT&T', 'S10001A', 1000),
#     ('Samsung', 'S22', '128GB', 6.6, '8GB', 'Bora Purple', 999.99, 'AT&T', 'S10001A', 1001),
#     ('Samsung', 'S22', '128GB', 6.6, '8GB', 'Pink Gold', 999.99, 'AT&T', 'S10001A', 1002),
#     ('Samsung', 'S22', '128GB', 6.6, '8GB', 'Phantom White', 999.99, 'Verizon', 'S10001A', 2000),
#     ('Samsung', 'S22', '128GB', 6.6, '8GB', 'Bora Purple', 999.99, 'Verizon', 'S10001A', 2001),
#     ('Samsung', 'S22', '128GB', 6.6, '8GB', 'Pink Gold', 999.99, 'Verizon', 'S10001A', 2002)]

# Uncomment out to insert the data above
# cur.executemany("INSERT INTO SmartPhone VALUES(?,?,?,?,?,?,?,?,?,?);", rows)
# connection.commit()
#print("Data inserted Successfully")
###############################################


# Query search here
res = cur.execute('SELECT Brand, Model, Color, Price, Carrier FROM SmartPhone WHERE Price < 1000 AND Carrier = "Verizon"')
showResult = res.fetchall()
#print(showResult)

print('------------Your Query Below-------------','\n'
      '-------------SQL To Python---------------', '\n')

count = 0
for i in showResult:
    count +=1
    print(i)
print("\nTotal Number of Results", count)
print('\n')
connection.close()
# saves the changes to the database
#connection.commit()