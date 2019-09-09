a = int(input("Enter the maximum number: "))
min = 0
max = 0
for i in range(a):
    b = int(input("Enter the %i. number: " % (i + 1)))
    if i == 0:
        min = b
        max = b
    if b < min:
        min = b
    if max < b:
        max = b
print("The smallest number is: %i." % min)
print("The highest number is: %i." % max)