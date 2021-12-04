def calcOxygen(data):
    index = 0
    remainingData = data.copy()
    print(remainingData)
    while(len(remainingData) > 1):
        remainingData = filterCommon(True, index, remainingData)
        index += 1
    return remainingData[0]

def calcCo2(data):
    index = 0
    remainingData = data.copy()
    print(remainingData)
    while(len(remainingData) > 1):
        remainingData = filterCommon(False, index, remainingData)
        index += 1
    return remainingData[0]

def digitIsOne(digit, num):
    comparator = 0b1 << (12 - digit - 1)
    return num & comparator != 0

def filterCommon(most, digit, data):
    def checkIsOne(num):
        return digitIsOne(digit, num)
    
    def checkIsZero(num):
        return not checkIsOne(num)

    group1 = list(filter(checkIsOne, data))
    group2 = list(filter(checkIsZero, data))

    if(len(group1) >= len(group2) and most):
        return group1
    elif(len(group1) < len(group2) and not most):
        return group1
    else:
        return group2


input = open("input.txt")

data = []

for line in input.read().splitlines():
    data.append(int(line, 2))

oxygen = calcOxygen(data)
co2 = calcCo2(data)
print("Oxygne: " + str(oxygen))
print("CO2: " + str(co2))

print(oxygen * co2)

print(digitIsOne(1, 15))