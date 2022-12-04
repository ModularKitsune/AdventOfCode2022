#!/usr/bin/env python

fileName = 'input.txt'


def main():
    with open(fileName, 'r') as file:
        guide = file.readlines()
        # Solution for part 1
        totalScore = 0
        for line in guide:
            values = line.split()
            totalScore += winScore(values) + choiceScore(values[1])
        print(totalScore)
        # Solution for part 2
        totalScore = 0
        for line in guide:
            values = line.split()
            values[1] = calculateResponse(values)
            totalScore += winScore(values) + choiceScore(values[1])
        print(totalScore)


def winScore(values):
    # If Draw
    if ord(values[0]) - ord(values[1]) == -23:
        return 3
    # If Opponent wins
    elif (values[0] == 'A' and values[1] == 'Z') or (values[0] == 'B' and values[1] == 'X') or (
            values[0] == 'C' and values[1] == 'Y'):
        return 0
    # Else we win
    else:
        return 6


def choiceScore(value):
    if value == 'X':
        return 1
    elif value == 'Y':
        return 2
    elif value == 'Z':
        return 3
    else:
        print('Improper input')


def calculateResponse(values):
    # Lose case
    if values[1] == 'X':
        if values[0] == 'A':
            return 'Z'
        elif values[0] == 'B':
            return 'X'
        else:
            return 'Y'
    # Draw case
    elif values[1] == 'Y':
        return chr(ord(values[0]) + 23)
    # Win case
    else:
        if values[0] == 'A':
            return 'Y'
        elif values[0] == 'B':
            return 'Z'
        else:
            return 'X'


if __name__ == "__main__":
    main()
