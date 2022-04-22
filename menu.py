from re import X
import time
import pygame


class Button:
    def __init__(self, screen, x, y, x_length, y_length, content, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_length = x_length
        self.y_length = y_length
        self.content = content
        self.font = self.font = pygame.font.SysFont('ligconsolata', 70)
        self.background_color = color

    def display(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
            self.x, self.y, self.x_length, self.y_length))
        pygame.draw.rect(self.screen, self.background_color, pygame.Rect(
            self.x+4, self.y+4, self.x_length-8, self.y_length-8))
        text = self.font.render(
            self.content, True, (255, 255, 255), self.background_color)
        textRect = text.get_rect()
        textRect.center = (self.x + self.x_length/2,
                           self.y + self.y_length/2)
        self.screen.blit(text, textRect)


class Time_Display:
    def __init__(self, screen):
        self.screen = screen
        self.start_time = time.perf_counter()
        self.x = 300
        self.y = 900
        self.x_length = 300
        self.y_length = 100
        self.font = pygame.font.SysFont('ligconsolata', 100)

    def display_current_time(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
            self.x, self.y, self.x_length, self.y_length))
        time_str = self.get_time_as_string(time.perf_counter())
        text = self.font.render(
            time_str, True, (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.x + self.x_length/2,
                           self.y + self.y_length/2)
        self.screen.blit(text, textRect)

    def get_time_as_string(self, current_time):
        time_in_sec = current_time - self.start_time
        minutes = int(time_in_sec / 60)
        seconds = int(time_in_sec % 60)
        min_pre = "0" if minutes < 10 else ""
        min_str = f"{min_pre}{minutes}"
        sec_pre = "0" if seconds < 10 else ""
        sec_str = f"{sec_pre}{seconds}"
        return f"{min_str}:{sec_str}"
