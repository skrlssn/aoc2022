from os import environ


def moveBody(moves, body):
        visitedByTail = {(0,0)}
        for move in moves:
            d, steps = move.split()
            for _ in range(int(steps)):
                match d: # first move the head
                    case 'R':
                        body[0][0] += 1
                    case 'L':
                        body[0][0] -= 1
                    case 'U':
                        body[0][1] += 1
                    case 'D':
                        body[0][1] -= 1
                for i in range(1, len(body)): # for each body part, follow the one infront
                    if body[i] == body[i-1]: # on same location do nothing
                        continue
                    if body[i][0] == body[i-1][0]: # on same x axis
                        distance = body[i][1] - body[i-1][1]
                        if distance < -1:
                            body[i][1] += 1
                        elif distance > 1:
                            body[i][1] -= 1
                    elif body[i][1] == body[i-1][1]: # on same y axis
                        distance = body[i][0] - body[i-1][0]
                        if distance < -1:
                            body[i][0] += 1
                        elif distance > 1:
                            body[i][0] -= 1
                    else:
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
        return visitedByTail

def getSolutionPart1(input_list):
    body = [[0,0],[0,0]]
    visitedByTail = moveBody(input_list, body)
    return len(visitedByTail)


def getSolutionPart2(input_list):
    body = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]    
    visitedByTail = moveBody(input_list, body)
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
