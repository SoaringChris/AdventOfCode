class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def getPoints(self, countDiagonals):
        points = [[self.x1, self.y1]]
        if(self.x1 == self.x2):
            y = self.y1
            while(y != self.y2):
                if(self.y2 > y):
                    y +=1
                else:
                    y -=1
                points.append([self.x1, y])

        elif(self.y1 == self.y2):
            x = self.x1
            while(x != self.x2):
                if(self.x2 > x):
                    x +=1
                else:
                    x -= 1
                points.append([x, self.y1])
        elif(countDiagonals):
            x = self.x1
            y = self.y1
            while(x != self.x2 and y != self.y2):
                if(self.y2 > y):
                    y +=1
                else:
                    y -=1
                if(self.x2 > x):
                    x +=1
                else:
                    x -= 1
                points.append([x,y])

        else:
            return None
        return points

def compute(useDiagonals):
    input = open("input.txt" , "r")

    inputLines = input.read().splitlines()

    pointDict = {}

    for inputLine in inputLines:
        brokenLine = inputLine.split()
        point1 = brokenLine[0].split(',')
        point2 = brokenLine[2].split(',')
        line = Line(int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1]))
        linePoints = line.getPoints(useDiagonals)
        if(linePoints == None):
            continue

        for point in linePoints:
            if point[0] in pointDict and point[1] in pointDict[point[0]]:
                pointDict[point[0]][point[1]] += 1
            else:
                if not point[0] in pointDict:
                    pointDict[point[0]] = {}
                pointDict[point[0]][point[1]] = 1

    # print(pointDict)
    overlaps = 0
    for x in pointDict:
        for y in pointDict[x]:
            if(pointDict[x][y] > 1):
                overlaps += 1

    print(overlaps)

compute(False) #Part 1
compute(True)  #Part 2

