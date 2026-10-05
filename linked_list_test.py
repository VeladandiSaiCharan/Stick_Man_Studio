from manim import *
from visualizers.linked_list_visualizer import LinkedListVisualizer


class LinkedListTest(Scene):

    def construct(self):

        # Initial linked list
        linked_list = LinkedListVisualizer(
            [10, 20, 30]
        )

        self.play(
            Create(linked_list.get_group())
        )

        self.wait(1)

        # -------------------------------------------------
        # Highlight node
        # -------------------------------------------------

        highlight = linked_list.highlight_node(1)

        self.play(
            Create(highlight)
        )

        self.wait(1)

        self.play(
            FadeOut(highlight)
        )

        linked_list.clear_highlight()

        self.wait(1)

        # -------------------------------------------------
        # Insert 25 at index 2
        # -------------------------------------------------

        old_group = linked_list.get_group()

        linked_list.insert(
            2,
            25
        )

        new_group = linked_list.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(2)

        # -------------------------------------------------
        # Remove node at index 1
        # -------------------------------------------------

        old_group = linked_list.get_group()

        removed_value = linked_list.remove(1)

        print(
            "Removed value:",
            removed_value
        )

        new_group = linked_list.get_group()

        self.play(
            FadeOut(old_group),
            FadeIn(new_group)
        )

        self.wait(2)

        # -------------------------------------------------
        # Final verification
        # -------------------------------------------------

        print(
            "Value at index 0:",
            linked_list.get_value(0)
        )

        print(
            "Value at index 1:",
            linked_list.get_value(1)
        )

        self.wait(2)