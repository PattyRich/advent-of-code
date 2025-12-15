arr = []

with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        arr.append(line)


spot = 50
password = 0

for move in arr:
    direction = move[0]
    amount = int(move[1:]) % 100
    if direction == 'L':
        spot -= amount
        if spot < 0:
            spot = 100 + spot
    if direction == 'R':
        spot += amount
        spot = spot % 100
    if spot == 0:
        password +=1
print(password, 'answer 1')

spot = 50
password = 0

position: int = 50
zero_count: int = 0

for move in arr:
    direction = move[0]
    amount = int(move[1:])
    if direction == 'L':
        check = False
        if spot == 0:
            check = True
        spot -= amount
        if spot == 0:
            password +=1
        while spot < 0:
            spot += 100
            password +=1
            if check:
                password -=1
                check = False
            if spot == 0:
                password +=1
    if direction == 'R':
        spot += amount
        while spot >= 100:
            spot -= 100
            password +=1
    print(spot, password, direction, amount)
print(password)