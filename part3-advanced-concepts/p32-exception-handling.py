# try:
#     print(10/0)
# except NameError:
#     print("Name Error")
# except ZeroDivisionError as e:
#     print("Cannot divide by 0")
#     print(e)
# except:
#     print("Something went wrong")
# else:
#     print("if no exception")
# finally:
#     print("Always get executed")


# print(a) # NameError
# print(10/0) # ZeroDivisionError
# print("10"/5) - TypeError


# try:
#     print(10/0)
# except (NameError,ZeroDivisionError) :
#     print("Name Error or ZeroDivisionError")
# except:
#     print("Something went wrong")
# else:
#     print("if no exception")
# finally:
#     print("Always get executed")


# x=-5
# if x<0:
#     raise Exception("x must be greater than 0")

# #Developer A - Module Developer
# def f1(age):
#     if not type(age) is int:
#             raise TypeError("Only integers are allowed")
#     print(age)


# #Developer B - User of the module
# try:
#     f1("Hello") 
# except TypeError as e:
#      print(e)

######################################

class AgeError(Exception):
    pass

# #Developer A - Module Developer
def f1(age):
    if not type(age) is int:
            raise AgeError("Only integers are allowed")
    print(age)


# #Developer B - User of the module
try:
    f1("Hello") 
except AgeError as e:
     print(e)

