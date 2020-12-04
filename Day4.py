"""Day 4 of Advent of Code 2020. Running this file will print out the correct answers to the two
puzzles from Day 4."""

from common.imports import importAdventFile
from common.passport import Passport
data = importAdventFile('data/Day4Input')

def FirstPart():
    """ Find ... """ 
    passportIndex = 0
    unenteredPassports = [[]]
    for line in data:
        if line == '':
            passportIndex +=1
            unenteredPassports.append([])
            continue
        for datum in line.split(' '):
            unenteredPassports[passportIndex].append(datum.split(':'))

    validPassports = 0
    passports = []
    for unenteredPassport in unenteredPassports:
        passport = Passport(unenteredPassport)
        passports.append(passport)
        if passport.checkForDataFields():
            validPassports += 1
            
    return validPassports


def SecondPart():
    """ Find ... """ 
    passportIndex = 0
    unenteredPassports = [[]]
    for line in data:
        if line == '':
            passportIndex +=1
            unenteredPassports.append([])
            continue
        for datum in line.split(' '):
            unenteredPassports[passportIndex].append(datum.split(':'))

    validPassports = 0
    passports = []
    for unenteredPassport in unenteredPassports:
        passport = Passport(unenteredPassport)
        passports.append(passport)
        if passport.checkForDataFields():
            if passport.checkForDataValidity():
                validPassports += 1
            
    return validPassports


print("First Puzzle Answer:\t{}\nSecond Puzzle Answer:\t{}\n".format(FirstPart(),SecondPart()))