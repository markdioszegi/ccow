a = int(input("Please type in the row of the triangle: "))
b = 1
c = a
for i in range(a):
    for k in range(c):
        print(" ", end='')
    for j in range(b): 
        #if (j < i + 1):
            print("*", end='')
        #print(" ", end='')
    b += 2
    c -= 1
    print()