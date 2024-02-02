#sort()
#sorted_function

students=(
    ("markson",19,"nigga"),
    ("amiyo",18,"uloop")
    
)
age=lambda ages:ages[1]
sorted_students=sorted(students,key=age,reverse=True)
for i in sorted_students:
    print(i)
