from manim import *
from visualizers.array_visualizer import ArrayVisualizer

class ArrayVisualizerTest(Scene):

    def construct(self):

        array = ArrayVisualizer(
            [10, 20, 30, 40, 50]
        )

        self.play(
            Create(array.get_group())
        )

        self.wait(1)

        #Get value
        value = array.get_value(2)

        print("Value at index 2:", value)

        self.wait(1)

        #Change value
        array.set_value(2, 99)

        self.wait(2)