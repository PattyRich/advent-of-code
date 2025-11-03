


def doDontValidate(string):
    if string[0:4] == "do()":
        return 'do'
    if string[0:7] == "don't()":
        return 'dont'
    return None

def mulValidate(string):
    if not string[0:4] == "mul(":
        return False
    
    cnt = 4
    while True:
        if cnt >= len(string):
            return False
        if string[cnt] == ")":
            break
        cnt += 1

    checkString = string[4:cnt]
    params = checkString.split(",")
    if len(params) != 2:
        return False
    if not params[0].strip().isdigit() or not params[1].strip().isdigit():
        return False

    return int(params[0].strip()) * int(params[1].strip())


total = 0
do = 'do'
with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        for i in range(len(line)):
            action = doDontValidate(line[i:])
            if action is not None:
                do = action
            value = mulValidate(line[i:])
            if value is not False and do == 'do':
                total += value
print(total)
