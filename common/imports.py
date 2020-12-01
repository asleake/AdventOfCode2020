def importAdventFile(filename):
    f = open(filename)
    output = f.readlines()
    f.close()

    output = [line.strip() for line in output]

    return output