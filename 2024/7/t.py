result = []
nums = []
with open("input.txt", "r") as file:
    data = file.read().strip()
    for line in data.split("\n"):
        line = line.split(':')
        result.append(line[0])
        numss = line[1].strip()
        numss = numss.split(" ")
        nums.append(numss)

def tryAllOperators(result, nums):
    if (len(nums)) == 1 and result != nums:
        return False
    if (len(nums)) == 1 and result == nums:
        return True
    
    maxDigit = 2**(len(nums) -1)
    for i in range(maxDigit):
        binary = bin(i)[2:]
        while len(binary) < len(nums) -1:
            binary = '0' + binary
        
        total = int(nums[0])
        for j in range(len(binary)):
            if binary[j] == '0':
                total += int(nums[j+1])
            elif binary[j] == '1':
                total *= int(nums[j+1])
    
        if total == int(result):
            return True
    
    return False


def tryAllOperators2(result, nums):
    totals = [nums[0], nums[0], nums[0]]
    for x in range(1,len(nums)):
        totalsTemp = []
        for i in range(len(totals)):
            totalsTemp.append(int(totals[i]) * int(nums[x]))
            totalsTemp.append(int(totals[i]) + int(nums[x]))
            totalsTemp.append(str(totals[i]) + nums[x])
        totals = totalsTemp
    if int(result) in totals or result in totals:
        return True
    return False


    

total = 0
total2 = 0

for i in range(len(result)):
    if tryAllOperators(result[i], nums[i]):
        total += int(result[i])
    if tryAllOperators2(result[i], nums[i]):
        total2 += int(result[i])






print(total)
print(total2)
