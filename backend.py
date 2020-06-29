import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS investment (id INTEGER PRIMARY KEY, name text, investment_type text, interest float, start_date text, end_date text)")
        self.conn.commit()

    def insert(self, name, investment_type, interest, start_date, end_date):
        self.cur.execute("INSERT INTO investment VALUES (NULL, ?, ?, ?, ?, ?)", (name, investment_type, interest, start_date, end_date))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM investment")
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    def search(self, name="", investment_type="", interest="", start_date="", end_date=""):
        self.cur.execute("SELECT * FROM investment WHERE name=? OR investment_type=? OR interest=? OR start_date=? OR end_date=?", (name, investment_type, interest, start_date, end_date))
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM investment WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, investment_type, interest, start_date, end_date):
        self.cur.execute("UPDATE investment SET name=?, investment_type=?, interest=?, start_date=?, end_date=? where id=?", (name, investment_type, interest, start_date, end_date, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
