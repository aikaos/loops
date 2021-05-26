# Combination
max_n = int(input("Enter max number: "))
summ = int(input("Summ: "))


for i in range(1, max_n + 1):
    for j in range(1, max_n + 1):
        for k in range(1, max_n + 1):
            if i + j + k == summ:
                print(i, j, k)
