# find a maximum number among entered numbers

a = int(input("Enter any number: "))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print("Max number: ", m)