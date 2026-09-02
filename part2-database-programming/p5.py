import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

sql = """
delete from students
where id=1
"""

cursor.execute(sql)

conn.commit()

conn.close()