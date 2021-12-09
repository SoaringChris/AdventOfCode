oneCount = 2
fourCount = 4
sevenCount = 3
eightCount = 7
unique = [None, oneCount, None, None, fourCount, None, None, sevenCount, eightCount, None]


def part1(output):
    numUnique = 0

    for line in output:
        displays = line.split()
        for display in displays:
            if len(display) in unique:
                numUnique += 1
    print(numUnique)

def part2(data, output):

    sum = 0

    for line in data:

        displays = line.split()
        key = [None] * 10
        segments = {
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None
        }

        for display in displays:
            if len(display) in unique:
                key[unique.index(len(display))] = display
        displays = [x for x in displays if x not in key]
        
        segments['a'] = [x for x in key[7] if x not in key[1]][0]
        nineEliminator = key[4] + segments['a']
        
        for display in displays:
            if len(display) != 6:
                continue
            eliminated = [x for x in display if x not in nineEliminator]
            if len(eliminated) == 1 and len([x for x in key[1] if x not in display]) == 0:
                key[9] = display
                displays.remove(display)
                segments['g'] = eliminated[0]
                break
        
        threeEliminator = key[7] + segments['g']

        for display in displays:
            eliminated = [x for x in display if x not in threeEliminator]
            if len(eliminated) == 1:
                key[3] = display
                displays.remove(display)
                segments['d'] = eliminated[0]
                break
        
        segments['b'] = [x for x in key[9] if x not in key[3]][0] # 0, 1, 3, 4, 6, 7, 8, 9 | a, b, c, d, e, f, g
        segments['e'] = [x for x in key[8] if x not in key[9]][0]
        
        for display in displays:
            remainer = [x for x in key[8] if x not in display][0]
            if remainer == segments['d']:
                key[0] = display
                displays.remove(display)
                break

        key[6] = [x for x in displays if len(x) == 6][0]
        displays.remove(key[6])

        segments['c'] = [x for x in key[7] if x not in key[6]][0]
        segments['f'] = key[1].replace(segments['c'], "")

        for display in displays:
            if display.find(segments['b']) != -1:
                key[5] = display
                displays.remove(display)
        
        key[2] = displays[0]

        result = ""

        for display in output[data.index(line)].split():
            for k in key:
                if len(k) == len(display) and len([x for x in k if x not in display]) == 0:
                    result += str(key.index(k))

        sum += int(result)
    
    print(sum)


        


input = open("input.txt", "r")

lines = input.read().splitlines()

data = []
output = []

for line in lines:
    splitLine = line.split(" | ")
    data.append(splitLine[0])
    output.append(splitLine[1])

#part1(output.copy())
part2(data.copy(), output.copy())




