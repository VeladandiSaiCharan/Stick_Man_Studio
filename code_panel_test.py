from manim import *
from visualizers.code_panel import CodePanel


class CodePanelTest(Scene):

    def construct(self):

        #Example Python code

        code = """def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    print("Total:", total)
    return total

values = [10, 20, 30]
result = calculate_sum(values)
"""

        #Create Code panel

        panel = CodePanel(
            code,
            width=7,
            height=6.0,
            title="Python Example",
            syntax_highlight=True
        )

        #Show Panel background

        self.play(
            Create(panel.background)
        )

        #Show title

        self.play(
            Write(panel.title_text)
        )

        self.wait(1)

        #Get typing animations

        typing_animations = (
            panel.get_typing_animations(
                characters_per_second=15
            )
        )

        #Type the code

        for animation in typing_animations:

            self.play(animation)

        self.wait(2)