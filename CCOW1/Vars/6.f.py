coronas = [10, 5, 2, 1]
balance = int(input("Please type in a number: "))
leftover = 0
for i in range(4):
    a = balance // coronas[i]
    print("%i coronas: %i" % (coronas[i], a))
    balance = balance % coronas[i]
    #balance % coronas[i]