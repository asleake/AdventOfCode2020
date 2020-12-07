"""Day 5 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 5."""

from common.imports import importAdventFile
from common.airport_functions import getSeatIDFromBoardingPass
part1Data = importAdventFile('data/Day5Input')
part2Data = importAdventFile('data/Day5Input_2')

def FirstPart():
    """ Find ... """ 
    seatIDs = [getSeatIDFromBoardingPass(datum) for datum in part1Data]
    return max(seatIDs)


def SecondPart():
    """ Find ... """ 
    seatIDs = [getSeatIDFromBoardingPass(datum) for datum in part1Data]
    for seatID in seatIDs:
        for seatID in range(min(seatIDs),max(seatIDs)):
            if seatID not in seatIDs:
                return seatID


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))