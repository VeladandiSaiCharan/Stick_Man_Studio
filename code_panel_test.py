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

        self.wait(1)

        #Highlight line 2

        highlight = panel.highlight_line(2)

        self.play(
            FadeIn(highlight)
        )

        self.wait(2)

        #Move highlight to line 4

        old_highlight = highlight

        new_highlight, self.animations = (
            panel.animate_change_highlight(4)
        )

        self.play(
            *self.animations
        )

        self.wait(2)

        #Remove highlight

        self.play(
            FadeOut(new_highlight)
        )

        panel.clear_highlight()

        self.wait(2)