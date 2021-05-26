# triangle
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

result = 'not exist'

if a + b < c:
    result = "Exist"

if b + c < a:
    result = "Exist"

if c + a < b:
    result = "Exist"

print(result)