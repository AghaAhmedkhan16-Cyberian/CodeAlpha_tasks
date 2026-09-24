import sqlite3

conn = sqlite3.connect("app.db")
conn.execute("CREATE TABLE users (username TEXT, password TEXT)")
conn.execute("INSERT INTO users VALUES ('admin', 'password123')")
conn.commit()
conn.close()
print("Database created.")