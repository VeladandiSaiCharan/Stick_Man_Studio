from manim import VGroup, Rectangle, Text, DOWN, RIGHT


class CodePanel:
    """
    Basic code panel for displaying source code
    inside a StickMan Studio scene.
    """

    def __init__(
        self,
        code,
        width=6,
        height=4,
        title="Code"
    ):

        self.code = code
        self.width = width
        self.height = height
        self.title = title

        # ---------------------------------------------
        # Create panel background
        # ---------------------------------------------

        self.background = Rectangle(
            width=self.width,
            height=self.height
        )

        # ---------------------------------------------
        # Create and position the title
        # ---------------------------------------------

        self.title_text = Text(
            self.title,
            font_size=28
        )

        self.title_text.move_to(
            self.background.get_top() + DOWN * 0.35
        )

        # ---------------------------------------------
        # Create code lines
        # ---------------------------------------------

        self.lines = []

        for raw_line in self.code.split("\n"):

            # Count indentation before removing it.
            indentation = len(raw_line) - len(raw_line.lstrip(" "))

            # Remove leading whitespace because Manim Text
            # does not reliably use it for visual indentation.
            content = raw_line.strip()

            # Create a small invisible spacer for blank lines.
            if content == "":
                code_line = Text(
                    " ",
                    font="DejaVu Sans Mono",
                    font_size=24
                )
            else:
                code_line = Text(
                    content,
                    font="DejaVu Sans Mono",
                    font_size=24
                )

            # Store indentation information.
            code_line.indentation = indentation

            self.lines.append(code_line)

        # ---------------------------------------------
        # Position code lines
        # ---------------------------------------------

        self.code_group = VGroup()

        # X position for the beginning of the code area.
        code_left = self.background.get_left() + RIGHT * 0.35

        # Starting Y position below the title.
        current_y = self.title_text.get_bottom()[1] - 0.35

        # Distance between code lines.
        line_spacing = 0.45

        for line in self.lines:

            # Convert spaces into a visible indentation amount.
            indent_offset = (
                line.indentation / 4
            ) * 0.3

            # Position the line explicitly.
            line.move_to(
                [
                    code_left[0] + indent_offset + line.width / 2,
                    current_y,
                    0
                ]
            )

            self.code_group.add(line)

            # Move downward for the next line.
            current_y -= line_spacing

        # ---------------------------------------------
        # Group complete panel
        # ---------------------------------------------

        self.group = VGroup(
            self.background,
            self.title_text,
            self.code_group
        )

    def get_parts(self):
        """
        Return all visual components of the code panel.
        """

        return [
            self.background,
            self.title_text,
            self.code_group
        ]

    def get_lines(self):
        """
        Return individual code lines.
        """

        return self.lines

    def get_group(self):
        """
        Return the complete CodePanel as a VGroup.
        """

        return self.group