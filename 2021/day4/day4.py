class tile:
    def __init__(self, value):
        self.value = value
        self.drawn = False

def generateBoards(input):
    boards = []
    board = []
    for i in range(2, len(input)):
        line = input[i]
        if(len(line) == 0):
            boards.append(board)
            board = []
            continue
        numbers = line.split()
        row = []
        for number in numbers:
            row.append(tile(int(number)))
        board.append(row)
    boards.append(board)
    return boards

def simulateTurn(number, boards):
    for board in boards:
        for row in board:
            for tile in row:
                if(tile.value == int(number)):
                    tile.drawn = True
    return boards

def checkWins(boards):
    for board in boards:
        colCheck = [0] * 5
        for row in board:
            currentCol = 0
            rowCheck = 0
            for tile in row:
                if(tile.drawn):
                    rowCheck += 1
                    colCheck[currentCol] += 1
                if(rowCheck > 4 or colCheck[currentCol] > 4):
                    return board
                currentCol += 1

    return None

def scoreBoard(board):
    sum = 0
    for row in board:
        for tile in row:
            if(not tile.drawn):
                sum += tile.value
    return sum

def part1(draws, boards):
    winner = None
    latestDraw = None
    while(winner == None):
        latestDraw = draws.pop()
        boards = simulateTurn(latestDraw, boards)
        winner = checkWins(boards)
    print(scoreBoard(winner) * int(latestDraw))

def part2(draws, boards):
    winner = None
    latestDraw = None
    while(len(boards) > 0):
        latestDraw = draws.pop()
        boards = simulateTurn(latestDraw, boards)
        winner = checkWins(boards)
        while(winner != None and len(boards) > 0):
            boards.remove(winner)
            if(len(boards) > 0):
                winner = checkWins(boards)

    print(scoreBoard(winner) * int(latestDraw))


input = open("input.txt", "r")

lines = input.read().splitlines()
draws = lines[0].split(',')
draws = list(reversed(draws))
boards = generateBoards(lines)

part1(draws.copy(), boards.copy())
part2(draws.copy(), boards.copy())

