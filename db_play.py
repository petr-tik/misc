#!/usr/bin/python
import sqlite3 as sql

conn = sql.connect('test.db')
print "Opened new db connection to test db"

conn.execute('''CREATE TABLE IF NOT EXISTS PLAYER
                ( ID INTEGER PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                EMAIL TEXT NOT NULL);''')

pls = [('Bob', 'Bob at gmail.com'), ('John', 'John at gmail.com')]

for c, v in enumerate(pls):
    conn.execute("INSERT INTO PLAYER (ID, NAME, EMAIL) \
            VALUES (?, ?, ?)", (c+1, v[0], v[1]))
        
conn.commit()


# with doesn't close connection - ALWAYS DO IT MANUALLY
conn.close()
