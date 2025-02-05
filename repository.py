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
                f"""
                CREATE TABLE IF NOT EXISTS {self.table} (
                    name TEXT,
                    artist TEXT,
                    file TEXT,
                    PRIMARY KEY (name, artist)
                )
                """
            )
            connection.commit()
    
    def clear(self):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM {self.table}"
            )
            connection.commit()

    def insert(self, js):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO {self.table} (name, artist, file) VALUES (?, ?, ?) ",
                (js["name"], js["artist"], js["file"])
            )
            connection.commit()
            return cursor.rowcount
    
    def lookup(self, name, artist):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT * FROM {self.table} WHERE (name, artist) = (?, ?)",
                (name, artist), 
            )
            row = cursor.fetchone()
            if row:
                return { "name":row[0], "artist":row[1], "file":row[2] }
            else:
                return None
    
    def delete(self, name, artist):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM {self.table} WHERE (name, artist) = (?, ?)",
                (name, artist), 
            )
            connection.commit()
            return cursor.rowcount
    
    def get_all(self):
         with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT name FROM {self.table}", 
            )
            rows = cursor.fetchall()
            if rows:
                return { "names":[row[0] for row in rows] }
            else:
                return None
