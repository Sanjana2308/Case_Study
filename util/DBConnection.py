import pyodbc

from util.PropertyUtil import PropertyUtil

# When new object -> new connection
class DBConnection:
    def __init__(self):
        conn_str = PropertyUtil.get_property_string()
        self.connection = pyodbc.connect(conn_str)
        self.cursor = self.connection.cursor()
        

    def close(self):
        self.cursor.close()
        self.connection.close()