def simulateDay(days):
    new5 = 0
    new7 = 0
    for i in range(len(days)):
        temp = days[i]
        if(i == 0):
            new5 += days[i]
            new7 += days[i]
        if(i + 1 != len(days)):
            days[i] = days[i + 1]
        else:
            days[i] = 0
        
    days[6] += new5
    days[8] += new7
    return days

input = open("input.txt", "r")

fish = input.read().split(',')
fish = [int(i) for i in fish]

days = [0] * 9

for f in fish:
    days[f] += 1

for i in range(256):
    days = simulateDay(days)
    print(str(i + 1) + ": " + str(days))
print(sum(days))