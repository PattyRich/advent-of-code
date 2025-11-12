result = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        t = []
        for char in line:
            t.append(int(char))
        result.append(t)


print(result)

def explore(board, x, y, target):
    if x <0 or x>len(board[0]) -1:
        return False
    if y <0 or y>len(board) -1:
        return False
    if board[y][x] == target:
        return True
    return False

trails = []
for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] == 0:
            trails.append({'start': (i,j), 'curr': (i,j)})

curr = 1
for i in range(9):
    print(trails)
    tmpTrails = []
    for trail in trails:
        if explore(result, trail['curr'][1] + 1, trail['curr'][0], curr):
            tmpTrails.append({'start': trail['start'], 'curr': (trail['curr'][0], trail['curr'][1] + 1)})
        if explore(result, trail['curr'][1] - 1, trail['curr'][0], curr):
            tmpTrails.append({'start': trail['start'], 'curr': (trail['curr'][0], trail['curr'][1] - 1)})
        if explore(result, trail['curr'][1], trail['curr'][0] + 1, curr):
            tmpTrails.append({'start': trail['start'], 'curr': (trail['curr'][0] + 1, trail['curr'][1])})
        if explore(result, trail['curr'][1], trail['curr'][0] - 1, curr):
            tmpTrails.append({'start': trail['start'], 'curr': (trail['curr'][0] - 1, trail['curr'][1])})
    trails = tmpTrails
    curr +=1

print(len(trails))

cnt = []
for trail in trails:
    tuples = ((trail['start']),(trail['curr']))
    if tuples not in cnt:
        cnt.append(tuples)

print(len(cnt))