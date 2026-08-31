#Control Structure

# a=10
# b=4
# if a>b:
#     print(f"{a} is greater")
# elif b>a:
#     print(f"{b} is greater")
# else:
#     print(f"Both are equal")

subject = "HTML"

match subject:
    case "HTML":
        print("Hypertext Markup Language")
    case "CSS":
        print("Cascading Style Sheet")
    case _:
        print("Unknown")