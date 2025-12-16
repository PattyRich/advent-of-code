
arr = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        arr.append(line)

print(arr)


total = 0
for bat in arr:
    maxOne = -1
    maxTwo = -1
    for i in range(len(bat)):
        num = int(bat[i])
        if num > maxOne and i < len(bat) -1:
            maxOne = num
            maxTwo = -1
            continue
        if num > maxTwo:
            maxTwo = num
    total += int(str(maxOne) + str(maxTwo))

print(total)


total = 0
for bat in arr:
    tracker = [-1 for _ in range(12)]
    for i in range(len(bat)):
        num = int(bat[i])
        for j in range(len(tracker)):
            if num > tracker[j] and i < len(bat) - (11-j):
                tracker[j] = num 
                for x in range(j+1, len(tracker), 1):
                    tracker[x] = -1
                break
    for i in range(len(tracker)):
        tracker[i] = str(tracker[i])
    print(tracker)
    squish = "".join(tracker)
    total += int(squish)

print(total)