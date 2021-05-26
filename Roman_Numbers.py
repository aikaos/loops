# Римские цифры
num = int(input("Enter number: "))
result = ''

# 90 -> 9
# 91 -> 1

if num == 100:
    result = 'C'
elif 0 < num < 100:

    # десятки
    a = num // 10

    if a == 9:
        result += 'XC'
    elif a == 8:
        result += 'LXXX'
    elif a == 7:
        result += 'LXX'
    elif a == 6:
        result += 'LX'
    elif a == 5:
        result += 'L'
    elif a == 4:
        result += 'XL'
    elif a == 3:
        result += 'XXX'
    elif a == 2:
        result += 'XX'
    elif a == 1:
        result += 'X'

    # единицы

    b = num % 10

    if b == 9:
        result += 'IX'
    elif b == 8:
        result += 'VIII'
    elif b == 7:
        result += 'VII'
    elif b == 6:
        result += 'VI'
    elif b == 5:
        result += 'V'
    elif b == 4:
        result += 'IV'
    elif b == 3:
        result += 'III'
    elif b == 2:
        result += 'II'
    elif b == 1:
        result += 'I'

print(result)