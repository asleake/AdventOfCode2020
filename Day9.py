"""Day 9 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 9."""

from common.imports import importAdventFile
from collections import deque
from itertools import combinations

data = importAdventFile('data/Day9Input')
data = [int(value) for value in data]

firstPartData = 1309761972

def FirstPart():
    """ Find ... """
    previousValues = deque(data[0:25])
    for checkedValue in data[25:]:
        availableValues = map(sum,combinations(previousValues,2))
        if checkedValue not in availableValues:
            return checkedValue
        previousValues.popleft()
        previousValues.append(checkedValue)
    return 'Not found'

def SecondPart():
    """ Find ... """
    for index,_ in enumerate(data):
        currentValue = 0
        currentIndex = index
        while currentValue < firstPartData:
            currentValue += data[currentIndex]
            currentIndex += 1
        if currentValue == firstPartData:
            return min(data[index:currentIndex])+max(data[index:currentIndex])

    return 'Not Found'

print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))