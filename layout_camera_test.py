from manim import *
from renderer import primitives
from renderer.layout import Layout


class LayoutCameraTest(Scene):
    def construct(self):

        # Create StickMan Studio primitives
        circle = primitives.Circle(radius=0.7)
        rectangle = primitives.Rectangle(width=2, height=1)
        text = primitives.Text("StickMan Studio")

        # Position objects using StickMan Studio Layout
        Layout.place(circle, Layout.left())
        Layout.place(rectangle, Layout.right())
        Layout.place(text, Layout.top())

        # Show objects
        self.play(Create(circle.object))
        self.play(Create(rectangle.object))
        self.play(Write(text.object))

        self.wait(2)