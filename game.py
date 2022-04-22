import pygame
from sudoku_field import Field
from loadGrids import getRandomPuzzle


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.empty_fields = 81
        self.current_puzzle = getRandomPuzzle()
        self.rows = self.initRows()
        self.columns = self.initColumns()
        self.blocks = self.initBlocks()
        self.fieldSelected = False
        self.selected_row = -1
        self.selected_column = -1

    def initRows(self):
        rows = []
        for i in range(9):
            row = []
            for j in range(9):
                field = Field(self.screen, 100*i, 100*j,
                              self.current_puzzle[i][j], self)
                if self.current_puzzle[i][j] != '0':
                    self.empty_fields -= 1
                field.display()
                row.append(field)
            rows.append(row)

        return rows

    def initColumns(self):
        columns = [[] for i in range(9)]
        print(columns)
        for i in range(9):
            for j in range(9):
                columns[j].append(self.rows[i][j])

        return columns

    def initBlocks(self):
        blocks = [[] for i in range(9)]

        for i in range(9):
            for j in range(9):
                if i < 3:
                    blocks[int(j/3)].append(self.rows[i][j])
                elif i < 6:
                    blocks[3 + int(j/3)].append(self.rows[i][j])
                else:
                    blocks[6 + int(j/3)].append(self.rows[i][j])

        return blocks

    def boardIsFilledOut(self):
        return self.empty_fields == 0

    def isCorrect(self):
        rows = [int(field.content) for row in self.rows for field in row]
        columns = [int(field.content)
                   for column in self.columns for field in column]
        blocks = [int(field.content)
                  for block in self.blocks for field in block]

        for row in rows:
            if len(set(row)) != 9:
                return False

        for column in columns:
            if len(set(column)) != 9:
                return False

        for block in blocks:
            if len(set(block)) != 9:
                return False

        return True
