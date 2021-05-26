# Deposit
max_sum = 100000
curr_sum = 0
percent_sum = 0

for i in range(1, 13):
    payment = int(input("Payment: "))
    curr_sum += payment

    if i % 6 == 0:
        if curr_sum >= max_sum:
            break

print("Total:", curr_sum)
print("Percent:", percent_sum)
