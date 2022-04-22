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

print(game.isCorrect())
