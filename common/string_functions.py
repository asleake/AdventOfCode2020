""" String functions """


def passwordChecker_incorrect(data):
    output = 0
    for n,letter,password in data:
        actual = password.count(letter[0])
        amounts = n.split('-')
        if int(amounts[0]) <= actual <= int(amounts[1]):
            output += 1    
    return output

def passwordChecker(data):
    output = 0
    for indices,letter,password in data:
        positions = indices.split('-')
        first = password[int(positions[0])-1] == letter[0]
        second = password[int(positions[1])-1] == letter[0]
        output += 1 if first+second == 1 else 0
    return output

