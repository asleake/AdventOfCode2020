"""Day 10 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 10."""

from common.imports import importAdventFile
from math import prod

data = importAdventFile('data/Day10Input')
data = [int(value) for value in data]

def tribonacci(i):
    tribonacciNumbers = [1,1,2]
    index = 0
    while index < i:
        tribonacciNumbers.append(sum(tribonacciNumbers[index:]))
        index += 1
    return tribonacciNumbers[i]

def FirstPart():
    """ Find ... """
    sortedData = sorted(data+[0, max(data)+3])
    differences = [sortedData[a+1]-sortedData[a] for a in range(len(sortedData)-1)]
    return differences.count(1)*differences.count(3)

def SecondPart():
    """ Find ... """
    sortedData = sorted(data+[0, max(data)+3])
    differences = [sortedData[a+1]-sortedData[a] for a in range(len(sortedData)-1)]
    diffString = ''.join([str(num) for num in differences])
    diffStrings = diffString.split('3')
    testing = [tribonacci(len(string)) for string in diffStrings]
    testOutput = []
    for i,num in enumerate(testing):
        testOutput.append(prod(testing[0:i]))
    return prod([tribonacci(len(string)) for string in diffStrings])
    # Gets the right answer for both test inputs, but not the real input

print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))