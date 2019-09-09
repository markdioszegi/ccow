routes = [[1,5,2,3,2,4,3], 
          [2,6,4,5,3,3,1]]
shortestRoute = []
#routes = list(map(int, routes))
min = 1
max = 1
for i in range(len(routes)):
    for j in range(len(routes[0])):
        if routes[i][j] > max:
            max = routes[i][j]
        if routes[i][j] < min:
            min = routes[i][j]
print("Max: {}, Min: {}".format(max, min))
min = 1
max = 1
#print(routes[-1][3])
print(len(routes[0]))
index = min
tmp = []
for i in range(len(routes[0])):
    if routes[1][i] == routes[0][i] + 1:
        print("good!")
        shortestRoute.append(routes[0][i])
        shortestRoute.append(routes[1][i])
        #shortestRoute.append(routes[0][i])
        #shortestRoute.append(routes[1][i])
print(shortestRoute)
a = 1
shortestRoute = set(shortestRoute)
print(shortestRoute)