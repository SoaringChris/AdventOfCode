def part2(lines):
    coordinates = [0,0]
    aim = 0

    for line in lines:
        args = line.split()

        match args[0]:
            case "forward":
                coordinates[0] += int(args[1])
                coordinates[1] += (int(args[1]) * aim)
            case "up":
                aim -= int(args[1])
            case "down":
                aim += int(args[1])

    print(coordinates)
    print(coordinates[0] * coordinates[1])


input = open("input.txt", "r")
part2(input.readlines())