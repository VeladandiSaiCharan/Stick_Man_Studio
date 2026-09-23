from manim import UP
from renderer.primitives import Circle, Line


class StickMan:

    def __init__(self):

        # Head design
        self.head = Circle(radius=0.5)
        self.head.object.shift(UP * 0.6)

        # Body design
        self.body = Line(
            start=(0, 0, 0),
            end=(0, -1.5, 0)
        )

        # Left arm design
        self.left_arm = Line(
            start=(0, -0.4, 0),
            end=(-0.8, -1.0, 0)
        )

        # Right arm design
        self.right_arm = Line(
            start=(0, -0.4, 0),
            end=(0.8, -1.0, 0)
        )

        # Left leg design
        self.left_leg = Line(
            start=(0, -1.5, 0),
            end=(-0.7, -2.4, 0)
        )

        # Right leg design
        self.right_leg = Line(
            start=(0, -1.5, 0),
            end=(0.7, -2.4, 0)
        )

    def get_parts(self):

        return [
            self.head,
            self.body,
            self.left_arm,
            self.right_arm,
            self.left_leg,
            self.right_leg,
        ]

    def move_to(self, position):
        """Moves the entire StickMan to a position."""

        for part in self.get_parts():
            part.object.move_to(
                part.object.get_center() + position
            )

    def shift(self, direction):
        """Shifts the entire in a Direction based on the requirement"""

        for part in self.get_parts():
            part.object.shift(direction)