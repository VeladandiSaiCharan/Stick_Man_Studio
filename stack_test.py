from manim import *
from visualizers.stack_visualizer import StackVisualizer


class StackTest(Scene):

    def construct(self):

        stack = StackVisualizer(
            [10, 20, 30]
        )

        # Show initial stack
        self.play(
            Create(stack.get_group())
        )

        self.wait(2)

        # Verify peek
        print(
            "Top value:",
            stack.peek()
        )

        self.wait(1)

        # Highlight top
        highlight = stack.highlight(
            stack.get_size() - 1
        )

        self.play(
            Create(highlight)
        )

        self.wait(2)

        self.play(
            FadeOut(highlight)
        )

        stack.clear_highlight()

        # Push 40
        old_group = stack.get_group()

        stack.push(40)

        new_group = stack.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(2)

        # Pop
        old_group = stack.get_group()

        popped_value = stack.pop()

        print(
            "Popped value:",
            popped_value
        )

        new_group = stack.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(2)

        # Final verification
        print(
            "Final top value:",
            stack.peek()
        )

        print(
            "Stack size:",
            stack.get_size()
        )

        self.wait(2)