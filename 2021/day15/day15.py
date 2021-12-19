import math

class Node:
    def __init__(self, x, y, risk, priority = 0):
        self.x = x
        self.y = y
        self.risk = risk
        self.value = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if(len(self.queue) < 1):
            return None
        min = 0
        for i in range(len(self.queue)):
            if self.queue[i].value < self.queue[min].value:
                min = i
            value = self.queue[min]
            del self.queue[min]
            return value

    def __len__(self):
        return len(self.queue)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def expandGrid(grid):
    maxY = len(grid)
    maxX = len(grid[0])
    expandedY = maxY * 5
    expandedX = maxX * 5

    for i in range(maxY):
        for j in range(maxX, expandedX):
            newVal = grid[i][j - maxX] + 1
            if(newVal == 10):
                newVal = 1
            grid[i].append(newVal)

    for i in range(maxY, expandedY):
        grid.append([])
        for j in range(expandedX):
            newVal = grid[i - maxY][j] + 1
            if(newVal == 10):
                newVal = 1
            grid[i].append(newVal)

input = open("input.txt", "r")
lines = input.read().splitlines()

grid = []

for i in range(len(lines)):
    line = lines[i]
    grid.append([])
    for j in range(len(line)):
        grid[i].append(int(line[j]))

def compute(grid):

    maxY = len(grid) - 1
    maxX = len(grid[0]) - 1

    came_from = {}
    cost_so_far = {}
    came_from[(0, 0)] = None
    cost_so_far[(0, 0)] = 0

    queue = PriorityQueue()
    queue.push(Node(0, 0, 0))

    goal = (maxX, maxY)

    def expandNode(x, y):
        neighbors = []
        if x > 0:
            neighbors.append([x - 1, y])

            # if y > 0:
            #     neighbors.append([x - 1, y - 1])
            # if y < maxY:
            #     neighbors.append([x - 1, y + 1])
        
        if x < maxX:
            neighbors.append([x + 1, y])
            
            # if y > 0:
            #     neighbors.append([x + 1, y - 1])
            # if y < maxY:
            #     neighbors.append([x + 1, y + 1])
        
        if y > 0:
            neighbors.append([x, y - 1])
        if y < maxY:
            neighbors.append([x, y + 1])

        for i in range(len(neighbors)):
            val = neighbors[i]
            neighbors[i] = Node(val[0], val[1], grid[val[1]][val[0]])

        return neighbors


    while len(queue) > 0:
        position = queue.pop()
        if([position.x, position.y] == goal):
            break

        for new in expandNode(position.x, position.y):
            cost = cost_so_far[(position.x, position.y)] + new.risk
            if not (new.x, new.y) in cost_so_far or cost < cost_so_far[(new.x, new.y)]:
                cost_so_far[(new.x, new.y)] = cost
                priority = cost + heuristic(goal, (new.x, new.y))
                new.value = priority
                queue.push(new)
                came_from[(new.x, new.y)] = (position.x, position.y)

    print(cost_so_far[goal])

compute(grid)
expandGrid(grid)
compute(grid)