from os import environ


def isVisible(height, x, y, forrest):
    left = [tree for tree in forrest[x][:y]]
    right = [tree for tree in forrest[x][y+1:]]
    up = [row[y] for row in forrest[:x]]
    down = [row[y] for row in forrest[x+1:]]

    if not left or not right or not up or not down:
        return True

    if max(left) < int(height):
        return True
    elif max(right) < int(height):
        return True
    elif max(up) < int(height):
        return True
    elif max(down) < int(height):
        return True
    else:
        return False


def getScenicScore(height, x, y, forrest):
    left = list(map(int, [tree for tree in forrest[x][:y]]))
    right = list(map(int, [tree for tree in forrest[x][y+1:]]))
    up = list(map(int, [row[y] for row in forrest[:x]]))
    down = list(map(int, [row[y] for row in forrest[x+1:]]))

    if not left or not right or not up or not down:
        return 0

    left_score, right_score, up_score, down_score = 0, 0, 0, 0
    
    for tree in reversed(left):            
        if tree < int(height):
            left_score += 1
        else:
            left_score += 1
            break
    for tree in right:
        if tree < int(height):
            right_score += 1
        else:
            right_score += 1
            break
    for tree in reversed(up):
        if tree < int(height):
            up_score += 1
        else:
            up_score += 1
            break
    for tree in down:
        if tree < int(height):
            down_score += 1
        else:
            down_score += 1
            break

    return left_score * right_score * up_score * down_score


def getSolutionPart1(input_list):
    total = 0
    for xPos, row in enumerate(input_list) :
        for yPos, tree in enumerate(row):
            if isVisible(tree, xPos, yPos, input_list):
                total += 1
    return total


def getSolutionPart2(input_list):
    best_score = 0
    for xPos, row in enumerate(input_list) :
        for yPos, tree in enumerate(row):
            score = getScenicScore(tree, xPos, yPos, input_list)
            if score > best_score:
                best_score = score 
    return best_score


file_input = [list(map(int, row)) for row in open("input.txt", "r").read().splitlines()]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input)) # 291840
else:
    print(getSolutionPart1(file_input)) # 1829
