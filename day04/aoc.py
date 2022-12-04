from os import environ


def getSolutionPart1(input_list):
    total = 0
    for pair in input_list:
        elf1, elf2 = pair.split(',')
        elf1_start, elf1_end = elf1.split('-')
        elf2_start, elf2_end = elf2.split('-')
        if int(elf1_start) <= int(elf2_start) and int(elf1_end) >= int(elf2_end):
            total += 1
        elif int(elf2_start) <= int(elf1_start) and int(elf2_end) >= int(elf1_end):
            total += 1
    return total


def getSolutionPart2(input_list):
    total = 0
    for pair in input_list:
        elf1, elf2 = pair.split(',')
        elf1_start, elf1_end = elf1.split('-')
        elf2_start, elf2_end = elf2.split('-')
        elf1_range = list(range(int(elf1_start), int(elf1_end) + 1))
        elf2_range = list(range(int(elf2_start), int(elf2_end) + 1))
        for value in elf1_range:
            if value in elf2_range:
                total += 1
                break
    return total


file = open("input.txt", "r")
input = file.read().splitlines()

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(input)) #804
else:
    print(getSolutionPart1(input)) #424
