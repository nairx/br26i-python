import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
sql = """
insert into students(name,skill)
values(?,?)
"""
cursor.execute(sql,("Amy","Python"))
conn.commit()
conn.close()