import copy
from functools import lru_cache

arr=[]
with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):   
        arr.append([char for char in line])

global arr2
arr2 = copy.deepcopy(arr)
# print(arr)

startIndex = arr[0].index("S")
activePaths = [(startIndex, 0)]

#pt 1
splits = 0
while len(activePaths):
    newActivePaths = []
    for path in activePaths:
        newCord = (path[0], path[1]+1)

        if newCord[1] >= len(arr):
            continue

        if newCord[0] < 0 or newCord[0] >= len(arr[newCord[1]]):
            continue
    
        if arr[newCord[1]][newCord[0]] == '.':
            newActivePaths.append(newCord)
            arr[newCord[1]][newCord[0]] = '|'

        elif arr[newCord[1]][newCord[0]] == '^':
            splits +=1
            newActivePaths.append((newCord[0] -1, newCord[1]-1))
            newActivePaths.append((newCord[0] +1, newCord[1]-1))

    activePaths = newActivePaths

print(splits)

# for i in range(len(arr)):
#     print(arr[i])

#pt2 

global hits
hits = []
@lru_cache(maxsize=None)
def rdive(cord):
    arr = arr2
    if cord[1] > len(arr) -1:
        return 1
    if cord[0] < 0 or cord[0] > len(arr[cord[1]])-1:
        return 0
    
    total = 0
    if arr[cord[1]][cord[0]] == '.':
        return rdive((cord[0], cord[1]+1))
    elif arr[cord[1]][cord[0]] == '^':
        total += rdive((cord[0]+1, cord[1]))
        total += rdive((cord[0]-1, cord[1]))
    
    hits.append([total, cord])
    return total


x = rdive((startIndex, 1))
print(x)
print(rdive.cache_info())
print(hits[400:500])




# activePaths = [{
#     'cord': (startIndex, 0),
#     'arr': arr2
# }]
# print(activePaths)

# badPath = 0
# change = True
# while change:
#     tmpActive = []
#     change = False
#     print(len(activePaths))
#     for index, path in enumerate(activePaths):
#         newCord = (path['cord'][0], path['cord'][1]+1)
#         arr = arr2

#         if newCord[1] >= len(arr):
#             tmpActive.append(activePaths[index])
#             continue

#         if newCord[0] < 0 or newCord[0] >= len(arr[newCord[1]]):
#             badPath +=1
#             continue

#         if arr[newCord[1]][newCord[0]] == '.':
#             #arr[newCord[1]][newCord[0]] = '|'
#             activePaths[index]['cord'] = newCord
#             change = True
#             tmpActive.append(activePaths[index])

#         elif arr[newCord[1]][newCord[0]] == '^':
#             tmpActive.append({
#                 'cord': (newCord[0] -1, newCord[1]-1)#,
#                 #'arr': copy.deepcopy(arr)
#             })
#             tmpActive.append({
#                 'cord': (newCord[0] +1, newCord[1]-1)#,
#                 #'arr': copy.deepcopy(arr)
#             })
#             change = True

#     activePaths = tmpActive

    # for i in range(len(activePaths)):
    #     print(activePaths[i]['cord'], 'here')
# print(len(activePaths), 'len')


# for path in activePaths:
#     for i in range(len(path['arr'])):
#         print(path['arr'][i])
