import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

sql = """
update students
set skill = "Java"
where id=1
"""

cursor.execute(sql)

conn.commit()

conn.close()