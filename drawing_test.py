from manim import *
from renderer import primitives

class DrawingTest(Scene):
    def construct(self):

        #Creating StickMan Studio primitives
        circle = primitives.Circle(radius=1)
        rectangle = primitives.Rectangle(width=3, height=1.5)
        line = primitives.Line(LEFT * 2, RIGHT * 2)
        text = primitives.Text("StickMan Studio")

        #Below we are positioning the objects
        circle.object.shift(UP * 1.5)
        rectangle.object.shift(DOWN * 1.5)
        text.object.shift(UP * 3)

        #Showing / Displaying the objects that are rendered
        self.play(Create(circle.object))
        self.play(Create(rectangle.object))
        self.play(Create(line.object))
        self.play(Create(text.object))

        self.wait(2)