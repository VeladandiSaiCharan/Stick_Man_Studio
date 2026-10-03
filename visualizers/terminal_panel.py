from manim import VGroup, Rectangle, Text, LEFT, RIGHT, DOWN

class TerminalPanel:

    def __init__(
            self,
            width=7,
            height=4,
            title="Terminal"
    ):
        self.width = width
        self.height = height
        self.title = title

        #Terminal background
        self.background = Rectangle(
            width=self.width,
            height=self.height
        )

        #Terminal title
        self.title_text = Text(
            self.title,
            font_size=28
        )

        self.title_text.move_to(
            self.background.get_top() + DOWN * 0.35
        )

        #Output area
        self.output_lines = []

        self.output_group = VGroup()

        #Complete terminal group
        self.group = VGroup(
            self.background,
            self.title_text,
            self.output_group
        )

    def get_parts(self):
        return [
            self.background,
            self.title_text,
            self.output_group
        ]

    def get_group(self):
        return self.group

    def set_output(self, output):
        self.output_lines = []

        for line in str(output).split("\n"):
            output_text = Text(
                line,
                font="DejaVu Sans Mono",
                font_size=24
            )

            self.output_lines.append(output_text)

        self.output_group = VGroup(*self.output_lines)

        self.output_group.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.15
        )

        self.output_group.next_to(
            self.title_text,
            DOWN,
            buff=0.35
        )

        self.output_group.align_to(
            self.background,
            LEFT
        )

        self.output_group.shift(
            RIGHT * 0.5
        )

        self.group = VGroup(
            self.background,
            self.title_text,
            self.output_group
        )

        return self.output_group