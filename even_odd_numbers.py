# Even and Odd numbers
a = int(input("Enter number: "))

even = 0
odd = 0

while a > 0:
    num = a % 10
    a = a // 10
    if num % 2 == 0:
        even += 1
    else:
        odd += 1


print(even)
print(odd)
