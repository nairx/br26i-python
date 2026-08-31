# i=1
# while i<=5:
#     print(i)
#     i=i+1


# i=1
# while i<=5:
#     print(i,end=" ")
#     i=i+1


# i=1
# while i<=10:
#     print(i)
#     i=i+1
#     if i==5:
#         break
#     print(f"Starting Loop {i}")


# i=1
# while i<=10:
#     i=i+1
#     if i==5:
#         continue
#     print(i)
#     print(f"Starting Loop {i}")


# while True:
#     name=input("Enter your name: ")
#     print(f"Hello {name}")
#     choice=input("Do you want to continue(y/n)?")
#     if choice!="y":
#         break


# i=1
# while i<=5:
#     number=input("Enter a number: ")
#     i=i+1
#     if number=="9":
#         break
# else:
#     print("Program Completed Successfully")

# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(5,36,5):
#     print(i)
# else:
#     print("Program Completed Successfully")

#Nested Loop
for i in range(5):
    for j in range(5):
        print(i,end=" ")
    print()