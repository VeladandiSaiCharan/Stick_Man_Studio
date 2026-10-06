from manim import *
from visualizers.queue_visualizer import QueueVisualizer


class QueueTest(Scene):

    def construct(self):

        # ---------------------------------------------
        # Create queue
        # ---------------------------------------------

        queue = QueueVisualizer(
            [10, 20, 30]
        )

        self.play(
            Create(queue.get_group())
        )

        self.wait(2)

        # ---------------------------------------------
        # Peek
        # ---------------------------------------------

        print(
            "Front value:",
            queue.peek()
        )

        self.wait(1)

        # ---------------------------------------------
        # Highlight FRONT
        # ---------------------------------------------

        highlight = queue.highlight(0)

        self.play(
            Create(highlight)
        )

        self.wait(2)

        self.play(
            FadeOut(highlight)
        )

        queue.clear_highlight()

        self.wait(1)

        # ---------------------------------------------
        # Enqueue 40
        # ---------------------------------------------

        old_group = queue.get_group()

        queue.enqueue(40)

        new_group = queue.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(2)

        # ---------------------------------------------
        # Dequeue
        # ---------------------------------------------

        old_group = queue.get_group()

        removed_value = queue.dequeue()

        print(
            "Dequeued value:",
            removed_value
        )

        new_group = queue.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(2)

        # ---------------------------------------------
        # Final verification
        # ---------------------------------------------

        print(
            "Final front value:",
            queue.peek()
        )

        print(
            "Queue size:",
            queue.get_size()
        )

        self.wait(2)