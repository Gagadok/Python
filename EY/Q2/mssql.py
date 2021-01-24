# SQL-queries and working with the database

import pyodbc

class Mssql:
    
    # Initialize the class so that when creating an object of this class,
    # it is enough to write Mssql ("table_name")
    def __init__(self, database, server="WIN-430ABT40FDH"):
        self.cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                                   "Server=" + server + ";"
                                   "Database=" + database + ";"
                                   "Trusted_Connection=yes;")
    
    # SQL-query to add rows to the database
    def insert(self, table, columns, values, index_string_variables = []):
        requestString = "INSERT INTO " + table + " ("
        for i in columns:
            requestString += str(i) + ", "
        requestString = requestString[:-2]
        requestString += ") VALUES ("
        for index, val in enumerate(values):
            if len(index_string_variables) > 0:
                if str(index) in index_string_variables:
                    requestString += "'" + str(val) + "', "
                else:
                    requestString += str(val) + ", "
            else:
                requestString += str(val) + ", "
        requestString = requestString[:-2]
        requestString += ");"
        return requestString
    
    # SQL-query to clear the table and reset the ID
    def delete(self, table):
        requestString = "DELETE FROM " + table + "\n"
        requestString += "DBCC CHECKIDENT ('" + table + "', RESEED, 0)"
        return requestString
    
    # Sample request
    def select(self, column, table, condition = ""):
        requestString = "SELECT "
        for i in column:
            requestString += str(i) + ", "
        requestString = requestString[:-2]
        requestString += " FROM " + table
        if len(condition) > 0:
            requestString += " WHERE " + condition + ";"
        return requestString
    
    # Executing a request to clear the table and reset the id
    def to_clear_the_table(self, table):
        dbCursor = self.cnxn.cursor()
        dbCursor.execute(self.delete(table))
        self.cnxn.commit()
        print("Таблица " + table + " очищена")
    
    # Executing a query to load rows in the database
    def loading_data(self, table, columns, values, index_string_variables = []):
        dbCursor = self.cnxn.cursor()
        dbCursor.execute(self.insert(table, columns, values, index_string_variables))
        self.cnxn.commit()
        
    # Loading data from the database
    def getting_data(self, column, table, condition = ""):
        dbCursor = self.cnxn.cursor()
        dbCursor.execute(self.select(column, table, condition))
        result = dbCursor.fetchall()
        self.cnxn.commit()
        return result