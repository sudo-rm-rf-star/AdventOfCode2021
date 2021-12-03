
def getPowerConsumption(filename: str):
    gammaRate = 0
    epsilonRate = 0
    diagnostics = readDiagnasticReport(filename)
    cols = len(diagnostics)
    rows = len(diagnostics[0])
    for j in range(rows):
        oneBits = sum(int(diagnostics[i][j]) for i in range(len(diagnostics)))
        zeroBits = cols - oneBits
        mostCommonBit = 1 if oneBits > zeroBits else 0
        leastCommonBit = 1 if mostCommonBit == 0 else 0
        gammaRate ^= mostCommonBit
        epsilonRate ^= leastCommonBit
        if j < rows - 1:
            gammaRate <<= 1
            epsilonRate <<= 1
    return gammaRate * epsilonRate


def readDiagnasticReport(filename: str):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    print(getPowerConsumption('test'))
    print(getPowerConsumption('input'))

