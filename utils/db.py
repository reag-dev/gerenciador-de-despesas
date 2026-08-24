from pathlib import Path
import sqlite3

class Database:    
    def __init__(self, name:str):
        self.name = Path(name)
        self.name.parent.mkdir(parents=True, exist_ok=True)        

    def exec_query(self, query, params=()):
        with sqlite3.connect(self.name) as con:
            cursor = con.cursor()            
            cursor.execute(query, params)
            return cursor.fetchall()
    
    def exec_queries(self, queries):
        with sqlite3.connect(self.name) as con:
            cursor = con.cursor()

            for query, params in queries:
                cursor.execute(query, params)

    
        
        
        
    