result = []
import functools

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        data = line.split(" ")
        result = data

for i in range(len(result)):
    result[i] = int(result[i])

print(result)


# this didn't work

# def process(arr):
#     temp = []
#     for i in range(len(arr)):
#         num = processNum(arr[i])
#         for item in num:
#             temp.append(item)
#     return temp

# @functools.lru_cache(maxsize=None)
# def processNum(num):
#     string = str(num)
#     length = len(string)
#     if num == 0:
#         return [1]
#     elif (length % 2) == 0:
#         length /= 2
#         length = int(length)
#         return [int(string[:length]), int(string[length:])]
#     else:
#         return [num * 2024]

# for i in range(75):
#     print(i)
#     result = process(result)


@functools.lru_cache(maxsize=None)
def countStones(num, depth):
    left, right = recursiveCnt(num)

    if depth == 75:
        if right is None:
            return 1
        else:
            return 2

    else:
        total = countStones(left, depth + 1)
        if right is not None:
            total += countStones(right, depth + 1)
        
    return total 

@functools.lru_cache(maxsize=None)
def recursiveCnt(num):
    string = str(num)
    length = len(string)
    if num == 0:
        return [1, None]
    elif (length % 2) == 0:
        length /= 2
        length = int(length)
        return [int(string[:length]), int(string[length:])]
    else:
        return [num*2024, None]

cnt = 0
total = 0
for i in range(len(result)):
    total += countStones(result[i], 1)
print(total)
print(countStones.cache_info())