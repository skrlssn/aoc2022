from os import environ


def getSortedElfs():
    calories = input.splitlines()
    elfs = []
    currentElf = 0
    for c in calories:
        if c == '':
            elfs.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(c)
    elfs.sort(reverse=True)
    return elfs


def getSolutionPart1(input):
    elfs = getSortedElfs()
    return elfs[0]


def getSolutionPart2(input):
    elfs = getSortedElfs()
    top_three = int(elfs[0]) + int(elfs[1]) + int(elfs[2])
    return top_three


file = open("input.txt", "r")
input = file.read()

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(input))  # 200945
else:
    print(getSolutionPart1(input))  # 69693
