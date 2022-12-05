#!/usr/bin/env python
import re

fileName = 'input.txt'


def main():
    # Part 1
    with open(fileName, 'r') as file:
        lines = file.readlines()
        indexLine = lines.index(' 1   2   3   4   5   6   7   8   9\n')
        stacks = setupStacks(lines, indexLine)
        lines = lines[indexLine + 2:]
        for x in lines:
            values = list(map(int, re.findall('\d+', x)))
            for objects in range(0, values[0]):
                stacks[values[2] - 1].append(stacks[values[1] - 1].pop())
        output = ''
        for x in stacks:
            output += x.pop()
        print(output)
    # Part 2
    with open(fileName, 'r') as file:
        lines = file.readlines()
        indexLine = lines.index(' 1   2   3   4   5   6   7   8   9\n')
        stacks = setupStacks(lines, indexLine)
        lines = lines[indexLine + 2:]
        for x in lines:
            values = list(map(int, re.findall('\d+', x)))
            popIndex = len(stacks[values[1] - 1]) - values[0]
            if popIndex < 0:
                popIndex = 0
            for objects in range(0, values[0]):
                stacks[values[2] - 1].append(stacks[values[1] - 1].pop(popIndex))
        output = ''
        for x in stacks:
            output += x.pop()
        print(output)


def setupStacks(lines, indexLine):
    stackCount = int(max(lines[indexLine].split()))
    stacks = []
    for x in range(0, stackCount):
        tempArray = []
        for y in range(0, indexLine + 1):
            if lines[y][(x * 4) + 1].isalpha():
                tempArray.append(lines[y][(x * 4) + 1])
        stacks.append(tempArray)
    for array in stacks:
        array.reverse()
    return stacks


if __name__ == "__main__":
    main()
