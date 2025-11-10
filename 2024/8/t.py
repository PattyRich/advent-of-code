result = []
d = {}
index = -1
maxWidth = -1
with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        maxWidth = len(line)
        index += 1
        for i in range(len(line)):
            if line[i] != '.':
                if not line[i] in d:
                    d[line[i]] = [(index, i)]
                else:
                    d[line[i]].append((index,i))

def checkValidAnti(tuple, maxHeight, maxWidth):
    if tuple[0] < 0 or tuple[0] > maxHeight:
        return False
    if tuple[1] > maxWidth or tuple[1] < 0:
        return False
    return True
    

antis = []
for key in d.keys():
    for i in range(len(d[key])):
        for j in range(i, len(d[key])):
            if i == j:
                continue
            yDist = abs(d[key][i][0] - d[key][j][0])
            xDist = abs(d[key][i][1] - d[key][j][1])
            # assumes x ([0]) in tuple comes in ascending order
            xFactor = d[key][i][1] > d[key][j][1]

            anti1 = None
            anti2 = None
            if xFactor:
                anti1 = (d[key][i][0] - yDist, d[key][i][1] + xDist)
                anti2 = (d[key][j][0] + yDist, d[key][j][1] - xDist)
            else:
                anti1 = (d[key][i][0] - yDist, d[key][i][1] - xDist)
                anti2 = (d[key][j][0] + yDist, d[key][j][1] + xDist)

            # print(anti1, anti2, i ,j, key, d, xFactor)
            if (checkValidAnti(anti1, index, maxWidth-1)):
                if anti1 not in antis:
                    antis.append(anti1)
            if (checkValidAnti(anti2, index, maxWidth-1)):
                if anti2 not in antis:
                    antis.append(anti2)

print(antis)
print(len(antis))

#part 2
antis = []
for key in d.keys():
    for i in range(len(d[key])):
        for j in range(i, len(d[key])):
            if (d[key][j][0], d[key][j][1]) not in antis:
                antis.append((d[key][j][0], d[key][j][1]))
            if i == j:
                continue
            
            yDist = abs(d[key][i][0] - d[key][j][0])
            xDist = abs(d[key][i][1] - d[key][j][1])
            # assumes x ([0]) in tuple comes in ascending order
            xFactor = d[key][i][1] > d[key][j][1]
            
            anti1 = None
            anti2 = None
            if xFactor:
                anti1 = (d[key][i][0] - yDist, d[key][i][1] + xDist)
                anti2 = (d[key][j][0] + yDist, d[key][j][1] - xDist)
            else:
                anti1 = (d[key][i][0] - yDist, d[key][i][1] - xDist)
                anti2 = (d[key][j][0] + yDist, d[key][j][1] + xDist)
            
            while True:
                if (checkValidAnti(anti1, index, maxWidth-1)):
                    if anti1 not in antis:
                        antis.append(anti1)
                else: 
                    break
                if xFactor:
                    anti1 = (anti1[0] - yDist, anti1[1] + xDist)
                else:
                    anti1 = (anti1[0] - yDist, anti1[1] - xDist)

            while True:
                if (checkValidAnti(anti2, index, maxWidth-1)):
                    if anti2 not in antis:
                        antis.append(anti2)
                else: 
                    break
                if xFactor:
                    anti2 = (anti2[0] + yDist, anti2[1] - xDist)
                else:
                    anti2 = (anti2[0] + yDist, anti2[1] + xDist)


print(antis)
print(len(antis))
