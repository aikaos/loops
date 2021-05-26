# Number in word

number = int(input('number: '))

if number == 1000:
    result = 'тысяча'
elif 0 < number < 1000:
    # сотни
    if number // 100 != 0:
        num = number // 100

        if num == 9:
            result = 'девятьсот '
        elif num == 8:
            result = 'восемьсот '
        elif num == 7:
            result = 'семьсот '
        elif num == 6:
            result = 'шестьсот '
        elif num == 5:
            result = 'пятьсот '
        elif num == 4:
            result = 'четыресто '
        elif num == 3:
            result = 'тристо '
        elif num == 2:
            result = 'двести '
        elif num == 1:
            result = 'сто '
    # десятки
    if 10 < number % 100 < 20:
        num = number % 100

        if num == 11:
            result += 'одиннадцать '
        elif num == 12:
            result += 'двенадцать '
        elif num == 13:
            result += 'тринадцать '
        elif num == 14:
            result += 'четырнадцать '
        elif num == 15:
            result += 'пятнадцать '
        elif num == 16:
            result += 'шестнадцать '
        elif num == 17:
            result += 'семнадцать '
        elif num == 18:
            result += 'восемнадцать '
        elif num == 19:
            result += 'девятнадцать '

    else:
        if number // 10 % 10 != 0:
            num = number // 10 % 10

            if num == 9:
                result += 'девяносто '
            elif num == 8:
                result += 'восемьдесят '
            elif num == 7:
                result += 'семьдесят '
            elif num == 6:
                result += 'шестьдесят '
            elif num == 5:
                result += 'пятьдесят '
            elif num == 4:
                result += 'сорок '
            elif num == 3:
                result += 'тридцать '
            elif num == 2:
                result += 'двадцать '
            elif num == 1:
                result += 'десять '

        # единицы
        if number % 10 != 0:
            num = number % 10

            if num == 9:
                result += 'девять '
            elif num == 8:
                result += 'восемь '
            elif num == 7:
                result += 'семь '
            elif num == 6:
                result += 'шесть '
            elif num == 5:
                result += 'пять '
            elif num == 4:
                result += 'четыре '
            elif num == 3:
                result += 'три '
            elif num == 2:
                result += 'два '
            elif num == 1:
                result += 'один '

print(result)
