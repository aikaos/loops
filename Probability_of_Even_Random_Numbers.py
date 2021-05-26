# Probability of Even random numbers

from random import randrange

q = 0


for i in range(1000):
    number = randrange(1001)
    if number % 2 == 0:
        q += 1
print(q / 10)