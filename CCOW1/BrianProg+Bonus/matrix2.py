matrix1 = []
matrix2 = []
tmp = []
x = int(input("Number of rows: "))
y = int(input("Number of columns: "))
for i in range(x):
    for j in range(y):
        a = input("[MATRIX1] row %i/column %i value: " % (i, j))
        tmp.append(a)
    matrix1.append(tmp)
    tmp = []
for i in range(x):
    for j in range(y):
        a = input("[MATRIX2] row %i/column %i value: " % (i, j))
        tmp.append(a)
    matrix2.append(tmp)
    tmp = []
matrix3 = matrix1
ch = ''
count = 0
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        if not(matrix1[i][j].isdigit()):
            ch = matrix1[i][j]
            for k in range(len(matrix2)):
                for l in range(len(matrix2)):
                    if matrix2[k][l] == ch:
                        count += 1
            matrix3[i][j] = count
            count = 0
        else:
            matrix3[i][j] = matrix1[i][j]
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        print(matrix1[i][j], end='')
    print()
for i in range(len(matrix2)):
    for j in range(len(matrix2)):
        print(matrix2[i][j], end='')
    print()
for i in range(len(matrix3)):
    for j in range(len(matrix3)):
        print(matrix3[i][j], end='')
    print()
print(matrix1)
print(matrix2)
print(matrix3)