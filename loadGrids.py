import random


def getRandomPuzzle():
    with open('grids.txt') as file:
        lines = file.readlines()

    puzzles = []
    counter = 0
    puzzle = []
    for line in lines:
        row = []
        counter += 1
        if "Grid" in line:
            counter = 0
        if counter > 0:
            l = line.rstrip()
            for char in l:
                row.append(char)
            puzzle.append(row)
        if counter == 9:
            puzzles.append(puzzle)
            puzzle = []

    return puzzles[random.randint(0, len(lines)/10-1)]
