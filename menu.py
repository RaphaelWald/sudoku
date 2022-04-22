from turtle import position


class Button:
    def __init__(self, position, size, content, onClick):
        self.position = position
        self.size = size
        self.content = content
        self.onClick = onClick
