from manim import *
from renderer import primitives
from renderer import animations


class DrawingTest(Scene):
    def construct(self):

        # Create primitives
        circle = primitives.Circle(radius=1)
        rectangle = primitives.Rectangle(width=3, height=1.5)
        text = primitives.Text("StickMan Studio")

        # Position objects
        circle.object.shift(LEFT * 3)
        rectangle.object.shift(RIGHT * 2)
        text.object.shift(UP * 2.5)

        # Create objects
        self.play(animations.create(circle))
        self.play(animations.create(rectangle))
        self.play(animations.write(text))

        self.wait(1)

        # Move the circle
        self.play(
            animations.move(circle, RIGHT * 3)
        )

        # Scale the rectangle
        self.play(
            animations.scale(rectangle, 1.5)
        )

        # Rotate the rectangle
        self.play(
            animations.rotate(rectangle, PI / 2)
        )

        self.wait(2)

        # Fade everything out
        self.play(animations.fade_out(circle))
        self.play(animations.fade_out(rectangle))
        self.play(animations.fade_out(text))

        self.wait(1)