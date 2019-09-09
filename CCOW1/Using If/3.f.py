numbers = []
oddNumbers = []
evenNumbers = 0
txt = input("Please type in numbers separated by commas! (e.g. 1,2,3)\n")
for i in range(len(txt)):
        numbers = txt.split(',')
for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
                evenNumbers += 1
        elif int(numbers[i]) % 2 == 1:
                oddNumbers.append(numbers[i])
print("Number of odd Numbers: %i" % len(oddNumbers))
print("Number of even Numbers: %i" % evenNumbers)
oddNumbersSum = 0
for i in range(len(oddNumbers)):
        oddNumbersSum += int(oddNumbers[i])
print("The sum of the odd numbers: %i " % oddNumbersSum)