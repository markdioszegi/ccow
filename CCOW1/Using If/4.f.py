year = 0
while year <= 1800 or year >= 2099:
    year = int(input("Please enter a year between 1800 - 2099: "))
print(year)
A = year % 19
B = year % 4
C = year % 7
D = (19 * A + 24) % 30
E = (2 * B + 4 * C + 6 * D + 5) % 7
#exceptions
if E == 6 and D == 29:
    H = 50
elif E == 6 and D == 28 and A > 10:
    H = 49
else:
    H = 22 + D + E
if H <= 31:
    print("March %i" % H)
else:
    print("April %i" % (H - 31))