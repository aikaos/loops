
summ = 0
val = 1
while summ < 1000:
    summ += val
    val += 1
print(summ)

n = 0
while True:
    num = int(input("Enter number: "))
    if num > 100:
         break
print("You entered more than 100")