from manim import *
from visualizers.code_panel import CodePanel


class CodePanelTest(Scene):

    def construct(self):

        # ---------------------------------------------
        # Code to display
        # ---------------------------------------------

        code = """def greet(name):
    print("Hello", name)

greet("World")"""

        # ---------------------------------------------
        # Create CodePanel
        # ---------------------------------------------

        panel = CodePanel(
            code,
            width=7,
            height=4.5,
            title="Python Example"
        )

        # ---------------------------------------------
        # Display the panel
        # ---------------------------------------------

        self.play(
            Create(panel.background)
        )

        self.play(
            Write(panel.title_text)
        )

        self.play(
            Write(panel.code_group)
        )

        self.wait(2)