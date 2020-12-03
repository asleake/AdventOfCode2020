""" Slope functions """


def findTreesOnSlope(slope,angle=(3,1)):
    currentPosition = 0
    output = 0
    for lineIndex in range(len(slope)):
        if lineIndex%angle[1] != 0:
            continue
        if slope[lineIndex][currentPosition] == '#':
            output += 1
        currentPosition += angle[0]
        if currentPosition >= len(slope[lineIndex]):
            currentPosition -= len(slope[lineIndex])
    return output