# Savings
saving = int(input("How much do you want to save?: "))

res = 0

while saving > res:
    p = int(input("Payment:"))
    res += p
print('congratulations!',  res)
