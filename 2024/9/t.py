result = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        for char in line:
            result.append(int(char))

res = []


for i in range(len(result)):
    if (i%2 == 0):
        index = int(i / 2)
        for i in range(result[i]):
            test = str(index)
            # for char in test:
            #     res.append(int(char))
            res.append(index)
    else:
        for i in range(result[i]):
            res.append('.')

res2 = res.copy()

rightTracker = len(res) -1
for i in range(len(res)):
    if res[i] == '.':
        for j in range(rightTracker, i, -1):
            rightTracker = j
            #print(res[j], len(res), j)
            if res[j] != '.':
                res[i] = res[j]
                res[j] = '.'
                break

sum = 0
for i in range(len(res)):
    if (res[i]) != '.':
        sum += i * res[i]

print(sum)

def getState(res):
    state = []
    for i in range(len(res)):
        if res[i] == '.' and res[i-1] != '.':
            count = 0
            curI = i
            for j in range(i, len(res), 1):
                if res[j] == '.':
                    count+=1
                    i = j
                else:
                    break
            state.append((curI, count))
    return state
     
#print(res2)

count = 0
for i in range(len(res2) -1, 0, -1):
    char = res2[i]
    if char == '.':
        continue
    count +=1
    if res2[i-1] == char:
        continue
    else:
        state = getState(res2)
        #print(state)
        #print(count, char)
        for set in state:
            if (set[0]) > i:
                break
            if set[1] >= count:
                for j in range(count):
                    res2[set[0] + j] = char
                for j in range(count):
                    res2[i+j] = '.'
                break
        count = 0
        #print(res2)

sum2 = 0
for i in range(len(res2)):
    if (res2[i]) != '.':
        sum2 += i * res2[i]

print(sum2)
        



