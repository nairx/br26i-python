import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="broadridge"
)
mycursor = mydb.cursor()
# mycursor.execute("create table customers (name varchar(200), email varchar(200))")
sql = "insert into customers (name,email) values(%s, %s )"
val = ("Mike","mike@gmail.com")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, " record inserted")



