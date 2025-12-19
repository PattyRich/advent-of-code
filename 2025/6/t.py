
arr = []
arr2 = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        arr2.append(line)
        line = line.split(" ")
        linefilter = [x for x in line if x!='']
        arr.append(linefilter)


#pt1
totals = [0 for _ in arr[0]]

for x in range(len(arr)-1):
    for y in range(len(arr[x])):
        if arr[-1][y] == '*':
            if totals[y] == 0:
                totals[y] = int(arr[x][y])
            else:
                totals[y] *= int(arr[x][y])
        else:
            totals[y] += int(arr[x][y])


print(totals)
print(sum(totals))


#pt2
print(arr2)
operators = [x for x in arr2[-1] if (x!='' and x!=' ')]
totals = [0 for _ in operators]
print(operators)

currOperator = 0
for i in range(len(arr2[0])):
    numCat = ''
    for j in range(len(arr2)-1):
        if arr2[j][i] != ' ':
            numCat += arr2[j][i]

    if numCat == '':
        currOperator +=1
        continue

    if operators[currOperator] == '*':
        if totals[currOperator] == 0:
            totals[currOperator] = int(numCat)
        else:
            totals[currOperator] *= int(numCat)
    else:
        totals[currOperator] += int(numCat)

print(totals)
print(sum(totals))