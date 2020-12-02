"""Day 2 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 2."""

from common.imports import importAdventFile
import re

data = importAdventFile('data/Day2Input')
data = [string.split() for string in data]

def FirstPart():
    """ Find the passwords that have the correct number of specified letters """
    output = 0
    for n,letter,password in data:
        actual = password.count(letter[0])
        amounts = n.split('-')
        if int(amounts[0]) <= actual <= int(amounts[1]):
            output += 1

    
    return output


def SecondPart():
    """ Find the passwords that have the correct number of specified letters in the specified 
        locations"""
    output = 0
    for indices,letter,password in data:
        positions = indices.split('-')
        first = password[int(positions[0])-1] == letter[0]
        second = password[int(positions[1])-1] == letter[0]
        output += 1 if first+second == 1 else 0
    return output


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))