import sqlite3

def commit_and_close_connection(conn):
    conn.commit()
    conn.close()

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS investment (id INTEGER PRIMARY KEY, name text, investment_type text, interest float, start_date text, end_date text)")
    commit_and_close_connection(conn)

def insert(name, investment_type, interest, start_date, end_date):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO investment VALUES (NULL, ?, ?, ?, ?, ?)", (name, investment_type, interest, start_date, end_date))
    commit_and_close_connection(conn)

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM investment")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="", investment_type="", interest="", start_date="", end_date=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM investment WHERE name=? OR investment_type=? OR interest=? OR start_date=? OR end_date=?", (name, investment_type, interest, start_date, end_date))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM investment WHERE id=?", (id,))
    commit_and_close_connection(conn)

def update(id, name, investment_type, interest, start_date, end_date):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE investment SET name=?, investment_type=?, interest=?, start_date=?, end_date=? where id=?", (name, investment_type, interest, start_date, end_date, id))
    commit_and_close_connection(conn)

connect()
