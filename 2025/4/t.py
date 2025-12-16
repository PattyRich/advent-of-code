
arr = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        tmp = []
        for char in line:
            tmp.append(char)
        arr.append(tmp)


def checkValid(x,y,arr):
    if x < 0 or y < 0:
        return False 
    if x > len(arr[0])-1:
        return False
    if y > len(arr)-1:
        return False
    
    if (arr[y][x]) == '@':
        return True
    return False

def checkSurrounding(x,y,arr):
    topLeft = (x-1, y-1)
    top = (x, y-1)
    topRight = (x+1, y-1)
    right = (x+1, y)
    bottomRight = (x+1, y+1)
    bottom = (x, y+1)
    bottomLeft = (x-1, y+1)
    left = (x-1, y)

    dir = [topLeft, top, topRight, right, bottomRight, bottom, bottomLeft, left]
    total = 0
    for direction in dir:
        if checkValid(direction[0], direction[1], arr):
            total +=1

    return total

total = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if checkSurrounding(j, i, arr) < 4 and arr[i][j] == '@':
            total +=1
print(total)


#pt2
total = 0
tmpCount = 1
while tmpCount > 0:
    tmpChange = []
    tmpCount = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if checkSurrounding(j, i, arr) < 4 and arr[i][j] == '@':
                total +=1
                tmpCount +=1
                tmpChange.append((i,j))
    for pt in tmpChange:
        arr[pt[0]][pt[1]] = '.'
    
print(total)

