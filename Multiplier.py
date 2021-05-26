# Multiplier test
from random import randrange

score = 0

for i in range(10):
    n1, n2 = randrange(2, 10), randrange(2, 10)
    print(n1, '*', n2, '?')
    ans = int(input(':'))
    if ans == n1 * n2:
        score += 10

print(score)
print("End")



