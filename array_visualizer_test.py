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

        highlight = array.highlight_element(0)

        self.play(
            Create(highlight)
        )

        self.wait(1)

        self.play(
            array.animate_highlight(1)
        )

        self.wait(1)

        self.play(
            array.animate_highlight(2)
        )

        self.wait(1)

        self.play(
            array.animate_highlight(3)
        )

        self.wait(1)

        self.play(
            array.animate_highlight(4)
        )

        self.wait(2)