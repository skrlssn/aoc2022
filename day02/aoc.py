from os import environ


def getSolutionPart1(input_list):
    total_score = 0
    for move in input_list:
        elf, me = move.split(" ")
        if elf == 'A':
            match me:
                case 'X':
                    total_score += (1 + 3)
                case 'Y':
                    total_score += (2 + 6)
                case 'Z':
                    total_score += (3 + 0)
        elif elf == 'B':
            match me:
                case 'X':
                    total_score += (1 + 0)
                case 'Y':
                    total_score += (2 + 3)
                case 'Z':
                    total_score += (3 + 6)
        elif elf == 'C':
            match me:
                case 'X':
                    total_score += (1 + 6)
                case 'Y':
                    total_score += (2 + 0)
                case 'Z':
                    total_score += (3 + 3)
                    
    return total_score


def getSolutionPart2(input_list):
    total_score = 0
    for move in input_list:
        elf, me = move.split(" ")
        if elf == 'A':
            match me:
                case 'X':
                    total_score += (3 + 0)
                case 'Y':
                    total_score += (1 + 3)
                case 'Z':
                    total_score += (2 + 6)

        elif elf == 'B':
            match me:
                case 'X':
                    total_score += (1 + 0)
                case 'Y':
                    total_score += (2 + 3)
                case 'Z':
                    total_score += (3 + 6)
        elif elf == 'C':
            match me:
                case 'X':
                    total_score += (2 + 0)
                case 'Y':
                    total_score += (3 + 3)
                case 'Z':
                    total_score += (1 + 6)
    return total_score


file = open("input.txt", "r")
input_list = file.read().splitlines()

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(input_list))  # 12535
else:
    print(getSolutionPart1(input_list))  # 15457 
