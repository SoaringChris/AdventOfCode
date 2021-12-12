class Cave:
    def __init__(self, name):
        self.name = name
        self.paths = []

    def isSmall(self):
        return self.name.lower() == self.name


input = open("input.txt", "r")

lines = input.read().splitlines()

caves = []
paths = []

def search(node, path, part2 = False, alreadyDupeAdded = False):
    dupeAdded = alreadyDupeAdded
    newPath = path.copy()
    newPath.append(node.name)
    if(node.name == "end"):
        if(not newPath in paths):
            paths.append(newPath)
        return

    smallsVisisted = [x for x in newPath if x.lower() == x]

    for next in node.paths:
        if next.name == "start" or (next.name in smallsVisisted and (not part2 or alreadyDupeAdded)):
            continue
        if next.name in smallsVisisted and part2 and not alreadyDupeAdded:
            dupeAdded = True
        search(next, newPath, part2, dupeAdded)




for line in lines:
    components = line.split("-")

    node1 = next((x for x in caves if x.name == components[0]), Cave(components[0]))
    if not node1 in caves:
        caves.append(node1)

    node2 = next((x for x in caves if x.name == components[1]), Cave(components[1]))
    if not node2 in caves:
        caves.append(node2)

    node1.paths.append(node2)
    node2.paths.append(node1)

start = next((x for x in caves if x.name == "start"), None)

search(start, [], False) #part1
print(len(paths))

paths = []
search(start, [], True)
print(len(paths))