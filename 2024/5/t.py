import math
rules = []
exe = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        row = []
        if '|' in line:
            parts = line.split('|')
            rules.append(parts)
        elif line != "":
            parts = line.split(",")
            exe.append(parts)


total = 0
totalBad = 0
bads = []
for i in range (len(exe)):
    ok = True
    for j in range (len(exe[i])):
        #print(j)
        num = exe[i][j]
        for rule in rules:
            if rule[0] == num:
                #print("Checking 1", rule, "in", exe[i], exe[i][0:j])
                if rule[1] in exe[i][0:j]:
                    #print("Found", rule[1], "before", num)
                    ok = False
                    break
            if rule[1] == num:
                #print("Checking 2", rule, "in", exe[i], exe[i][j:])
                if rule[0] in exe[i][j:]:
                    #print("Found", rule[0], "after", num)
                    ok = False
                    break
    if ok: 
        total += int(exe[i][math.ceil(len(exe[i])/2)-1])
    else:
        bads.append(exe[i])


for i in range (len(bads)):
    for x in range(len(bads[i])):
        for j in range (len(bads[i])):
            num = bads[i][j]
            for rule in rules:
                if rule[0] == num:
                    if rule[1] in bads[i][0:j]:
                        badIndex = bads[i].index(rule[1])
                        bads[i].insert(j+1, rule[1])
                        bads[i].pop(badIndex)
                    
                if rule[1] == num:
                    if rule[0] in bads[i][j:]:
                        badIndex = bads[i].index(rule[0])
                        bads[i].insert(j, rule[0])
                        bads[i].pop(badIndex+1)

    totalBad += int(bads[i][math.ceil(len(bads[i])/2)-1])
    print(bads[i], 'after', int(bads[i][math.ceil(len(bads[i])/2)-1]))


print(total)
print(totalBad)