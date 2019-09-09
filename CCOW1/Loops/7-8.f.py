fibonacciNumbers = [1, 1]
b = 0
a = int(input("How many Fibonacci numbers do you want to see?: "))
for i in range(a-2):
    b = fibonacciNumbers[i + 1] + fibonacciNumbers[i]
    fibonacciNumbers.append(b)
print(fibonacciNumbers)
sum = 0
for i in range(len(fibonacciNumbers)):
    sum += fibonacciNumbers[i]
print("Their sum is: %i" % sum)
