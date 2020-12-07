""" Airport Functions """
import re, math

def checkCustomsGroup(responses):
    numberOfMatches = 0
    if len(responses) < 2:
        return(len(responses[0]))
    for answer in responses[0]:
        restOfGroup = responses[1:]
        count = len([value for response in restOfGroup for value in response if value==answer])
        if count == len(responses) - 1:
            numberOfMatches += 1
    return numberOfMatches

def checkCustomsGroup_incorrect(responses):
    return len(set(''.join(responses)))

def getSeatIDFromBoardingPass(boardingPassString):
    rowString = re.search('[FB]+',boardingPassString).group()
    columnString = re.search('[LR]+',boardingPassString).group()

    row = [0,127]
    for rowLetter in rowString:
        rowRange = row[1] - row[0]
        if rowLetter == 'F':
            row[1] -= math.ceil(rowRange/2)
        elif rowLetter == 'B':
            row[0] += math.ceil(rowRange/2)
    
    column = [0,7]
    for columnLetter in columnString:
        columnRange = column[1] - column[0]
        if columnLetter == 'L':
            column[1] -= math.ceil(columnRange/2)
        elif columnLetter == 'R':
            column[0] += math.ceil(columnRange/2)

    return row[0]*8 + column[0]

class Passport(object):
    def __init__(self,data):
        self.data = {kvPair[0]:kvPair[1] for kvPair in data}

        self.requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
        self.validEyeColors = ['amb','blu','brn','gry','grn','hzl','oth']

        
    
    def checkForDataFields(self):
        # Check for all types
        for field in self.requiredFields:
            if field not in self.data.keys() and field != 'cid':
                return False
        return True

    def checkForDataValidity(self):
        # Regex to check validity
        birthYearValid = re.fullmatch('(19[2-9][0-9])|(200[0-2])',self.data['byr'])
        issueYearValid = re.fullmatch('(201[0-9])|(2020)',self.data['iyr'])
        expirationYearValid = re.fullmatch('(202[0-9])|(2030)',self.data['eyr'])
        if re.fullmatch('.*cm',self.data['hgt']):
            height = self.data['hgt'][:-2]
            heightValid = re.fullmatch('(1[5-8][0-9])|(19[0-3])',height)
        elif re.fullmatch('.*in',self.data['hgt']):
            height = self.data['hgt'][:-2]
            heightValid = re.fullmatch('(59)|(6[0-9])|(7[0-6])',height)
        else:
            heightValid = False
        hairColorValid = re.fullmatch('#([0-9]|[a-f]){6}',self.data['hcl'])
        if self.data['ecl'] in self.validEyeColors:
            eyeColorValid = True
        else:
            eyeColorValid = False
        pidValid = re.fullmatch('[0-9]{9}',self.data['pid'])
        cidValid = True #re.fullmatch('202[0-9]|2030',self.data['cid'])
        
        validity = birthYearValid and issueYearValid and expirationYearValid and heightValid and \
                   hairColorValid and eyeColorValid and pidValid and cidValid

        return validity

        

