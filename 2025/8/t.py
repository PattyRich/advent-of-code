import math
import ast

arr=[]
with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):   
        line = line.split(",")
        line = [int(x) for x in line]
        arr.append(line)

#print(arr)

def distance(cord1, cord2):
    val = (cord1[0] - cord2[0])**2 + (cord1[1] - cord2[1])**2 + (cord1[2] - cord2[2])**2
    return abs(math.sqrt(val))

circuits = []
d = {}
size = 10
distances = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        dist = distance(arr[i], arr[j])
        indexes = (i,j)
        distances.append({'name': str(indexes), 'value': dist})

distances.sort(key=lambda x: x['value'])

last = -1
for x in range(int(len(distances)/2)):
    if (x%10000 == 0):
        print(x, len(distances))
    indexes = ast.literal_eval(distances[x * 2]['name'])
    iIn = False
    jIn = False
    iIndex = -1
    jIndex = -1
    i = arr[indexes[0]]
    j = arr[indexes[1]]
    eye = arr[indexes[0]]
    jay = arr[indexes[1]]

    if str(i) in d:
        iIn = True
        iIndex = d[str(i)]
    if str(j) in d:
        jIn = True
        jIndex = d[str(j)]

    if jIn and not iIn:
        circuits[jIndex].append(i)
        d[str(i)] = jIndex 
        last = eye[0] * jay[0]

    elif iIn and not jIn:
        circuits[iIndex].append(j)
        d[str(j)] = iIndex 
        last = eye[0] * jay[0]


    elif iIn and jIn and iIndex != jIndex:
        for i in range(len(circuits)):
            if i == iIndex or i == jIndex:
                continue
        circuits.append([*circuits[iIndex], *circuits[jIndex]])
        circuits[jIndex] = []
        circuits[iIndex] = []
        newIndex = len(circuits) -1
        for thing in circuits[-1]:
            d[str(thing)] = newIndex
        last = eye[0] * jay[0]

    elif not jIn and not iIn:
        circuits.append([i,j])
        newIndex = len(circuits) -1
        d[str(i)] = newIndex
        d[str(j)] = newIndex
        last = eye[0] * jay[0]

print(last)

    


lengths = []
for i in range(len(circuits)):
    lengths.append(len(circuits[i]))

lengths.sort(reverse=True)
print(circuits)
print(lengths)
print(lengths[0] * lengths[1] * lengths[2])










