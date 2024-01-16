big_list = ["A:new", "B:now", "C:latter", "D:jangle", "E:maker"]
d_list = [["(down", "up)"], ["(lowndown", "eggs)"], ["(kondooo", "mallo)"], ["(kilele", "bomalo)"]]

num = 1
for p in big_list:
    print(p)
    for i in d_list[num - 1]:
        print(i)
num += 1  # Incrementing num inside the outer loop resets it for each iteration
