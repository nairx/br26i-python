import re 
# input_string  = "johngmail.com"
# pattern = '@'
# email = re.search(pattern,input_string)
# if email:
#     print("Valid Email")
# else:
#     print("Invalid Email")


# text = "This is Broadridge. I am from Broadridge."
# result = re.findall("Broadridge",text)
# print(result)


# text = "Broadridge. I am from Broadridge."
# result = re.match("Broadridge",text)
# if result:
#     print("Match found")


text = "Broadridge. I am from Broadridge."
result = re.sub("Broadridge","Broadridge Inc",text)
print(result)