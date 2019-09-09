matrix = [[1, 4, 7],
          [9, 2, 1],
          [1, 2, 3]]
print(len(matrix))
#a = 10
#matrix[0].append(a)
print(matrix)
sum = 0
for i in range(len(matrix)):
    for j in range(i + 1):
        if i == j:
            print(matrix[i][j], end='')
            sum += matrix[i][j]
    print()
print(sum)