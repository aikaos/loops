# find a number out of 10 attempts

from random import randrange
n = randrange(100)
i = 1
print("The computer thought of the number. Guess it. You have ten attempts.")
print(n)
for i in range(1, 10):
    x = int(input(str(i) + ':attempt: '))
    if x < n:
        print('More')
    if x > n:
        print('Less')
    elif n == x:
        print('You guessed it on the %d attempt ' % i)
        break
    i += 1
else:
    print('You have exhausted ten attempts. It was: ', n)
