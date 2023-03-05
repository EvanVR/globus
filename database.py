# Danai Roumelioti, dr3248@drexel.edu
# CS530: dr3248, Assignment 2 

import sqlite3

class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)

    def select(self, sql, parameters = []):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        return c.fetchall()

    def execute(self, sql, parameters = []):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        self.conn.commit()

    def get_bikes(self):
        data = self.select(
            'SELECT * FROM bikes'
        )
        return [{
            'id': d[0],
            'name': d[1],
            'wheels': d[2],
            'size': d[3],
            'motor': d[4],
            'folding': d[5],
            'image': d[6],
            'available': d[7] 
        } for d in data]

    def update_bike(self, id, availability):
        self.execute('UPDATE bikes SET available=? WHERE id=?', [availability, id])

    def reset_bikes(self):
        self.execute('UPDATE bikes SET available=3')


    def close(self):
        self.conn.close()

