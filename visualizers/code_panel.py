from manim import VGroup, Rectangle, Text, DOWN, RIGHT

from visualizers.syntax_highlighter import SyntaxHighlighter

class CodePanel:

    """
    Code panel is used to display the source code inside 
    stickman studio scenes.
    """

    def __init__(
            self,
            code,
            width = 7,
            height = 4.5,
            title = "Code",
            syntax_highlight = False
    ):

        self.code = code
        self.width = width
        self.height = height
        self.title = title
        self.syntax_highlight = syntax_highlight

        #background for panel

        self.background = Rectangle(
            width = self.width,
            height = self.height
        )

        #Panel title

        self.title_text = Text(
            self.title,
            font_size = 28
        )

        self.title_text.move_to(
            self.background.get_top() + DOWN * 0.35
        )

        #Code

        if self.syntax_highlight:
            self.highlighter = SyntaxHighlighter(
                font_size = 24
            )

            code_start_x = (
                self.background.get_left()[0] + 0.35
            )

            code_start_y = (
                self.title_text.get_bottom()[1] - 0.35
            )

            self.lines = self.highlighter.highlight(
                code,
                start_x = code_start_x,
                start_y = code_start_y
            )

            self.code_group = VGroup(
                *self.lines
            )

        else:

            self.highlighter = None
            self.lines = []

            for raw_line in code.split("\n"):
                if raw_line.strip() == "":
                    content = " "
                else: 
                    content = raw_line

                code_line = Text(
                    content,
                    font = "DejaVu Sans Mono",
                    font_size=2
                )

                self.lines.append(code_line)

            self.code_group = VGroup(
                *self.lines
            )

            self.code_group.arrange(
                DOWN,
                aligned_edge = RIGHT,
                buff = 0.15
            )

            self.code_group.align_to(
                self.background,
                RIGHT
            )

        #Group the complete Panel together

        self.group = VGroup(
            self.background,
            self.title_text,
            self.code_group
        )

    #Return panel parts

    def get_parts(self):

        return [
            self.background,
            self.title_text,
            self.code_group
        ]

    #Return individual code lines

    def get_lines(self):
        return self.lines

    #Return complete panel 

    def get_group(self):
        return self.group