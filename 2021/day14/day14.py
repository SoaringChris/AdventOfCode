def performStep(dict, instances, counters):
    instanceCopy = instances.copy()
    for key in list(instances.keys()):
        count = instances[key]
        targets = dict[key]
        instanceCopy[key] -= count
        instanceCopy[targets[0]] += count
        instanceCopy[targets[1]] += count
        counters[targets[2]] += count
    return instanceCopy

def compute(dict, instances, counters, steps):
    _instances = instances
    for i in range(steps):
        _instances = performStep(dict, _instances, counters)
    
    maxKey = max(counters, key= lambda k: counters[k])
    minKey = min(counters, key= lambda k: counters[k])

    print(counters[maxKey] - counters[minKey])


input = open("input.txt", "r")

lines = input.read().splitlines()

polymer = lines[0]

dict = {}
instances = {}
counters = {}

for line in lines[2:]:
    components = line.split(" -> ")
    dict[components[0]] = [components[0][0] + components[1], components[1] + components[0][1], components[1]]
    instances[components[0]] = 0

uniqueCharacters = list(set(''.join(list(instances.keys()))))
for char in uniqueCharacters:
    counters[char] = polymer.count(char)

for i in range(len(polymer) - 1):
    if polymer[i : i + 2] in list(instances.keys()):
        instances[polymer[i : i + 2]] += 1

compute(dict.copy(), instances.copy(), counters.copy(), 10) #Part 1

compute(dict.copy(), instances.copy(), counters.copy(), 100000) #Part 2