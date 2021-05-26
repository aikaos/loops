y = int(input())
if y % 4 == 0:
    print("Високосный")
elif y % 100 == 0:
    if y % 400 != 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Обычный")
