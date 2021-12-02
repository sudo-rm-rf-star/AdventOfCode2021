# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

directions = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1),
}


def getSubmarinePosition(filename: str):
    x, y = 0, 0
    aim = 0
    for dx, aimDiff in readCommands(filename):
        x += dx
        y += aim * dx
        aim += aimDiff

    return x * y


def readCommands(filename: str):
    with open(filename) as file:
        for line in file:
            direction, units = line.split(' ')
            yield tuple(int(units) * pos for pos in directions[direction])


if __name__ == '__main__':
    print(getSubmarinePosition('test'))
    print(getSubmarinePosition('input'))

