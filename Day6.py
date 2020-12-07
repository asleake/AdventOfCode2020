"""Day 6 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 6."""

from common.imports import importAdventFile, importAdventFileOnEmptyLines
from common.airport_functions import checkCustomsGroup, checkCustomsGroup_incorrect
data = importAdventFileOnEmptyLines('data/Day6Input')

def FirstPart():
    """ Find the sum of the unique values in each group's customs declaration form """
    return sum([checkCustomsGroup_incorrect(datum) for datum in data])


def SecondPart():
    """ Find the sum shared values in each group's customs declaration form"""
    return sum([checkCustomsGroup(datum) for datum in data])


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))