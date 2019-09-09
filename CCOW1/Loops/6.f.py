width = int(input("Type in the width: "))
height = int(input("Type in the height: "))
for i in range(height):
    for j in range(width):
        if (i == 0 or i == height - 1):
            print("*", end='')
        elif j == 0 or j == width - 1:
            print("*", end='')
        else:
            print(" ", end='')
        #if i == 0 or i == height - 1:
        #    print("*", end='')
    print()