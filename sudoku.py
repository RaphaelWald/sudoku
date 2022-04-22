from cgi import test
import pygame
from sudoku_field import Field
# Simple pygame program

# Import and initialize the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([900, 1000])
screen.fill((255, 255, 255))

fields = []
for i in range(9):
    for j in range(9):
        field = Field(screen, 100*i, 100*j)
        field.display()
        fields.append(field)

        # Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
