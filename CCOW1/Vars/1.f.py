price = int(input("How much for one kilogram?\n"))
quantity = int(input("How many apples do you want? %i corona(s) for one kilogram.\n" % price))
total = price * quantity
print("You have to pay %i corona(s)." % total)
