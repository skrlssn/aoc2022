from os import environ


def isVisible(height, x, y, forrest):
    left = [tree for tree in forrest[x][:y]]
    right = [tree for tree in forrest[x][y+1:]]
    up = [row[y] for row in forrest[:x]]
    down = [row[y] for row in forrest[x+1:]]

    if not left or not right or not up or not down:
        return True

    if max(left) < height:
        return True
    elif max(right) < height:
        return True
    elif max(up) < height:
        return True
    elif max(down) < height:
        return True
    else:
        return False


def getScenicScore(height, x, y, forrest):
    left = [tree for tree in forrest[x][:y]]
    right = [tree for tree in forrest[x][y+1:]]
    up = [row[y] for row in forrest[:x]]
    down = [row[y] for row in forrest[x+1:]]

    if not left or not right or not up or not down:
        return 0

    left_score, right_score, up_score, down_score = 0, 0, 0, 0
    
    for tree in reversed(left):            
        if tree < height:
            left_score += 1
        else:
            left_score += 1
            break
    for tree in right:
        if tree < height:
            right_score += 1
        else:
            right_score += 1
            break
    for tree in reversed(up):
        if tree < height:
            up_score += 1
        else:
            up_score += 1
            break
    for tree in down:
        if tree < height:
            down_score += 1
        else:
            down_score += 1
            break

    return left_score * right_score * up_score * down_score


def getSolutionPart1(input_list):
    visibleTrees = 0
    for xPos, row in enumerate(input_list) :
        for yPos, tree in enumerate(row):
            if isVisible(tree, xPos, yPos, input_list):
                visibleTrees += 1
    return visibleTrees


def getSolutionPart2(input_list):
    scores = []
    for xPos, row in enumerate(input_list) :
        for yPos, tree in enumerate(row):
            scores.append(getScenicScore(tree, xPos, yPos, input_list))
    return max(scores)


file_input = [list(map(int, row)) for row in open("input.txt", "r").read().splitlines()]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input)) # 291840
else:
    print(getSolutionPart1(file_input)) # 1829
