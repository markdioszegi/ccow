string = input("Write a sentence and it will tell you the amount of spaces: ")
numberOfSpaces = 0
for i in range(len(string)):
    if string[i] == ' ':
        numberOfSpaces += 1
print(numberOfSpaces)
