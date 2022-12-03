#!/usr/bin/env python

fileName = 'input.txt'


def main():
    # Part 1
    with open(fileName, 'r') as file:
        priorityPoints = 0
        for x in file.readlines():
            x = x.strip('\n')
            half = int((len(x)) / 2)
            firstHalf = set(x[:half])
            secondHalf = set(x[half:])
            shared = list(firstHalf & secondHalf)
            priorityPoints += calcPriority(shared[0])
        print(priorityPoints)

    # Part 2
    with open(fileName, 'r') as file:
        priorityPoints = 0
        fileLines = file.readlines()
        while len(fileLines) > 0:
            rucksack1 = set(fileLines.pop().strip('\n'))
            rucksack2 = set(fileLines.pop().strip('\n'))
            rucksack3 = set(fileLines.pop().strip('\n'))
            shared = list(rucksack1 & rucksack2 & rucksack3)
            priorityPoints += calcPriority(shared[0])
        print(priorityPoints)


def calcPriority(letter):
    isUpper = letter.isupper()
    letterValue = ord(letter.upper()) - 64
    if isUpper:
        return letterValue + 26
    else:
        return letterValue


if __name__ == "__main__":
    main()