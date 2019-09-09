numbers = []
i = 0
sum = 0
#evenNumbers = []
while True:
    if (i % 2) == 0:
        if len(numbers) < 100:
                numbers.append(i)     
        else:
                break
    i += 1
for i in range(len(numbers)):
        sum += numbers[i]
print(sum)