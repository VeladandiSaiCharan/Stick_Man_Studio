from manim import *
from visualizers.array_visualizer import ArrayVisualizer

class ArrayVisualizerTest(Scene):

    def construct(self):

        small_array = ArrayVisualizer(
            [5, 10, 15]
        )

        normal_array = ArrayVisualizer(
            [10, 20, 30, 40, 50]
        )

        different_values = ArrayVisualizer(
            [42, 7, 100, 3, 25]
        )

        small_array.get_group().shift(UP * 2)
        normal_array.get_group().shift(UP * 0)
        different_values.get_group().shift(DOWN * 2)

        self.play(
            Create(small_array.get_group())
        )

        self.play(
            Create(normal_array.get_group())
        )

        self.play(
            Create(different_values.get_group())
        )

        self.wait(2)