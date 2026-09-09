from pathlib import Path

# path = Path("report1.txt")

# print(path.exists())

# print(path.is_file())

# folder = Path("temp")

# folder.mkdir(exist_ok=True)

# file = Path("reports/report1.txt")
# # file.write_text("Sales Repport")

# data = file.read_text()
# print(data)

# with open("report1.txt","r") as file:
#     data = file.read()

# if "john" in data.lower():
#     print("Joh exists in the file")



# from glob import glob
# files = glob("part1-python-fundamentals/*.py")
# # print(files)
# for file in files:
#     with open(file,"r") as f:
#         data = f.read()
#         if "john" in data.lower():
#             print(f"{file}-John exists in the file")

# folder = Path(".")
# for file in folder.glob("*.py"):
#     print(file)


# folder = Path(".")
# for file in folder.rglob("*.py"):
#     print(file)

file = Path("reports1.txt")
print(file.name)
print(file.suffix)
print(file.stem)
print(file.parent)