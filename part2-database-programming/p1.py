import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

sql = """
create table if not exists students(
id integer primary key autoincrement,
name text not null,
skill text not null
)
"""

cursor.execute(sql)

conn.commit()

conn.close()