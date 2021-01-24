# SQL-queries and working with the database

import pyodbc

class Mssql:
    
    # Initialize the class so that when creating an object of this class,
    # it is enough to write Mssql ("table_name")
    def __init__(self, database, server="WIN-430ABT40FDH"):
        self.cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
    
    # SQL-query to add rows to the database
    def insert(self, table, columns, values):
        requestString = "INSERT INTO " + table + " ("
        for i in columns:
            requestString += str(i) + ", "
        requestString = requestString[:-2]
        requestString += ") VALUES ("
        j = 0
        for i in values:
            if j <= 3:
                requestString += "'" + str(i) + "', "
                j += 1
            else:
                requestString += str(i) + ", "
        requestString = requestString[:-2]
        requestString += ");"
        return requestString
    
    # SQL-query to clear the table and reset the ID
    def delete(self, table):
        requestString = "DELETE FROM " + table + "\n"
        requestString += "DBCC CHECKIDENT ('" + table + "', RESEED, 0)"
        return requestString
    
    # Executing a request to clear the table and reset the id
    def to_clear_the_table(self, table):
        dbCursor = self.cnxn.cursor()
        dbCursor.execute(self.delete(table))
        self.cnxn.commit()
        print("Таблица " + table + " очищена")
    
    # Executing a query to load rows in the database
    def loading_data(self, table, columns, values):
        dbCursor = self.cnxn.cursor()
        dbCursor.execute(self.insert(table, columns, values))
        self.cnxn.commit()