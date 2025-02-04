import sqlite3

class Repository:
    def __init__(self, table):
        self.table = table
        self.database = self.table + ".db"
        self.make()

    def make(self):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table} " +
                "(name TEXT PRIMARY KEY, artist TEXT PRIMARY KEY, file TEXT)"
            )
            connection.commit()
