from manim import (
    VGroup,
    Arrow,
    Text,
    UP,
    DOWN,
    BLUE,
    WHITE,
)


class Pointer:
    def __init__(
        self,
        label,
        target,
        direction=DOWN,
        color=BLUE,
        font_size=24,
    ):
        self.label_text = label
        self.target = target
        self.direction = direction
        self.color = color
        self.font_size = font_size

        self.arrow = None
        self.label = None
        self.group = VGroup()

        self._create_pointer()

    def _create_pointer(self):
        target_point = self.target.get_center()

        arrow_start = target_point + self.direction * 1.0
        arrow_end = target_point + self.direction * 0.25

        self.arrow = Arrow(
            start=arrow_start,
            end=arrow_end,
            color=self.color,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )

        self.label = Text(
            self.label_text,
            font_size=self.font_size,
            color=WHITE,
        )

        self.label.next_to(
            self.arrow,
            self.direction,
            buff=0.1,
        )

        self.group = VGroup(
            self.arrow,
            self.label,
        )

    def get_group(self):
        return self.group

    def get_arrow(self):
        return self.arrow

    def get_label(self):
        return self.label

    def move_to_target(self, target):
        self.target = target

        target_point = target.get_center()

        new_arrow_start = target_point + self.direction * 1.0
        new_arrow_end = target_point + self.direction * 0.25

        new_arrow = Arrow(
            start=new_arrow_start,
            end=new_arrow_end,
            color=self.color,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )

        new_label = Text(
            self.label_text,
            font_size=self.font_size,
            color=WHITE,
        )

        new_label.next_to(
            new_arrow,
            self.direction,
            buff=0.1,
        )

        return new_arrow, new_label

    def animate_to(self, target):
        new_arrow, new_label = self.move_to_target(target)

        self.target = target

        return [
            self.arrow.animate.become(new_arrow),
            self.label.animate.become(new_label),
        ]