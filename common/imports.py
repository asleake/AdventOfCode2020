import re

def importAdventFile(filename):
    f = open(filename)
    output = f.readlines()
    f.close()

    output = [line.strip() for line in output]

    return output

def importAdventFileOnEmptyLines(filename):
    f = open(filename)
    output = f.read()
    f.close()

    output = output.split('\n\n')
    output = [group.split('\n') for group in output]

    return output

def bagSplit(bags):
    organizedBags = {}
    for bag in bags:
        bagTypes = re.findall('\w+\s*\w*(?=\sbag)',bag)
        bagNumbers = re.findall('\d',bag)
        container = bagTypes[0]
        contained = bagTypes[1:]
        organizedBags[container] = {}
        for item,quantity in zip(contained,bagNumbers):
            organizedBags[container].update({item:quantity})
    return organizedBags