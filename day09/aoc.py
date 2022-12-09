from os import environ


def getSolutionPart1(input_list):
    headLocation = [0,0]
    tailLocation = [0,0]
    visitedByTail = {(0,0)}

    def moveHead(d, steps):
        for _ in range(steps):
            match d:
                case 'R':
                    headLocation[0] += 1
                case 'L':
                    headLocation[0] -= 1
                case 'U':
                    headLocation[1] += 1
                case 'D':
                    headLocation[1] -= 1
            if tailLocation == headLocation: # on same location do nothing
                continue
            if abs(tailLocation[0] - headLocation[0]) == abs(tailLocation[1] - headLocation[1]): # head is diagonally from tail
                continue
            if tailLocation[0] == headLocation[0]: # on same x axis
                distance = tailLocation[1] - headLocation[1]
                if distance < -1: # head to the left by two
                    tailLocation[1] += 1
                elif distance > 1: # head to the right by two
                    tailLocation[1] -= 1
            elif tailLocation[1] == headLocation[1]: # on same y axis
                distance = tailLocation[0] - headLocation[0]
                if distance < -1: # head to the up by two
                    tailLocation[0] += 1
                elif distance > 1: # head to the down by two
                    tailLocation[0] -= 1
            else: # head not adjacent to tail
                if headLocation[1] > tailLocation[1]:
                    tailLocation[1] += 1
                else:
                    tailLocation[1] -= 1
                if headLocation[0] > tailLocation[0]:
                    tailLocation[0] += 1
                else:
                    tailLocation[0] -= 1
            if (tailLocation[0],tailLocation[1]) not in visitedByTail:
                visitedByTail.add((tailLocation[0],tailLocation[1]))      

    for row in input_list:
        d, steps = row.split()
        moveHead(d, int(steps))

    return len(visitedByTail)


def getSolutionPart2(input_list):
    body = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    visitedByTail = {(0,0)}

    def moveHead(d, steps):
        for _ in range(steps):
            match d:
                case 'R':
                    body[0][0] += 1
                case 'L':
                    body[0][0] -= 1
                case 'U':
                    body[0][1] += 1
                case 'D':
                    body[0][1] -= 1
            for i in range(1,10): # for each body part, follow the one infront
                if body[i] == body[i-1]: # on same location do nothing
                    continue
                if body[i][0] == body[i-1][0]: # on same x axis
                    distance = body[i][1] - body[i-1][1]
                    if distance < -1: # head to the left by two
                        body[i][1] += 1
                    elif distance > 1: # head to the right by two
                        body[i][1] -= 1
                elif body[i][1] == body[i-1][1]: # on same y axis
                    distance = body[i][0] - body[i-1][0]
                    if distance < -1: # head to the up by two
                        body[i][0] += 1
                    elif distance > 1: # head to the down by two
                        body[i][0] -= 1
                else: # head not adjacent to tail
                    if abs(body[i][0] - body[i-1][0]) == abs(body[i][1] - body[i-1][1]): # head is diagonally from tail
                        if abs(body[i][0] - body[i-1][0]) < 2: # diagonally adjacent, do not move
                            continue
                    if body[i-1][1] > body[i][1]:
                        body[i][1] += 1
                    else:
                        body[i][1] -= 1
                    if body[i-1][0] > body[i][0]:
                        body[i][0] += 1
                    else:
                        body[i][0] -= 1

            if (body[-1][0], body[-1][1]) not in visitedByTail:
                visitedByTail.add((body[-1][0],body[-1][1]))   


    for row in input_list:
        d, steps = row.split()
        moveHead(d, int(steps))

    return len(visitedByTail)


def main():
    file_input = open("input.txt", "r").read().splitlines()

    print('Python')
    part = environ.get('part')

    if part == 'part2':
        print(getSolutionPart2(file_input))
    else:
        print(getSolutionPart1(file_input))


if __name__ == '__main__':
    main()
