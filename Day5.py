"""Day 5 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 5."""

from common.imports import importAdventFile
from common.airport_functions import getSeatIDFromBoardingPass
data = importAdventFile('data/Day5Input')

def FirstPart():
    """ Find ... """ 
    seatIDs = [getSeatIDFromBoardingPass(datum) for datum in data]
    return max(seatIDs)


def SecondPart():
    """ Find ... """ 
    seatIDs = [getSeatIDFromBoardingPass(datum) for datum in data]
    for seatID in seatIDs:
        for seatID in range(min(seatIDs),max(seatIDs)):
            if seatID not in seatIDs:
                return seatID


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))