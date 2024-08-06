import sqlite3

connection = sqlite3.connect("hotel.db")

# creating table
query = '''
create table water_bottle_company (
    id int unique not null,
    size int not null,
    category varchar(20) not null,
    primary key (id)
 );
'''
connection.execute(query)

# inserting data
connection.execute("insert into water_bottle_company values (1,20,'medium');")
connection.execute("insert into water_bottle_company values (2,20,'small');")
connection.execute("insert into water_bottle_company values (3,30,'big');")

# select table
cursor = connection.execute("select * from water_bottle_company")
for row in cursor:
    print(row)
    

connection.commit()
connection.close()
