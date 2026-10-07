from manim import *

from visualizers.array_visualizer import ArrayVisualizer
from visualizers.pointer import Pointer
from visualizers.linked_list_visualizer import LinkedListVisualizer
from visualizers.stack_visualizer import StackVisualizer
from visualizers.queue_visualizer import QueueVisualizer


class CoreVisualizersTest(Scene):

    def construct(self):

        # =================================================
        # 1. ARRAY + POINTER
        # =================================================

        array = ArrayVisualizer(
            [10, 20, 30, 40, 50]
        )

        array_group = array.get_group()

        self.play(
            Create(array_group)
        )

        self.wait(1)

        pointer = Pointer(
            "i",
            array.get_cells()[2],
            direction=DOWN,
        )

        self.play(
            Create(pointer.get_group())
        )

        self.wait(1)

        self.play(
            *pointer.animate_to(
                array.get_cells()[4]
            )
        )

        self.wait(1)

        # Remove array section
        self.play(
            FadeOut(pointer.get_group()),
            FadeOut(array_group)
        )

        self.wait(1)

        # =================================================
        # 2. LINKED LIST
        # =================================================

        linked_list = LinkedListVisualizer(
            [10, 20, 30, 40]
        )

        linked_list_group = linked_list.get_group()

        self.play(
            Create(linked_list_group)
        )

        self.wait(1)

        # Highlight node
        linked_highlight = linked_list.highlight_node(1)

        self.play(
            Create(linked_highlight)
        )

        self.wait(1)

        self.play(
            FadeOut(linked_highlight)
        )

        linked_list.clear_highlight()

        self.wait(1)

        self.play(
            FadeOut(linked_list_group)
        )

        self.wait(1)

        # =================================================
        # 3. STACK
        # =================================================

        stack = StackVisualizer(
            [10, 20, 30]
        )

        stack_group = stack.get_group()

        self.play(
            Create(stack_group)
        )

        self.wait(1)

        stack_highlight = stack.highlight(
            stack.get_size() - 1
        )

        self.play(
            Create(stack_highlight)
        )

        self.wait(1)

        self.play(
            FadeOut(stack_highlight)
        )

        stack.clear_highlight()

        self.wait(1)

        self.play(
            FadeOut(stack_group)
        )

        self.wait(1)

        # =================================================
        # 4. QUEUE
        # =================================================

        queue = QueueVisualizer(
            [10, 20, 30]
        )

        queue_group = queue.get_group()

        self.play(
            Create(queue_group)
        )

        self.wait(1)

        queue_highlight = queue.highlight(0)

        self.play(
            Create(queue_highlight)
        )

        self.wait(1)

        self.play(
            FadeOut(queue_highlight)
        )

        queue.clear_highlight()

        self.wait(1)

        self.play(
            FadeOut(queue_group)
        )

        self.wait(1)

        # =================================================
        # FINAL MESSAGE
        # =================================================

        final_text = Text(
            "Core Visualizers Ready",
            font_size=36
        )

        self.play(
            Write(final_text)
        )

        self.wait(2)

        self.play(
            FadeOut(final_text)
        )