#walrus operator
# food=[]
# while True:
#     list=input("which foods do you like ? ").capitalize()
#     food.append(list)
#     if list== "Quit":
#         break

foods = []
while (food := input("What food do you like? ").capitalize()) != "Quit":
    foods.append(food)

print("List of foods:", foods)
