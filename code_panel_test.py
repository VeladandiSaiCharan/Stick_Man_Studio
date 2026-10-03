from manim import *
from visualizers.code_panel import CodePanel


class CodePanelTest(Scene):

    def construct(self):

        #Example Python code

        code = """def greet(name):
    message = "Hello"
    number = 10
    print(message, name, number)

# Call the function
greet("World")"""

        #Create Code panel

        panel = CodePanel(
            code,
            width=7,
            height=4.5,
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