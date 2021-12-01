input = open("input.txt", "r")

increases = 0
lastDepth = -1
counter = 0
array = []
windowSize = 3

for line in input:


    for i in range(counter, counter - (windowSize), -1):
        if(i >= 0):
            if(len(array) <= i):
                array.append(int(line))
            else:
                array[i] += int(line)
    counter += 1

for i in range(windowSize - 1):
    array.pop()

for depth in array:
    if(lastDepth >= 0):
        if(depth > lastDepth):
            increases += 1      
    
    lastDepth = depth

print(increases)