# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def countIncreasesInDepth(filename: str):
    count = 0
    prevDepth = None
    for depth in readDepths(filename):
        if prevDepth and depth > prevDepth:
            count += 1
        prevDepth = depth
    return count


def readDepths(filename: str):
    with open(filename) as file:
        for line in file:
            yield int(line.strip())



if __name__ == '__main__':
    print(countIncreasesInDepth('test'))
    print(countIncreasesInDepth('input'))

