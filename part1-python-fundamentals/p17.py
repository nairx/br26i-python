# numbers = [i for i in range(1,10)]
# print(numbers)

# numbers = [i for i in range(1,10) if i%2==0]
# print(numbers)


# numbers = {i for i in range(1,10) if i%2==0}
# print(numbers)


numbers = {f"ID{i}:{i}" for i in range(1,10)}
print(numbers)