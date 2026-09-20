from manim import *
from renderer import primitives
from renderer import animations


class DrawingTest(Scene):
    def construct(self):

        # Create StickMan Studio primitives
        circle = primitives.Circle(radius=1)
        rectangle = primitives.Rectangle(width=3, height=1.5)
        line = primitives.Line(LEFT * 2, RIGHT * 2)
        text = primitives.Text("StickMan Studio")

        # Position objects
        circle.object.shift(UP * 1.5)
        rectangle.object.shift(DOWN * 1.5)
        text.object.shift(UP * 3)

        # Create animations using StickMan Studio's animation layer
        self.play(animations.create(circle))
        self.play(animations.create(rectangle))
        self.play(animations.create(line))
        self.play(animations.write(text))

        self.wait(2)

        # Test fade out
        self.play(animations.fade_out(circle))
        self.play(animations.fade_out(rectangle))
        self.play(animations.fade_out(line))
        self.play(animations.fade_out(text))

        self.wait(1)