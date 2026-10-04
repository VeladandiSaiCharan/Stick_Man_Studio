from manim import *
from visualizers.array_visualizer import ArrayVisualizer


class ArrayVisualizerTest(Scene):

    def construct(self):

        # ---------------------------------------------
        # CREATE ARRAY
        # ---------------------------------------------

        array = ArrayVisualizer(
            [10, 20, 30, 40, 50]
        )

        self.play(
            Create(array.get_group())
        )

        self.wait(1)

        # ---------------------------------------------
        # GET VALUE
        # ---------------------------------------------

        value = array.get_value(2)

        print(
            "Value at index 2:",
            value
        )

        self.wait(1)

        # ---------------------------------------------
        # ANIMATED VALUE UPDATE
        # 30 -> 99
        # ---------------------------------------------

        self.play(
            array.animate_set_value(2, 99)
        )

        self.wait(1)

        # ---------------------------------------------
        # ANIMATED SWAP
        # 20 <-> 99
        # ---------------------------------------------

        self.play(
            array.animate_swap(1, 2)
        )

        self.wait(1)

        # ---------------------------------------------
        # SYNCHRONIZE INTERNAL STATE
        # ---------------------------------------------

        array.swap(1, 2)

        self.wait(1)

        # ---------------------------------------------
        # INSERT
        # Insert 25 at index 2
        # ---------------------------------------------

        old_group = array.get_group()

        array.insert(
            2,
            25
        )

        new_group = array.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(1)

        # ---------------------------------------------
        # REMOVE
        # Remove element at index 2
        # ---------------------------------------------

        old_group = array.get_group()

        removed_value = array.remove(2)

        print(
            "Removed value:",
            removed_value
        )

        new_group = array.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(2)