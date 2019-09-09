folds = int(input("Enter the number of folds: "))
for n in range(folds):
    for i in range(5):
        for j in range(5):
            if i == 0 or i == 5 - 1:
                print("*", end='')
            elif j == 0 or j == 5 - 1:
                print("*", end='')
            elif j == 2 and i == 2:
                print("@", end='')
            else:
                print(" ", end='')
        print()