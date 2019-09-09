factorial = int(input("Type in a number to see their factorial: "))
sum = 1
for i in range(1, factorial + 1):
    sum *= i
print(sum)