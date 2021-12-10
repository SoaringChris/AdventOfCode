import math


def part1(grid):
    sum = 0
    lowPoints = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            smallest = True
            if x > 0 and grid[x - 1][y] <= grid[x][y]:
                smallest = False
            if x < len(grid) - 1 and grid[x + 1][y] <= grid[x][y]:
                smallest = False
            if y > 0 and grid[x][y - 1] <= grid[x][y]:
                smallest = False
            if y < len(grid[x]) - 1 and grid[x][y + 1] <= grid[x][y]:
                smallest = False
            
            if smallest:
                lowPoints.append([x, y])
                sum += grid[x][y] + 1

    print(sum)
    return lowPoints


def part2(grid, lowPoints):
    sizeX = len(grid)
    sizeY = len(grid[0])

    open = []
    closed = []
    sizes = []

    def expand(x, y):
        if x > 0:
            if (not [x - 1, y] in open) and (not [x - 1, y] in closed):
                open.append([x - 1, y])

        if x < sizeX - 1:
            if (not [x + 1, y] in open) and (not [x + 1, y] in closed):
                open.append([x + 1, y])
        
        if y > 0:
            if(not [x, y - 1] in open) and (not [x, y - 1] in closed):
                open.append([x, y - 1])
        if y < sizeY - 1:
            if(not [x, y + 1] in open) and (not [x, y + 1] in closed):
                open.append([x, y + 1])

    for start in lowPoints:
        open = []
        closed = []
        basin = []

        open.append(start)

        while len(open) > 0:
            newNode = open[0]
            del open[0]
            closed.append(newNode)
            if(grid[newNode[0]][newNode[1]]) < 9:
                basin.append(newNode)
                expand(newNode[0], newNode[1])
        
        sizes.append(len(basin))
    
    sizes.sort(reverse= True)
    top3 = sizes[:3]
    print(math.prod(top3))




input = open("input.txt", "r")

lines = input.read().splitlines()


grid = [list(x) for x in lines]
grid = [[int(y) for y in x] for x in grid]

lowPoints = part1(grid.copy())

part2(grid.copy(), lowPoints)