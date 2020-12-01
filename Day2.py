"""Day 2 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 2."""

from common.imports import importAdventFile
from common.perm_functions import multiplicativeSum
from itertools import permutations

data = importAdventFile('data/Day2Input')
data = [int(string) for string in data]

def FirstPart():
    """ Find the two numbers that add to 2020 and return their product"""
    return multiplicativeSum(data,2020,2)


def SecondPart():
    """ Find the three numbers that add to 2020 and return their product"""
    return multiplicativeSum(data,2020,3)


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))