from manim import (
    VGroup,
    Rectangle,
    Text,
    SurroundingRectangle,
    FadeIn,
    FadeOut,
    Create,
    DOWN,
    RIGHT,
    LEFT,
    YELLOW,
)

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

        #Currently highlightes line
        self.highlight = None
        self.highlighted_line = None

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

    #High light the required code line during video

    def create_line_highlight(self, line_number):
        """
        Create a highlight rectangle around a code line.
        """

        if line_number < 1:
            raise ValueError(
                "Line number must start from 1."
            )

        if line_number > len(self.lines):
            raise ValueError(
                f"Line number {line_number} "
                f"does not exist."
            )

        line = self.lines[line_number - 1]

        highlight = SurroundingRectangle(
            line,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.15,
            buff=0.08,
            stroke_width=1.5
        )

        return highlight

    #Set the highlighted line

    def highlight_line(self, line_number):
        """
        Set the currently highlighted line.
        Returns the new highlight rectangle.
        """

        highlight = self.create_line_highlight(
            line_number
        )

        self.highlight = highlight
        self.highlighted_line = line_number

        return highlight

    #Create an animated highlight

    def animate_highlight_line(self, line_number):
        """
        Create a new highlight and return an animation that displays it.
        """

        highlight = self.create_line_highlight(
            line_number
        )

        self.highlight = highlight
        self.highlighted_line = line_number

        return highlight, FadeIn(highlight)

    #Clear the current highlight

    def clear_highlight(self):
        """
        Clear the stored highlight state.
        """

        self.highlight = None
        self.highlighted_line = None

    #Get current highlight

    def get_highlight(self):
        """
        Return the current highlight object.
        """

        return self.highlight

    #Animate changing the highlighted line

    def animate_change_highlight(self, line_number):
        """
        Return animations for moving the highlight
        from the current line to another line
        """

        new_highlight = self.create_line_highlight(
            line_number
        )

        old_highlight = self.highlight

        self.highlight = new_highlight
        self.highlighted_line = line_number

        animations = []

        if old_highlight is not None:
            animations.append(
                FadeOut(old_highlight)
            )

        animations.append(
            FadeIn(new_highlight)
        )

        return new_highlight, animations

    #Get typing animations

    def get_typing_animations(self, characters_per_second=15):
        """
        Return animations that reveal the code token by token
        in source order.

        characters_per_second controls how quickly the code appears. 
        """

        if characters_per_second <= 0:
            raise ValueError(
                "characters_per_second must be greater than 0."
            )

        animations = []

        for line_group in self.lines:
            for token_mobject in line_group:

                character_count = len(
                    token_mobject.text
                )

                run_time = max(
                    0.05,
                    character_count
                    / characters_per_second
                )

                animations.append(
                    FadeIn(
                        token_mobject,
                        run_time=run_time
                    )
                )

        return animations