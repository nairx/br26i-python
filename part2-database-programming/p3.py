import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("select * from students")
for row in cursor.fetchall():
    print(row[1],row[2])
conn.close()


# import sqlite3
# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()
# cursor.execute("select * from students")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# conn.close()