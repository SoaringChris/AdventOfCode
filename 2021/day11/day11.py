input = open("input.txt", "r")

lines = input.read().splitlines()


grid = [list(x) for x in lines]
grid = [[int(y) for y in x] for x in grid]
sizeX = len(grid)
sizeY = len(grid[0])

toFlash = []

def flash(x, y):
    grid[x][y] = 0

    if x > 0:
        if grid[x - 1][y] > 0:
            grid[x - 1][y] += 1
            if (grid[x - 1][y] > 9) and (not [x - 1, y] in toFlash):
                toFlash.append([x - 1, y])
        
        if y > 0:
            if grid[x - 1][y - 1] > 0:
                grid[x - 1][y - 1] += 1
                if (grid[x - 1][y - 1] > 9) and (not [x - 1, y - 1] in toFlash):
                    toFlash.append([x - 1, y - 1])

        if y < sizeY - 1:
            if grid[x - 1][y + 1] > 0:
                grid[x - 1][y + 1] += 1
                if (grid[x - 1][y + 1] > 9) and (not [x - 1, y + 1] in toFlash):
                    toFlash.append([x - 1, y + 1])

    if x < sizeX - 1:
        if grid[x + 1][y] > 0:
            grid[x + 1][y] += 1
            if (grid[x + 1][y] > 9) and (not [x + 1, y] in toFlash):
                toFlash.append([x + 1, y])
        
        if y > 0:
            if grid[x + 1][y - 1] > 0:
                grid[x + 1][y - 1] += 1
                if (grid[x + 1][y - 1] > 9) and (not [x + 1, y - 1] in toFlash):
                    toFlash.append([x + 1, y - 1])

        if y < sizeY - 1:
            if grid[x + 1][y + 1] > 0:
                grid[x + 1][y + 1] += 1
                if (grid[x + 1][y + 1] > 9) and (not [x + 1, y + 1] in toFlash):
                    toFlash.append([x + 1, y + 1])

    if y > 0:
         if grid[x][y - 1] > 0:
            grid[x][y - 1] += 1
            if (grid[x][y - 1] > 9) and (not [x, y - 1] in toFlash):
                toFlash.append([x, y - 1])

    if y < sizeY - 1:
        if grid[x][y + 1] > 0:
            grid[x][y + 1] += 1
            if (grid[x][y + 1] > 9) and (not [x, y + 1] in toFlash):
                toFlash.append([x, y + 1])

def simulateStep():
    for x in range(sizeX):
        for y in range(sizeY):
            grid[x][y] += 1
            if grid[x][y] > 9:
                toFlash.append([x, y])


    numFlashes = 0
    while len(toFlash) > 0:
        octo = toFlash.pop()
        flash(octo[0], octo[1])
        numFlashes += 1
    
    return numFlashes


totalFlashes = 0
counter = 0
allTogether = False
while allTogether == False or counter < 100:
    counter += 1
    flashes = simulateStep()
    totalFlashes += flashes
    if(counter == 100): #Part 1
        print("At 100: ")
        print(totalFlashes)

    if(flashes == sizeX * sizeY):
        print("Synchronzied at: ")
        print(counter)
        allTogether = True
        
