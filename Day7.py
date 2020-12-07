"""Day 7 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 7."""

from common.imports import importAdventFile, bagSplit
from common.airport_functions import countAllBagsIn, howManyBagColorsContain

data = importAdventFile('data/Day7Input')
targetBag = 'shiny gold'
organizedBags = bagSplit(data)

def FirstPart():
    """ Find how many colors of bag eventually contain a shiny gold bag """
    return howManyBagColorsContain(targetBag, organizedBags)
    

def SecondPart():
    """ Find the total number of bags that a shiny gold bag contains """
    return countAllBagsIn(targetBag, organizedBags)


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))