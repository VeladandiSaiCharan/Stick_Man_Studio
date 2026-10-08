from manim import VGroup

class Character:
    def __init__(self, name):
        self.name = name
        self.group = VGroup()

    def get_group(self):
        return self.group

    def get_name(self):
        return self.name

    def move_to(self, position):
        self.group.move_to(position)

    def shift(self, direction):
        self.group.shift(direction)