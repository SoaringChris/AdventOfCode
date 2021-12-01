input = open("input.txt", "r")

increases = 0
lastDepth = -1

for line in input:
    depth = int(line)
    if(lastDepth >= 0):
        if(depth > lastDepth):
            increases += 1
        
    

    lastDepth = depth

print(increases)