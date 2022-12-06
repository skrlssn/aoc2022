from os import environ


def getSolutionPart1(input_list):
    count = 4
    pastFour = input_list[:count]
    for _ in input_list[count:]:
        if areAllUnique(pastFour):
            return count
        count += 1
        pastFour = input_list[count-4:count]
    return None

# den här stal jag, ngl
def areAllUnique(list):
    seen = set()
    return not any(i in seen or seen.add(i) for i in list)

def getSolutionPart2(input_list):
    count = 14
    pastFourteen = input_list[:count]
    for _ in input_list[count:]:
        if areAllUnique(pastFourteen):
            return count
        count += 1
        pastFourteen = input_list[count-14:count]
    return None


file_input = open("input.txt", "r").read()

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input)) # 3774
else:
    print(getSolutionPart1(file_input)) # 1623
