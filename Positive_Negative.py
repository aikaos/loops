# Positive & Negative numbers
a = int(input("Enter number: "))

if a == 0:
    print("Zero")
else:
    if a > 0:
        print("Positive")
    else:
        print("Negative")
    if abs(a) < 0:
        print("Single")
    else:
        if (abs(a) >= 0) and (abs(a) < 100):
            print("two-digits")
        else:
            print("three-digits or more")

