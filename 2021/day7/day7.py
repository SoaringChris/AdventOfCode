input = open("input.txt", "r")


def compute(crabs, part2):
    minPos = min(crabs)
    maxPos = max(crabs)

    fuel = []

    for i in range(minPos, maxPos):
        cost = 0
        for crab in crabs:
            dist = abs(crab - i)
            if(part2):
                cost += ((dist * (dist + 1)) / 2)
            else:
                cost += dist
        fuel.append(cost)

    print(min(fuel))

crabs = input.read().split(',')
crabs = [int(i) for i in crabs]


compute(crabs.copy(), False)
compute(crabs.copy(), True)