import csv

# with open("students.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age"])
#     writer.writerow(["John",21])
#     writer.writerow(["Amy",23])
#     writer.writerow(["Mike",23])


# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open("students.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# data = [
#  {"Name": "John", "Age": 20, "Course": "Python"},
#  {"Name": "Bob", "Age": 22, "Course": "Java"}
# ]

# with open("students1.csv","w",newline="") as file:
#     fieldnames=["Name","Age","Course"]
#     writer = csv.DictWriter(file,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

with open("students1.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie",25,"Reactjs"])