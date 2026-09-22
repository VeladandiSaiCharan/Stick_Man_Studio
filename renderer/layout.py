from manim import (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    ORIGIN,
    UL,
    UR,
    DL,
    DR,
)


class Layout:
    """This is used to provide standard positions for the objects in StickMan Studio"""

    @staticmethod
    def center():
        return ORIGIN

    @staticmethod
    def top():
        return UP * 2

    @staticmethod
    def bottom():
        return DOWN * 2

    @staticmethod
    def left():
        return LEFT * 3

    @staticmethod
    def right():
        return RIGHT * 3

    @staticmethod
    def top_left():
        return UL * 2

    @staticmethod
    def top_right():
        return UR * 2

    @staticmethod
    def bottom_left():
        return DL * 2

    @staticmethod
    def bottom_right():
        return DR * 2

    @staticmethod
    def place(obj, position):
        obj.object.move_to(position)

    @staticmethod
    def shift(obj, direction):
        obj.object.shift(direction) 