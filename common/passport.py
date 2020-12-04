""" Passport """
import re

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
        birthYearValid = re.match('^(19[2-9][0-9])$|(200[0-2])$',self.data['byr'])
        issueYearValid = re.match('^(201[0-9])|(2020)$',self.data['iyr'])
        expirationYearValid = re.match('^(202[0-9])|(2030)$',self.data['eyr'])
        if re.match('.*cm',self.data['hgt']):
            height = self.data['hgt'][:-2]
            heightValid = re.match('^(1[5-8][0-9])|(19[0-3])$',height)
        elif re.match('.*in',self.data['hgt']):
            height = self.data['hgt'][:-2]
            heightValid = re.match('^(59)|(6[0-9])$|(7[0-6])$',height)
        else:
            heightValid = False
        hairColorValid = re.match('#([0-9]|[a-f]){6}$',self.data['hcl'])
        if self.data['ecl'] in self.validEyeColors:
            eyeColorValid = True
        else:
            eyeColorValid = False
        pidValid = re.match('^[0-9]{9}$',self.data['pid'])
        cidValid = True #re.match('202[0-9]|2030',self.data['cid'])
        
        validity = birthYearValid and issueYearValid and expirationYearValid and heightValid and \
                   hairColorValid and eyeColorValid and pidValid and cidValid

        return validity

        

