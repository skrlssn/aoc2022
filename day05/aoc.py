from os import environ


def getStacks(input):
    stacks = []
    for j in range(1, 35, 4):
        stack = []
        for i in range(7, -1, -1):
            if input[i][j] != ' ':
                stack.append(input[i][j])
        stacks.append(stack)
    return stacks


def getUpdatedStacksOneAtATime(stacks, input):
    for row in input[10:]:
        move, start, end = row.split(' ')[1::2]
        for _ in range(int(move)):
            stacks[int(end)-1].append(stacks[int(start)-1].pop())
    return stacks


def getUpdatedStacksManyAtATime(stacks, input):
    for row in input[10:]:
        move, start, end = row.split(' ')[1::2]    
        to_move = stacks[int(start)-1][-int(move):]
        to_keep = stacks[int(start)-1][:-int(move)]
        stacks[int(start)-1] = to_keep
        stacks[int(end)-1] += to_move
    return stacks


def getSolutionPart1(input_list):
    return ''.join([stack[-1] for stack in getUpdatedStacksOneAtATime(getStacks(input_list), input_list)])


def getSolutionPart2(input_list):
    return ''.join([stack[-1] for stack in getUpdatedStacksManyAtATime(getStacks(input_list), input_list)])


file_input = open("input.txt", "r").read().splitlines()

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input)) # QNDWLMGNS
else:
    print(getSolutionPart1(file_input)) # CNSZFDVLJ
