import pygame
from sudoku_field import Field
from loadGrids import getRandomPuzzle
import time
from menu import Time_Display, Button


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
        self.time_display = Time_Display(screen)
        self.menu_button = Button(
            screen, 0, 900, 300, 100, "OPTIONS", (0, 150, 0))
        self.solve_button = Button(
            screen, 600, 900, 300, 100, "SOLVE!", (255, 0, 0))

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

    def display(self):
        self.menu_button.display()
        self.solve_button.display()
        for row in self.rows:
            for field in row:
                field.display()

    def boardIsFilledOut(self):
        return self.empty_fields == 0

    def isCorrect(self):

        for i in range(9):
            row, column, block = set(), set(), set()
            for j in range(9):
                row.add(self.rows[i][j].content)
                column.add(self.columns[i][j].content)
                block.add(self.blocks[i][j].content)
            print(row)
            print(column)
            print(block)
            if len(row) != 9 or len(column) != 9 or len(block) != 9:
                return False

        return True

    def displayTime(self):
        pygame.draw.r
