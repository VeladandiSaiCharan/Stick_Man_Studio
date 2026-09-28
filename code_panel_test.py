from manim import *
from visualizers.code_panel import CodePanel


class CodePanelTest(Scene):

    def construct(self):

        code = """def greet(name):
    message = "Hello"
    number = 10
    print(message, name, number)

# Call the function
greet("World")"""

        panel = CodePanel(
            code,
            width=7,
            height=4.5,
            title="Python Example",
            syntax_highlight=True
        )

        self.play(
            Create(panel.background)
        )

        self.play(
            Write(panel.title_text)
        )

        self.play(
            Write(panel.code_group)
        )

        self.wait(3)