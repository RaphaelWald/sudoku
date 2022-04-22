import pygame
from sudoku_field import Field
from outer_grid import displayOuterGrid

# Import and initialize the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([900, 1000])
screen.fill((255, 255, 255))

selected_row, selected_column = -1, -1

fields = []
for i in range(9):
    row = []
    for j in range(9):
        field = Field(screen, 100*i, 100*j)
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
                if selected_row >= 0 and selected_column >= 0:
                    fields[selected_row][selected_column].unselect()
                row, column = int(x / 100), int(y / 100)
                fields[row][column].select()
                selected_row, selected_column = row, column

    # Flip the display
    displayOuterGrid(screen)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
