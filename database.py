import sqlite3

def database():
    connection = sqlite3.connect(database="school result management.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text)")
    connection.commit()
database()