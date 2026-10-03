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
            """10
            20
            30
            Total: 60"""
        )

        self.play(
            Write(output)
        )

        self.wait(2)