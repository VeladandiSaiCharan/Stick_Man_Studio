from manim import *
from visualizers.syntax_highlighter import SyntaxHighlighter


class SyntaxHighlighterTest(Scene):

    def construct(self):

        # ---------------------------------------------
        # Example Python code
        # ---------------------------------------------

        code = """def greet(name):
    message = "Hello"
    number = 10
    print(message, name, number)

# Call the function
greet("World")"""

        # ---------------------------------------------
        # Create syntax highlighter
        # ---------------------------------------------

        highlighter = SyntaxHighlighter(
            font_size=24
        )

        # ---------------------------------------------
        # Generate highlighted code
        # ---------------------------------------------

        lines = highlighter.highlight(
            code,
            start_x=-5,
            start_y=2
        )

        # ---------------------------------------------
        # Display each line
        # ---------------------------------------------

        for line in lines:
            self.play(
                Write(line)
            )

        self.wait(3)