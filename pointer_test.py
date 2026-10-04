from manim import *
from visualizers.array_visualizer import ArrayVisualizer
from visualizers.pointer import Pointer


class PointerTest(Scene):

    def construct(self):

        # Create array
        array = ArrayVisualizer(
            [10, 20, 30, 40, 50]
        )

        self.play(
            Create(array.get_group())
        )

        self.wait(1)

        # Create first pointer
        pointer_i = Pointer(
            "i",
            array.get_cells()[1],
            direction=DOWN,
        )

        # Create second pointer
        pointer_j = Pointer(
            "j",
            array.get_cells()[3],
            direction=DOWN,
        )

        # Show both pointers
        self.play(
            Create(pointer_i.get_group()),
            Create(pointer_j.get_group()),
        )

        self.wait(2)

        # Move i from index 1 -> index 2
        self.play(
            *pointer_i.animate_to(
                array.get_cells()[2]
            )
        )

        self.wait(1)

        # Move j from index 3 -> index 4
        self.play(
            *pointer_j.animate_to(
                array.get_cells()[4]
            )
        )

        self.wait(2)

        # Move both pointers simultaneously
        self.play(
            *pointer_i.animate_to(
                array.get_cells()[0]
            ),
            *pointer_j.animate_to(
                array.get_cells()[2]
            ),
        )

        self.wait(2)