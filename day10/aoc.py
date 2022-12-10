from os import environ


def getSolutionPart1(input_list):
    x = 1
    cpuValues = []
    cyclesOfInterest = list(range(20, 240, 40))

    for input in input_list:
        cpuValues.append(x)
        instruction = input.split()
        if instruction[0] == 'addx':
            cpuValues.append(x)
            x += int(instruction[1])
    
    return sum([cpuValues[x-1] * x for x in cyclesOfInterest])


def getSolutionPart2(input_list):
    def drawPixel():
        if currentPixel in sprite:
            pixels.append('# ')
        else:
            pixels.append('  ')

    def moveSprite():
        return [x-1, x, x+1]
    
    def getNextPixel(pixel):
        if pixel < 39: 
            return pixel + 1
        else:
            return 0
    
    def printCRT(pixels):
        count = 0
        for i in pixels:
            print(i, end='')
            if count == 39:
                print('\n')
                count = 0
            else:
                count += 1
    x = 1
    pixels = []
    sprite = [0, 1, 2]
    currentPixel = 0

    for input in input_list:
        match input.split(): # start process
            case [_, value]:
                #first run, execution begins
                drawPixel()
                currentPixel = getNextPixel(currentPixel)
                #second run
                drawPixel()
                #execution finishes
                x += int(value)
                sprite = moveSprite()
            case ['noop']:
                drawPixel()
        currentPixel = getNextPixel(currentPixel)
    printCRT(pixels)


def main():
    file_input = open("input.txt", "r").read().splitlines()

    print('Python')
    part = environ.get('part')

    if part == 'part2':
        getSolutionPart2(file_input)
    else:
        print(getSolutionPart1(file_input))

if __name__ == '__main__':
    main()
