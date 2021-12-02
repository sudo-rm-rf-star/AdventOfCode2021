# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

RANGE = 3 # range of sliding window

def countIncreasesInDepth(filename: str):
    count = 0  # Amount of increases
    index = 0  # Start of sliding window
    depths = readDepths(filename)

    prevDepth = None
    while index < len(depths):
        depth = sum(depths[index: index+RANGE])
        if prevDepth and depth > prevDepth:
            count += 1
        prevDepth = depth
        index += 1
    return count


def readDepths(filename: str):
    with open(filename) as file:
        return [int(line.strip()) for line in file.readlines()]



if __name__ == '__main__':
    print(countIncreasesInDepth('test'))
    print(countIncreasesInDepth('input'))

