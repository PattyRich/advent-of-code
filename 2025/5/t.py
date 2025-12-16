
arr = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        arr.append(line)

ranges = []
ingredients = []

for line in arr:
    if '-' in line:
        s = line.split('-')
        ranges.append((int(s[0]), int(s[1])))
        continue
    if line == "\n" or line == '':
        continue
    ingredients.append(int(line))

#print(ranges,ingredients)

def checkRanges(ranges, target):
    for r in ranges:
        if target >= r[0] and target <= r[1]:
            return True
    return False

total = 0
for item in ingredients:
    if checkRanges(ranges, item):
        total +=1
print(total)

def combineRanges(x,y):
    # x will always have the lowest start value
    if x[0] > y[0]:
        tmp = x
        x = y
        y = tmp

    # ex: 1-2 4-5
    # two seperate ranges no overlap
    if x[1] < y[0] and x[1] != y[0]:
        return False

    # ex: 1-6 4-5
    # x fully incorporates y so we can just return x and ignore y going forward
    if x[1] >= y[1]:
        return x
    
    # ex : 1-9 6-11
    # we know these two ranges overlap so lets take the outside of each
    return (x[0], y[1])


total = 0
changes = 1
ranges.sort(key=lambda x: x[0])

while changes > 0:
    rangesTmp = []
    changes = 0
    ranges.sort(key=lambda x: x[0])

    for i in range(len(ranges)):
        if i == 0: 
            continue
        t = combineRanges(ranges[i-1], ranges[i])
        if (t):
            print('combine', t,ranges[i-1], ranges[i])
            rangesTmp.append(t) 
            for j in range(i+1, len(ranges)):
                rangesTmp.append(ranges[j])
            changes +=1
            break
        else:
            rangesTmp.append(ranges[i-1])
        if i == len(ranges)-1:
            rangesTmp.append(ranges[i])

    ranges = rangesTmp.copy()

for r in ranges:
    total += r[1] - r[0] + 1
print(ranges)
print(total)



