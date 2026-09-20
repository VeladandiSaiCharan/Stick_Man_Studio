from manim import Circle as ManimCircle
from manim import Rectangle as ManimRectangle
from manim import Line as ManimLine
from manim import Text as ManimText


class Circle:
    def __init__(self, radius=1):
        self.object = ManimCircle(radius=radius)


class Rectangle:
    def __init__(self, width=2, height=1):
        self.object = ManimRectangle(
            width=width,
            height=height
        )


class Line:
    def __init__(self, start, end):
        self.object = ManimLine(start, end)


class Text:
    def __init__(self, content):
        self.object = ManimText(content)