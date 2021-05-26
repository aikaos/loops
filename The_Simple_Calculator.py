# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.

print("Zero as Operation Sign Completes Program Work")
while True:
    s = input("Sign (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x= "))
        y = float(input("y= "))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Division by zero!")
    else:
        print("Wrong operation sign!")