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


import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("SmartphoneInventory.db")
 
cur = connection.cursor()
# Only uncomment out this line to create a NEW TABLE
# cur.execute("CREATE TABLE SmartPhones(Brand, Model, InternalMemory, ScreenSize, RAM, Color, Price, SKU, ReleaseDate)")
#print("Table Successfully Created!")

# Insert records into the newly created columns here
# cur.execute("""
#     INSERT INTO SmartPhones VALUES
#         ('Apple', 'iPhone 14', '128GB',  6.1, '8GB', 'Space Grey', 1099.99, 000001, '09/22/2022')
# """)
#print("Records have been added, refresh the DB to see changes.")



# insert many records into the DB here


# Query search here
res = cur.execute("SELECT Model FROM SmartPhones")
showResult = res.fetchall()
print(showResult)
# saves the changes to the database
#connection.commit()
