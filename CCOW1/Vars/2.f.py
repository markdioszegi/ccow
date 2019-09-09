time = ["hour" , "minute", "second"]
day1 = [0, 0, 0]
day2 = [0, 0, 0]
#i = 0
def dayInput(day, num):
    i = 0
    while i < 3:
        if i == 0:
            day[i] = int(input("%i. time: %s\n" % (num, time[i])))
            if not(day[i] >= 0 and day[i] <= 24):
                print("Wrong number!")
                exit()
        elif i == 1:
            day[i] = int(input("%i. time: %s\n" % (num, time[i])))
            if not(day[i] >= 0 and day[i] <= 60):
                print("Wrong number!")
                exit()
        elif i == 2:
            day[i] = int(input("%i. time: %s\n" % (num, time[i])))
            if not(day[i] >= 0 and day[i] <= 60):
                print("Wrong number!")
                exit()
        i += 1
dayInput(day1, 1)
dayInput(day2, 2)
#------
def diffBetweenDaysInSecs(day1, day2):
    day1InSecs = day1[0] * 3600 + day1[1] * 60 + day1[2]
    day2InSecs = day2[0] * 3600 + day2[1] * 60 + day2[2]
    print(day1InSecs)
    print(day2InSecs)
    diff = abs(day1InSecs - day2InSecs)
    print("The difference between the two times in seconds: %i" % diff)
#-----
print(day1)
print(day2)
diffBetweenDaysInSecs(day1, day2)
