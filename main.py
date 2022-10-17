
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])


# ******************************
# Make your Code
# ******************************
# finding the sum of row
sumRowResult = []
sumRow = 0

print("Sum of rows: ", end=" ")
for i in range(rnum):
    for j in range(cnum):
        sumRow += numbers[i][j]

    sumRowResult.append(sumRow)
    print(sumRow, end=" ")
    # reset
    sumRow = 0

print()
print("Sum of colums: ", end=" ")

# finding the sum of col
sumColResult = []
sumCol = 0
for x in range(cnum):
    for y in range(rnum):
        sumCol += numbers[y][x]

    sumColResult.append(sumCol)
    print(sumCol, end=" ")
    # reset
    sumCol = 0

print()
maxSumRow = sumRowResult.index(max(sumRowResult))
print(f"The row that has greatest sum: {maxSumRow}")

# finding the greatest number
maxNum = 0
for a in numbers:
    if maxNum < max(a):
        maxNum = max(a)

print(f"The greates number: {maxNum}")
