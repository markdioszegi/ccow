sides = [0, 0, 0]
#        a  b  c
numbers = (input("Enter the sides of a triangle (separated by commas): "))
if numbers.count(',') == 2:
    sides = numbers.split(',')
    sides = list(map(int, sides))
    if (sides[0] ** 2 + sides[1] ** 2) == sides[2] ** 2:
        print("Can be a rectangular triangle! :)")
    else:
        print("Can't be a rectangular triangle!")
    #print("good!")
else:
    print("Try again!")

print(sides)