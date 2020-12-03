"""Day 3 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 3."""

from common.imports import importAdventFile
from common.slope_functions import findTreesOnSlope
data = importAdventFile('data/Day3Input')

def FirstPart():
    """ Find the number of trees for the given slope on the hill """ 
    return findTreesOnSlope(data,(3,1))


def SecondPart():
    """ Find the product of the number of trees for the given slopes on the hill """ 
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    output = 1
    for slope in slopes:
        output *= findTreesOnSlope(data,slope)

    return output

print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))