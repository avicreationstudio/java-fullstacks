import sqlite3

# # -----------------------------------------
#        Mention your data base name
# # -----------------------------------------

class Logic:
    def createTable(db_name, tb_name):
        connection = sqlite3.connect(db_name)
        query = f'''
        CREATE TABLE IF NOT EXISTS {tb_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        '''
        connection.execute(query)
        connection.commit()
        connection.close()
    
    def insertTable(db_name, tb_name, column, value):
        connection = sqlite3.connect(db_name)
        query = f"INSERT INTO {tb_name} ( {column} ) VALUES ( '{value}' );"
        connection.execute(query)
        connection.commit()
        connection.close()

    def deleteTable(db_name,tb_name, id):
        connection = sqlite3.connect(db_name)
        query = f"DELETE FROM {tb_name} WHERE id={id} ;"
        connection.execute(query)
        connection.commit()
        connection.close()
    
    def updateTable(db_name,tb_name, id, value):
        connection = sqlite3.connect(db_name)
        query = f"UPDATE {tb_name} SET name='{value}' WHERE id={id} ;"
        connection.execute(query)
        connection.commit()
        connection.close()
    
    def selectTable(db_name,tb_name):
        connection = sqlite3.connect(db_name)
        query = f"SELECT * FROM {tb_name};"
        cursor = connection.execute(query)
        table = []
        for row in cursor:
            table.append(row)
        connection.close()
        return table
    
        
    