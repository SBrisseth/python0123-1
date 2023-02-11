import sqlite3
class Conection:
    def __init__(self,file_db):
        self.con=sqlite3.connect(file_db)
    def getCursor(self):
        return self.con.cursor()
   
