import pygame


class Field:
    def __init__(self, screen, x, y, content):
        self.screen = screen
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont('ligconsolata', 80)
        self.size = 100
        self.border_size = self.size * 0.01
        self.content = content if content != '0' else ''
        self.isFixed = content != '0'
        self.isSelected = False

    def display(self):
        background_color = (245, 245, 245) if self.isFixed else (
            (0, 255, 255) if self.isSelected else (255, 255, 255))
        if self.isSelected:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                self.x, self.y, self.size, self.size))
            pygame.draw.rect(self.screen, background_color, pygame.Rect(
                self.x + 2*self.border_size, self.y + 2*self.border_size, self.size -
                4*self.border_size, self.size - 4*self.border_size)
            )
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                self.x, self.y, self.size, self.size))
            pygame.draw.rect(self.screen, background_color, pygame.Rect(
                self.x + self.border_size, self.y + self.border_size, self.size -
                2*self.border_size, self.size - 2*self.border_size)
            )

        if self.content != "":
            text = self.font.render(
                self.content, True, (0, 0, 0), background_color)
            textRect = text.get_rect()
            textRect.center = (self.x + self.size/2,
                               self.y + self.size/2)
            self.screen.blit(text, textRect)

    def select(self):
        self.isSelected = True
        self.display()

    def unselect(self):
        self.isSelected = False
        self.display()

    def updateNumber(self, number):
        self.content = number
        self.display()
