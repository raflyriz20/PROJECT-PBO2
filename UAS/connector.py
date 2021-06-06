import mysql.connector

class Database:
    __host = 'localhost'
    __user = 'root'
    __passwd = 'Abgtua789'
    __database = 'perusahaan'
    def __init__(self):
        self.db = mysql.connector.connect(
            host = Database.__host,
            user = Database.__user,
            passwd = Database.__passwd,
            database = Database.__database
            )
        self.cursor = self.db.cursor()

    def execute(self, query):
        if ('INSERT' in query) or ('DELETE' in query) or ('UPDATE' in query):
            self.cursor.execute(query)
            return self.commit()
        return self.cursor.execute(query)
        
    def commit(self):
        self.db.commit()
        return self.cursor.rowcount
        
    def fetchall(self, query):
        self.execute(query)
        return self.cursor.fetchall()

    def fetchone(self, query):
        self.execute(query)
        return self.cursor.fetchone()