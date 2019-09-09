num = int(input("Please type in a number from 1 to 5: "))
if num >= 1 and num <=5:
    for i in range(num):
        for j in range(num):
            print(" %i" % ((i + 1) * (j + 1)), end='')
        print()