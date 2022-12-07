from os import environ


def getDirSizes(input_list):
    dir_sizes = []
    dir_stack = []

    def leaveDir():
        # first add the dir size to list of dir sizes
        dir_being_left_size = dir_stack.pop(-1)
        dir_sizes.append(dir_being_left_size)

        # if dir exists above it, add the size to that dir too since it contains the dir we are leaving
        if len(dir_stack) > 0:
            dir_stack[-1] += dir_being_left_size

    for input in input_list:
        args = input.split(' ')
        match args:
            case ['$', 'cd', '..']:
                leaveDir()
            case ['$', 'cd', dir_name]:
                # add new dir to stack
                dir_stack.append(0)
            case ['$', 'ls']:
                pass
            case ['dir', dir_name]:
                pass
            # add file size to current dir being explored
            case [file_size, file_name]:
                dir_stack[-1] += int(file_size)

    # there can be dirs left in stack we need to exit         
    while len(dir_stack) > 0:
        leaveDir()

    return dir_sizes
    

def getSolutionPart1(input_list):
    dir_sizes = getDirSizes(input_list)
    return sum([ds for ds in dir_sizes if ds <= 100000])

    
def getSolutionPart2(input_list):
    dir_sizes = getDirSizes(input_list)
    # largest dir most be root dir
    root_size = max(dir_sizes)
    storage_left = 70000000 - root_size
    storage_needed = 30000000 - storage_left
    return min([ds for ds in dir_sizes if ds >= storage_needed])


file_input = open("input.txt", "r").read().splitlines()

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input)) # 2832508
else:
    print(getSolutionPart1(file_input)) # 1182909
