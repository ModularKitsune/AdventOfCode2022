#!/usr/bin/env python

fileName = 'input.txt'

def main():
    with open(fileName, 'r') as file:
        elves=[]
        tempValue=0
        for x in file:
            if x != '\n':
                tempValue+=int(x.strip())
            else:
                elves.append(tempValue)
                tempValue=0

        #Part 1
        print(max(elves))
        #Part 2
        elves.sort()
        print(sum(elves[-3:]))

if __name__ == "__main__":
    main()