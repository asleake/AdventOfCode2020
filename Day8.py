"""Day 8 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 8."""

from common.imports import importAdventFile, bagSplit
from copy import deepcopy

data = importAdventFile('data/Day8Input')
data = [[command.split()[0],int(command.split()[1])] for command in data]
instructions = ['nop','jmp','acc']

def FirstPart():
    """ Find ... """
    index = 0
    indexList = []
    accumulation = 0
    while True:
        if index in indexList:
            break
        indexList.append(index)

        command,value = data[index]
        if command == 'acc':
            accumulation += value
            index += 1
        elif command == 'nop':
            index += 1
        elif command == 'jmp':
            index += value


    return accumulation
    

def SecondPart():
    """ Find ... """
    index = 0
    indexList = []
    accumulation = 0
    for fixIndex,command in enumerate(data):
        [instruction,_] = command
        data_copy = deepcopy(data)
        if instruction == instructions[2]:
            continue
        else:
            data_copy[fixIndex][0] = instructions[not instruction == instructions[1]]

        index = 0
        indexList = []
        accumulation = 0
        passing = False
        while passing == False:
            try:
                data_copy[index]
            except IndexError:
                passing = True
                break
            if index in indexList:
                break
            indexList.append(index)

            currentCommand,currentValue = data_copy[index]
            if currentCommand == 'acc':
                accumulation += currentValue
                index += 1
            elif currentCommand == 'nop':
                index += 1
            elif currentCommand == 'jmp':
                index += currentValue

        if passing == True:
            break


    return accumulation

print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))