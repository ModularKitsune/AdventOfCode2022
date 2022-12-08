#!/usr/bin/env python

fileName = 'input.txt'


def main():
    with open(fileName, 'r') as file:
        forrest = []
        for line in file.readlines():
            tempList = [*line.strip('\n')]
            tempList = [int(x) for x in tempList]
            forrest.append(tempList)

        visibleDict = dict()

        for vertIndex in range(0, len(forrest)):
            treeLine = forrest[vertIndex]
            for value in visible(treeLine):
                visibleDict[(value, vertIndex)] = 0
            treeLine.reverse()
            for value in visible(treeLine):
                visibleDict[(len(treeLine) - value - 1, vertIndex)] = 0
            treeLine.reverse()

        for horizIndex in range(0, len(forrest[0])):
            treeLine = []
            for arr in forrest:
                treeLine.append(arr[horizIndex])
            for value in visible(treeLine):
                visibleDict[(horizIndex, value)] = 0
            treeLine.reverse()
            for value in visible(treeLine):
                visibleDict[(horizIndex, len(treeLine) - value - 1)] = 0

        print(len(visibleDict))


def visible(trees):
    baseHeight = -1
    visible = []
    for index in range(0, len(trees)):
        if trees[index] > baseHeight:
            baseHeight = trees[index]
            visible.append(index)
        if baseHeight == 9:
            break
    print(visible)
    return visible


if __name__ == "__main__":
    main()
