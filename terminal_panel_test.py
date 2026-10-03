from manim import *
from visualizers.terminal_panel import TerminalPanel

class TerminalPanelTest(Scene):

    def construct(self):

        terminal = TerminalPanel(
            width=7,
            height=4,
            title="Terminal"
        )

        self.play(
            Create(terminal.background)
        )

        self.play(
            Write(terminal.title_text)
        )

        self.wait(1)

        output = terminal.set_output(
            """$ python program.py
        Total: 60"""
        )

        output_animations = terminal.get_output_animations()

        for animation in output_animations:
            self.play(animation)
        self.wait(2)