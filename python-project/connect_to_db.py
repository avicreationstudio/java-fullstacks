# importing sqlite3 module
import sqlite3

# create connection by using object
# to connect with hotel_data database
connection = sqlite3.connect('hotel_data.db')

# query to create a table named FOOD1
query = '''CREATE TABLE hotel 
( 
  id INT UNIQUE NOT NULL, 
  name VARCHAR(20) NOT NULL 
)'''
connection.execute(query)

# insert query to insert food details in 
# the above table
connection.execute("INSERT INTO hotel VALUES (1, 'cakes')")
connection.execute("INSERT INTO hotel VALUES (2, 'biscuits' )")
connection.execute("INSERT INTO hotel VALUES (3, 'chocos')")

print("All data in food table\n")

# create a cousor object for select query
cursor = connection.execute("SELECT * from hotel ")

# display all data from hotel table
for row in cursor:
	print(row)

connection.commit()
connection.close()
