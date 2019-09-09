def challenge1():
    print("What is your name? ", end="")
    print("Hello, " + input() + ", nice to meet ya!")
def challenge2():
    names = ["Josh", "Jonathan", "Mark"]
    name = input("What is your name? ")
    if name == names[0]:
        print("Hello, {}, how's it going bruv?".format(name))
    elif name == names[1]:
        print("Hello, {}, we have a nice day, aren't we?".format(name))
    elif name == names[2]:
        print("Hello, {}, you rock at coding!".format(name))
    else:
        print("Hello, {}, nice to meet ya!".format(name))
#---
name = input("What is your name? ")
print("Hello, {}, nice to meet ya!".format(name))
challenge1()
challenge2()