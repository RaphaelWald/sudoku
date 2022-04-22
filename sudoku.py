from os import getrandom
import pygame
from sudoku_field import Field
from outer_grid import displayOuterGrid
from game import Game


# Import and initialize the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([900, 1000])
screen.fill((255, 255, 255))

game = Game(screen)


displayOuterGrid(screen)
# Run until the user asks to quit
running = True
while running:
    print(game.empty_fields)
    if game.boardIsFilledOut():
        if game.isCorrect:
            print("Puzzle was solved successfully!")
        else:
            print("WRONG")
            pygame.quit()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if (y < 900):
                game.fieldSelected = True
                if game.selected_row >= 0 and game.selected_column >= 0:
                    game.rows[game.selected_row][game.selected_column].unselect()
                game.selected_row, game.selected_column = int(
                    x / 100), int(y / 100)
                game.rows[game.selected_row][game.selected_column].select()

        if event.type == pygame.KEYDOWN:
            if game.fieldSelected and not game.rows[game.selected_row][game.selected_column].isFixed:
                if event.key == pygame.K_1:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "1")
                elif event.key == pygame.K_2:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "2")
                elif event.key == pygame.K_3:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "3")
                elif event.key == pygame.K_4:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "4")
                elif event.key == pygame.K_5:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "5")
                elif event.key == pygame.K_6:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "6")
                elif event.key == pygame.K_7:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "7")
                elif event.key == pygame.K_8:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "8")
                elif event.key == pygame.K_9:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "9")
                elif event.key == pygame.K_BACKSPACE:
                    game.rows[game.selected_row][game.selected_column].updateNumber(
                        "")

                # Flip the display
    displayOuterGrid(screen)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
