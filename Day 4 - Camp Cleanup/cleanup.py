#!/usr/bin/env python

fileName = 'input.txt'

def main():
    with open(fileName, 'r') as file:
        containCount = 0
        overlapCount = 0
        for x in file.readlines():
            x = x.replace(',','-').strip().split('-')
            if containsRange(x):
                containCount+=1
            if overlaps(x):
                overlapCount+=1
        print(containCount)
        print(overlapCount)


def containsRange(x):
    a = set(range(int(x[0]),int(x[1])+1))
    b = set(range(int(x[2]), int(x[3])+1))
    if a.issubset(b) or b.issubset(a):
        return True
    else:
        return False

def overlaps(x):
    a = set(range(int(x[0]), int(x[1]) + 1))
    b = set(range(int(x[2]), int(x[3]) + 1))
    if a & b:
        return True
    else:
        return False

if __name__ == "__main__":
    main()