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