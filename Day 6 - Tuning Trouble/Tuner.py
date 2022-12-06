#!/usr/bin/env python

fileName = 'input.txt'

def main():
    with open(fileName, 'r') as file:
        # Part 1
        dataStream = file.readline()
        for index in range(0, len(dataStream)):
            if len(list(dict.fromkeys(dataStream[index:index + 4]))) == 4:
                print(dataStream[index:index + 4])
                print(index + 4)
                break
        # Part 2
        for index in range(0, len(dataStream)):
            if len(list(dict.fromkeys(dataStream[index:index + 14]))) == 14:
                print(dataStream[index:index + 14])
                print(index + 14)
                break

if __name__ == "__main__":
    main()
