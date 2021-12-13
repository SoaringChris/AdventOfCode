def performFold(points, fold):

    foldIndex = 0 if fold[0] == 'x' else 1
    for point in points.copy():
        if point[foldIndex] > fold[1]:
            points.remove(point)
            newPoint = point
            newPoint[foldIndex] = fold[1] - (point[foldIndex] -  fold[1])
            if not newPoint in points:
                points.append(newPoint)
    return points

def part2(pts, folds):
    points = pts
    for fold in folds:
        points = performFold(points.copy(), fold)

    maxX = max(point[0] for point in points) + 1
    maxY = max(point[1] for point in points) + 1

    grid = [['.'] * maxX for i in range(maxY)]

    for point in points:
        grid[point[1]][point[0]] = '#'

    for y in range(maxY):
        for x in range(maxX):
            print(grid[y][x], end="")
        print("\n", end="")

input = open("input.txt", "r")

data = input.read().split("\n\n")
gridData = data[0].splitlines()
foldData = data[1].splitlines()

points = []
for line in gridData:
    components = line.split(",")
    points.append([int(components[0]), int(components[1])])

folds = []
for line in foldData:
    components = line.split()
    foldInfo = components[2].split('=')
    folds.append([foldInfo[0], int(foldInfo[1])])

print(len(performFold(points.copy(), folds[0]))) #Part 1
part2(points.copy(), folds)
