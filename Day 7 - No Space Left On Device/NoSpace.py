#!/usr/bin/env python

fileName = 'input.txt'


def main():
    with open(fileName, 'r') as file:
        directories = ['/']
        files = dict()
        currentPath = ''
        directorySizes = dict()
        for line in file.readlines():
            if line[:4] == '$ cd':  # For cd operations
                substr = line[5:].strip('\n')  # Get the cd value
                if substr == '..':
                    currentPath = currentPath[
                                  :currentPath[:-1].rindex('/') + 1]  # Remove last directory from current path
                elif substr[0] == '/':
                    currentPath = '/'
                    # If cding to root, just set path to root. This could also be modified to handle direct root paths.
                else:
                    currentPath += substr + '/'
                    if currentPath not in directories:
                        directories.append(currentPath)
            if line[0].isdigit():  # If the line starts with a file size
                values = line.strip('\n').split()  # Splits string into array of [File size, file name]
                files[currentPath + values[1]] = values[0]
        total = 0
        for directory in directories:
            tempTotal = 0
            for file in files:
                if directory in file:  # If directory paths are not unique this could cause a bug.
                    tempTotal += int(files.get(file))
            directorySizes[
                tempTotal] = directory  # If multiple optimal directories have the same size, this could cause a bug
            if tempTotal <= 100000:
                total += tempTotal
        print(total)

        # Part 2

        spaceNeeded = 30000000 - (70000000 - max(
            directorySizes.keys()))  # The max call is a shortcut to find the size of the root file
        bestKey = max(directorySizes.keys())

        for x in directorySizes.keys():
            if x < bestKey and x > spaceNeeded:
                bestKey = x

        print(bestKey)


if __name__ == "__main__":
    main()
