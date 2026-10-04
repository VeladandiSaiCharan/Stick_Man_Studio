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

        highlight = array.highlight_element(2)

        self.play(
            Create(highlight)
        )

        self.wait(2)
        