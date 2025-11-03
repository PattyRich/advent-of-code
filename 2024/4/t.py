


array=[]

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        row = []
        for element in line:
            row.append(element)
        array.append(row)

def check(array,tuple1, tuple2, tuple3, tuple4):
    if (tuple1[0] < 0 or tuple1[0] >= len(array)) or (tuple1[1] < 0 or tuple1[1] >= len(array[0])):
        return False
    if (tuple2[0] < 0 or tuple2[0] >= len(array)) or (tuple2[1] < 0 or tuple2[1] >= len(array[0])):
        return False
    if (tuple3[0] < 0 or tuple3[0] >= len(array)) or (tuple3[1] < 0 or tuple3[1] >= len(array[0])):
        return False
    if (tuple4[0] < 0 or tuple4[0] >= len(array)) or (tuple4[1] < 0 or tuple4[1] >= len(array[0])):
        return False
    if array[tuple1[0]][tuple1[1]] == 'X' and array[tuple2[0]][tuple2[1]] == 'M' and array[tuple3[0]][tuple3[1]] == 'A' and array[tuple4[0]][tuple4[1]] == 'S':
        return True

    
def checkDirections(x,y,array):
    total = 0

    #left
    if check(array,(x,y),(x-1,y),(x-2,y),(x-3,y)):
        total +=1
    #left-up
    if check(array,(x,y),(x-1,y+1),(x-2,y+2),(x-3,y+3)):
        total +=1
    #up
    if check(array,(x,y),(x,y+1),(x,y+2),(x,y+3)):
        total +=1
    #right-up
    if check(array,(x,y),(x+1,y+1),(x+2,y+2),(x+3,y+3)):
        total +=1
    #right
    if check(array,(x,y),(x+1,y),(x+2,y),(x+3,y)):
        total +=1
    #right-down
    if check(array,(x,y),(x+1,y-1),(x+2,y-2),(x+3,y-3)):
        total +=1
    #down
    if check(array,(x,y),(x,y-1),(x,y-2),(x,y-3)):
        total +=1
    #left-down
    if check(array,(x,y),(x-1,y-1),(x-2,y-2),(x-3,y-3)):
        total +=1
    return total

def checkDirections2(x,y,array, tuple1, tuple2, tuple3, tuple4):
    if (tuple1[0] < 0 or tuple1[0] >= len(array)) or (tuple1[1] < 0 or tuple1[1] >= len(array[0])):
        return False
    if (tuple2[0] < 0 or tuple2[0] >= len(array)) or (tuple2[1] < 0 or tuple2[1] >= len(array[0])):
        return False
    if (tuple3[0] < 0 or tuple3[0] >= len(array)) or (tuple3[1] < 0 or tuple3[1] >= len(array[0])):
        return False
    if (tuple4[0] < 0 or tuple4[0] >= len(array)) or (tuple4[1] < 0 or tuple4[1] >= len(array[0])):
        return False

    if array[x][y] != 'A':
        return False
    
    topLeft = array[tuple1[0]][tuple1[1]]
    topRight = array[tuple2[0]][tuple2[1]]
    bottomRight = array[tuple3[0]][tuple3[1]]
    bottomLeft = array[tuple4[0]][tuple4[1]]
    acceptable = ['M', 'S']
    if topLeft not in acceptable or topRight not in acceptable or bottomRight not in acceptable or bottomLeft not in acceptable:
        return False
    if topLeft == bottomRight:
        return False
    if topRight == bottomLeft:
        return False
    all = [topLeft, topRight, bottomRight, bottomLeft]
    if all.count('M') != 2 or all.count('S') != 2:
        return False
    return True


total = 0
xdashmas = 0
for i in range(len(array)):
    for j in range(len(array[0])):
        total += checkDirections(i,j,array)
        if checkDirections2(i,j,array,(i-1,j+1),(i+1,j+1),(i+1,j-1),(i-1,j-1)):
            xdashmas += 1
print(total)
print(xdashmas)