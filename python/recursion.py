# def add_one(num):
#     if (num >= 9):
#         return num + 1
#     total= num + 1
#     print(total)
#     return add_one(total)
# print(add_one(2))

password=input("put down your password >> ")
if len(password)<8:
    print("your password is too short!git !")
elif len(password) >10:
    print("your password is too long my guy")
else:
    print("good job")