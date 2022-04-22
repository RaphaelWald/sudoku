from os import getrandom
from loadGrids import getRandomPuzzle
import pygame
from game import Game


# Import and initialize the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([900, 1000])
screen.fill((255, 255, 255))

game = Game(screen, getRandomPuzzle())
game.display()


# Run until the user asks to quit
running = True
while running:
    game.time_display.display_current_time()
    if game.boardIsFilledOut():
        if game.isCorrect():
            print("Puzzle was solved successfully!")
        else:
            print("WRONG")
            pygame.quit()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()

            for button in game.buttons:
                if button.isPosition(x, y):
                    button.color = button.color_on_hover
                else:
                    button.color = button.color_unhovered
                button.display()

            if game.options:
                for button in game.menu.buttons:
                    if button.isPosition(x, y):
                        button.color = button.color_on_hover
                    else:
                        button.color = button.color_unhovered
                    button.display()

        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if y < 900:
                if game.options == False:
                    game.fieldSelected = True
                    if game.selected_row >= 0 and game.selected_column >= 0:
                        game.rows[game.selected_row][game.selected_column].unselect()
                    game.selected_row, game.selected_column = int(
                        x / 100), int(y / 100)
                    game.rows[game.selected_row][game.selected_column].select()
                else:
                    if game.menu.new_game_button.isPosition(x, y):
                        game = Game(screen, getRandomPuzzle())
                        game.display()
                    elif game.menu.restart_button.isPosition(x, y):
                        puzzle = game.current_puzzle
                        game = Game(screen, puzzle)
                    elif game.menu.exit_button.isPosition(x, y):
                        pygame.quit()
            elif game.options_button.isPosition(x, y):
                game.options = not game.options
                game.display()
            elif game.solve_button.isPosition(x, y):
                # Solve the puzzle
                pass

        if event.type == pygame.KEYDOWN:
            if game.fieldSelected and not game.rows[game.selected_row][game.selected_column].isFixed and not game.options:
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
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
