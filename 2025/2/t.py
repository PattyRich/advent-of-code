
arr = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    arr = data.split(",")

print(arr)

def findRepeats(start, end):
    start = int(start)
    end = int(end)
    count = 0
    tracker = start
    while tracker <= end:
        length = len(str(tracker))
        if length %2 != 0:
            tracker +=1
            continue
        strTracker = str(tracker)
        lengthHalf = int(length /2)
        if strTracker[:lengthHalf] == strTracker[lengthHalf:]:
            count += tracker
        tracker +=1
    return count

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def check(curr):
    trackerStr = str(curr)
    length = len(trackerStr)
    currLength = length - 1
    while currLength > 0:
        if length % currLength != 0:
            currLength -=1
            continue
        chunk = list(chunks(trackerStr, currLength))
        if len(set(chunk)) == 1:
            return curr
        currLength -=1
    return 0

def findRepeatsPt2(start, end):
    start = int(start)
    end = int(end)
    count = 0
    tracker = start
    while tracker <= end:
        count += check(tracker)
        tracker +=1
    return count


total = 0
total2 = 0
for pair in arr:
    pair = pair.split("-")
    total += findRepeats(pair[0], pair[1])
    total2 += findRepeatsPt2(pair[0], pair[1])

print(total)
print(total2)

