#this is absolutely attrocious but it works.... please don't judge me off this

arr = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        tmp = []
        for char in line:
            tmp.append(char)
        arr.append(tmp)

d = {}

def checkNeighbors(x,y,arr):
    total = 0
    #left
    if x-1 >= 0:
        total += 0 if arr[y][x-1] == arr[y][x] else 1
    else:
        total +=1
    #right
    if x < len(arr[y])-1:
        total += 0 if arr[y][x+1] == arr[y][x] else 1
    else:
        total +=1
    #up
    if y-1 >= 0:
        total += 0 if arr[y-1][x] == arr[y][x] else 1
    else:
        total +=1
    #down
    if y < len(arr)-1:
        total += 0 if arr[y+1][x] == arr[y][x] else 1
    else:
        total +=1
    return total

def checkLeft(x,y,arr, letter):
    if x-1 >= 0:
        if arr[y][x-1] == letter:
            return True
    return False

def checkRight(x,y,arr, letter):
    if x < len(arr[y])-1:
        if arr[y][x+1] == letter:
            return True
    return False

def checkUp(x,y,arr, letter):
    if y-1 >= 0:
        if arr[y-1][x] == letter:
            return True
    return False

def checkDown(x,y,arr, letter):
    if y < len(arr)-1:
        if arr[y+1][x] == letter:
            return True
    return False

def assignGroup(x,y,arr, cords):
    #left
    if x-1 >= 0:
        if not (x-1,y) in cords and arr[y][x-1] == arr[y][x]:
            cords.append((x-1,y))
            cords = assignGroup(x-1,y,arr,cords)
    #right
    if x < len(arr[y])-1:
        if not (x+1,y) in cords  and arr[y][x+1] == arr[y][x]:
            cords.append((x+1,y))
            cords = assignGroup(x+1,y,arr,cords)
    #up
    if y-1 >= 0:
        if not (x,y-1) in cords  and arr[y-1][x] == arr[y][x]:
            cords.append((x,y-1))
            cords = assignGroup(x,y-1,arr,cords)
    #down
    if y < len(arr)-1:
        if not (x,y+1) in cords  and arr[y+1][x] == arr[y][x]:
            cords.append((x,y+1))
            cords = assignGroup(x,y+1,arr,cords)

    return cords

groups = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        check = False
        for group in groups:
            if (j,i) in group:
                check = True
        if not check:
            groups.append(assignGroup(j,i,arr,[(j,i)]))

        group = None

        for x in range(len(groups)):
            if (j,i) in groups[x]:
                group = arr[i][j] + str(x)

        if group not in d:
            d[group] = {'occurances': 0, 'perimeter': 0}
        perim = checkNeighbors(j,i, arr)
        d[group]['occurances'] +=1
        d[group]['perimeter'] += perim


total = 0
for key in d.keys():
    total += d[key]['occurances'] * d[key]['perimeter']

print(d)
print(total)

#part 2
total2 = 0
for group in groups:
    wallsLeft = {}
    wallsRight = {}
    wallsUp = {}
    wallsDown = {}
    for pt in group:
        if (pt[0]+1, pt[1]) in group and (pt[0]-1, pt[1]) in group and (pt[0], pt[1]+1) in group and (pt[0], pt[1]-1) in group:
            #surrounded by like chars aka we don't have walls
            continue
        
        letter = arr[pt[1]][pt[0]]
        #left
        c = False
        if checkLeft(pt[0], pt[1], arr, letter):
            c = True
        for key in wallsLeft.keys():
            wall = wallsLeft[key]
            if (pt[0],pt[1]) in wall:
                c = True
        if not c:
            wallTemp = [(pt[0],pt[1])]
            y = pt[1]
            while True:
                y +=1
                if (pt[0], y) in group:
                    if checkLeft(pt[0],y,arr,letter):
                        break
                    wallTemp.append((pt[0],y))
                else:
                    break
            y = pt[1]
            while True:
                y -=1
                if (pt[0], y) in group:
                    if checkLeft(pt[0],y,arr,letter):
                        break
                    wallTemp.append((pt[0],y))
                else:
                    break
            wallsLeft['l' + letter + str(len(wallsLeft.keys()))] = wallTemp


        #right
        c = False
        if checkRight(pt[0], pt[1], arr, letter):
            c = True
        for key in wallsRight.keys():
            wall = wallsRight[key]
            if (pt[0],pt[1]) in wall:
                c = True
        if not c:
            wallTemp = [(pt[0],pt[1])]
            y = pt[1]
            while True:
                y +=1
                if (pt[0], y) in group:
                    if checkRight(pt[0],y,arr,letter):
                        break
                    wallTemp.append((pt[0],y))
                else:
                    break
            y = pt[1]
            while True:
                y -=1
                if (pt[0], y) in group:
                    if checkRight(pt[0],y,arr,letter):
                        break
                    wallTemp.append((pt[0],y))
                else:
                    break
            wallsRight['r' + letter + str(len(wallsRight.keys()))] = wallTemp


        #up
        c = False
        if checkUp(pt[0], pt[1], arr, letter):
            c = True
        for key in wallsUp.keys():
            wall = wallsUp[key]
            if (pt[0],pt[1]) in wall:
                c = True
        if not c:
            wallTemp = [(pt[0],pt[1])]
            x = pt[0]
            while True:
                x +=1
                if (x, pt[1]) in group:
                    if checkUp(x,pt[1],arr,letter):
                        break
                    wallTemp.append((x,pt[1]))
                else:
                    break
            x = pt[0]
            while True:
                x -=1
                if (x, pt[1]) in group:
                    if checkUp(x,pt[1],arr,letter):
                        break
                    wallTemp.append((x,pt[1]))
                else:
                    break
            wallsUp['u' + letter + str(len(wallsUp.keys()))] = wallTemp


        #down
        c = False
        if checkDown(pt[0], pt[1], arr, letter):
            c = True
        for key in wallsDown.keys():
            wall = wallsDown[key]
            if (pt[0],pt[1]) in wall:
                c = True
        if not c:
            wallTemp = [(pt[0],pt[1])]
            x = pt[0]
            while True:
                x +=1
                if (x, pt[1]) in group:
                    if checkDown(x,pt[1],arr,letter):
                        break
                    wallTemp.append((x,pt[1]))
                else:
                    break
            x = pt[0]
            while True:
                x -=1
                if (x, pt[1]) in group:
                    if checkDown(x,pt[1],arr,letter):
                        break
                    wallTemp.append((x,pt[1]))
                else:
                    break
            wallsDown['d' + letter + str(len(wallsDown.keys()))] = wallTemp

    wallCount = len(wallsDown.keys()) + len(wallsUp.keys()) +len(wallsLeft.keys()) +len(wallsRight.keys())
    total2 += len(group) * wallCount
    #print(len(group) * wallCount)
    #print(wallsDown, wallsLeft, wallsRight, wallsUp)
    #print(wallsRight)
print(total2)