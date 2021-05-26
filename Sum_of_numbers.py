# Ввести число любой длины.
# Вывести на экран сумму его цифр.

sumn = 0
num = int(input("Enter any number: "))

while num != 0:
    last_num = num % 10
    num = num // 10
    sumn += last_num


print(sumn)

