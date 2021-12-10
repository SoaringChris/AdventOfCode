corruptionValues = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autoCompleteValues = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

mirrors = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

def part1(lines):
    score = 0
    corruptedLines = []
    for line in lines:
        readChars = []
        for char in line:
            if not char in corruptionValues.keys():
                readChars.append(char)
            elif mirrors[char] == readChars[len(readChars) - 1]:
                readChars.pop()
            else:
                if not line in corruptedLines:
                    corruptedLines.append(line)
                score += corruptionValues[char]
                break
    print(score)
    return corruptedLines

def part2(lines):
    scores = []
    for line in lines:
        additions = []
        readChars = []
        for char in line:
            if not char in autoCompleteValues.keys():
                readChars.append(char)
            elif mirrors[char] == readChars[len(readChars) - 1]:
                readChars.pop()

        if(len(readChars) == 0):
            continue

        while len(readChars) > 0:
            char = readChars[len(readChars) - 1]
            index = list(mirrors.values()).index(char)
            mirror = list(mirrors.keys())[index]
            additions.append(mirror)
            readChars.pop()

        score = 0
        for i in range(len(additions)):
            score = score * 5
            score += autoCompleteValues[additions[i]]
        scores.append(score)

    middle = int(len(scores) / 2)
    scores.sort()
    print(scores[middle])


input = open("input.txt", "r")

lines = input.read().splitlines()

corrupted = part1(lines.copy())
part2([x for x in lines if x not in corrupted])