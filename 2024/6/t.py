import copy 
def checkEdge(x,y,array):
    if (x==0 or y==0 or x==(len(array)-1) or y == (len(array)-1)):
        return True
    return False


array = []
with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        row = []
        for char in line:
            row.append(char)
        array.append(row)

x = 0
y = 0
for i in range(len(array)):
    for j in range (len(array[i])):
        if array[i][j] == '^':
            x = i
            y = j

def runSet(x,y,array, printPatrol = False):
    curr = '^'
    patrolledArea = []
    steps = 0
    while True:
        steps +=1
        if (steps > 10000):
            return False
        if checkEdge(x,y,array):
            patrolledArea.append((x,y))
            break
        
        if curr == '^':
            if array[x-1][y] != '#':
                if (x,y) not in patrolledArea and printPatrol:
                    patrolledArea.append((x,y))
                x-=1
            else:
                curr = '>'

        if curr == '>':
            if array[x][y+1] != '#':
                if (x,y) not in patrolledArea and printPatrol:
                    patrolledArea.append((x,y))
                y+=1
            else:
                curr = 'v'

        if curr == 'v':
            if array[x+1][y] != '#':
                if (x,y) not in patrolledArea and printPatrol:
                    patrolledArea.append((x,y))
                x+=1
            else:
                curr = '<'

        if curr == '<':
            if array[x][y-1] != '#':
                if (x,y) not in patrolledArea and printPatrol:
                    patrolledArea.append((x,y))
                y-=1
            else:
                curr = '^'
    
    if printPatrol:
        print(len(patrolledArea))
    
    return True


runSet(x,y,array,True)

loops = 0
for i in range(len(array)):
    print(i)
    for j in range(len(array[i])):
        if (array[i][j]) != '^':
            arrayCopy = copy.deepcopy(array)
            arrayCopy[i][j] = '#'
        else:
            continue
        if not runSet(x,y,arrayCopy):
            loops +=1
print(loops)

    
