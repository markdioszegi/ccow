passed = False
while not passed:
    billAmount = input("Bill amount: ")
    tipRate = input("Tip rate: ")
    try:
        billAmount = float(billAmount)
        tipRate = float(tipRate)
        passed = True
    except ValueError:
        print("Please type in a number!")
tip = billAmount * (tipRate / 100)
total = billAmount + tip
#print(total)
print("Tip: ${:.2f}\nTotal: ${:.2f}".format(tip, total))