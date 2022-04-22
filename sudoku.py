from os import getrandom
import pygame
from sudoku_field import Field
from outer_grid import displayOuterGrid
from loadGrids import getRandomPuzzle

# Import and initialize the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([900, 1000])
screen.fill((255, 255, 255))

selected_row, selected_column = -1, -1
fieldSelected = False

puzzle = getRandomPuzzle()
fields = []
for i in range(9):
    row = []
    for j in range(9):
        field = Field(screen, 100*i, 100*j, puzzle[i][j])
        field.display()
        row.append(field)
    fields.append(row)


displayOuterGrid(screen)
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if (y < 900):
                fieldSelected = True
                if selected_row >= 0 and selected_column >= 0:
                    fields[selected_row][selected_column].unselect()
                selected_row, selected_column = int(x / 100), int(y / 100)
                fields[selected_row][selected_column].select()

        if event.type == pygame.KEYDOWN:
            if fieldSelected and not fields[selected_row][selected_column].isFixed:
                if event.key == pygame.K_1:
                    fields[selected_row][selected_column].updateNumber("1")
                elif event.key == pygame.K_2:
                    fields[selected_row][selected_column].updateNumber("2")
                elif event.key == pygame.K_3:
                    fields[selected_row][selected_column].updateNumber("3")
                elif event.key == pygame.K_4:
                    fields[selected_row][selected_column].updateNumber("4")
                elif event.key == pygame.K_5:
                    fields[selected_row][selected_column].updateNumber("5")
                elif event.key == pygame.K_6:
                    fields[selected_row][selected_column].updateNumber("6")
                elif event.key == pygame.K_7:
                    fields[selected_row][selected_column].updateNumber("7")
                elif event.key == pygame.K_8:
                    fields[selected_row][selected_column].updateNumber("8")
                elif event.key == pygame.K_9:
                    fields[selected_row][selected_column].updateNumber("9")

                # Flip the display
    displayOuterGrid(screen)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
