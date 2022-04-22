import pygame


def displayOuterGrid(screen):
    # Outer Polygon
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 900), 8)
    pygame.draw.line(screen, (0, 0, 0), (896, 0), (896, 900), 8)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (900, 0), 8)
    pygame.draw.line(screen, (0, 0, 0), (0, 896), (900, 896), 8)

    pygame.draw.line(screen, (0, 0, 0), (298, 0), (298, 900), 4)
    pygame.draw.line(screen, (0, 0, 0), (598, 0), (598, 900), 4)

    pygame.draw.line(screen, (0, 0, 0), (0, 298), (900, 298), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 598), (900, 598), 4)
