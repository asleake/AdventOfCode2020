"""Day 2 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 2."""

from common.imports import importAdventFile
from common.string_functions import *

data = importAdventFile('data/Day2Input')
data = [string.split() for string in data]

def FirstPart():
    """ Find the passwords that have the correct number of specified letters """  
    return passwordChecker_incorrect(data)


def SecondPart():
    """ Find the passwords that have the correct number of specified letters in the specified 
        locations"""
    return passwordChecker(data)


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))