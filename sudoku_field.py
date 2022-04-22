import pygame


class Field:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = 100
        self.border_size = self.size * 0.02
        self.content = ""

    def display(self):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
            self.x, self.y, self.size, self.size))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
            self.x + self.border_size, self.y + self.border_size, self.size -
            2*self.border_size, self.size - 2*self.border_size)
        )
