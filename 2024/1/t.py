
row1 = []
row2 = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        line = line.strip()
        line = line.split(" ")
        row1Done = False
        for lineData in line:
            if lineData != "":
                if not row1Done:
                    row1.append(lineData)
                    row1Done = True
                else:
                    row2.append(lineData)


row1.sort()
row2.sort()

total = 0

for i in range(len(row1)):
    total += abs(int(row1[i]) - int(row2[i]))

print(total)
    

total2 = 0
occurances = {}
for i in range(len(row1)):
    if row1[i] in occurances:
       total2 += occurances[row1[i]]
    else:
        occurances[row1[i]] = row2.count(row1[i])
        total2 += occurances[row1[i]] * int(row1[i])

print(occurances)
print(total2)
