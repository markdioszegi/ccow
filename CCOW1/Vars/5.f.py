coronas = [5, 2, 1]
wallet = [0, 0, 0]
balance = 0

for i in range(3):
    wallet[i] = int(input("How much of %i corona(s)? " % coronas[i])) 
    #print(wallet[i])
print(wallet)
for i in range(3):
    balance += int(coronas[i] * wallet[i])
    
print("Your total balance: %i coronas." % balance)