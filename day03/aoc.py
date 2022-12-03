from os import environ

points = {
    'a': 1, 
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 1 + 26, 
    'B': 2 + 26,
    'C': 3 + 26,
    'D': 4 + 26,
    'E': 5 + 26,
    'F': 6 + 26,
    'G': 7 + 26,
    'H': 8 + 26,
    'I': 9 + 26,
    'J': 10 + 26,
    'K': 11 + 26,
    'L': 12 + 26,
    'M': 13 + 26,
    'N': 14 + 26,
    'O': 15 + 26,
    'P': 16 + 26,
    'Q': 17 + 26,
    'R': 18 + 26,
    'S': 19 + 26,
    'T': 20 + 26,
    'U': 21 + 26,
    'V': 22 + 26,
    'W': 23 + 26,
    'X': 24 + 26,
    'Y': 25 + 26,
    'Z': 26 + 26
}


def getSolutionPart1(input_list):
    total_prio = 0
    for row in input_list:
        bag1, bag2 = row[:(len(row)//2)], row[(len(row)//2):]
        for char in bag1:
            if char in bag2:
                total_prio += points[char]
                break
    return total_prio


def getSolutionPart2(input_list):
    total_prio = 0
    i = 0
    while i < len(input_list):
        for char in input_list[i]:
            if char in input_list[i+1] and char in input_list[i+2]:
                total_prio += points[char]
                break
        i += 3
    return total_prio


file = open("input.txt", "r")
input_list = file.read().splitlines()

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(input_list)) 
else:
    print(getSolutionPart1(input_list))
