import calendar

year = 1945

for month in range(1, 13):
    x = calendar.month(year, month)
    print(x, end=" ")
