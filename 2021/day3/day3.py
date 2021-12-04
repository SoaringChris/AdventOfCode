def listToInt(data):
    num = 0
    for bit in data:
        num = (num << 1) | bit
    return num


def part1(data):
    mostCommon = [0 for i in range(len(data[0]))]
    for row in data:
        for i in range(len(row)):
            val = int(row[i])
            if(val > 0):
                mostCommon[i] += 1
            else:
                mostCommon[i] -= 1
    
    for i in range(len(mostCommon)):
        if(mostCommon[i] > 0):
            mostCommon[i] = 1
        else:
            mostCommon[i] = 0

    gamma = listToInt(mostCommon)

    for i in range(len(mostCommon)):
        if(mostCommon[i] > 0):
            mostCommon[i] = 0
        else:
            mostCommon[i] = 1

    epsilon = listToInt(mostCommon)

    print(gamma)

    print(epsilon)
    print(epsilon * gamma)

input = open("input.txt", "r")
part1(input.read().splitlines())