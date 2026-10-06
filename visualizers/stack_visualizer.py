from manim import (
    VGroup,
    Rectangle,
    Text,
    UP,
    RIGHT,
    YELLOW,
    BLUE,
    WHITE,
    SurroundingRectangle,
)


class StackVisualizer:

    def __init__(
        self,
        values=None,
        cell_width=1.6,
        cell_height=0.8,
        font_size=24,
        cell_spacing=0.05,
    ):
        self.values = list(values) if values else []

        self.cell_width = cell_width
        self.cell_height = cell_height
        self.font_size = font_size
        self.cell_spacing = cell_spacing

        self.cells = []
        self.values_text = []

        self.top_text = None

        # Stores the actual highlight object
        self.highlight_object = None
        self.highlighted_index = None

        self.group = VGroup()

        self._create_stack()

    def _create_stack(self):
        self.cells = []
        self.values_text = []

        for value in self.values:

            cell = Rectangle(
                width=self.cell_width,
                height=self.cell_height,
            )

            value_text = Text(
                str(value),
                font_size=self.font_size,
            )

            value_text.move_to(
                cell.get_center()
            )

            self.cells.append(cell)
            self.values_text.append(value_text)

        self._arrange_stack()
        self._create_top_indicator()
        self._rebuild_group()

    def _arrange_stack(self):

        if not self.cells:
            return

        stack_group = VGroup()

        for cell, value_text in zip(
            self.cells,
            self.values_text,
        ):
            stack_group.add(
                VGroup(
                    cell,
                    value_text,
                )
            )

        stack_group.arrange(
            UP,
            buff=self.cell_spacing,
        )

    def _create_top_indicator(self):

        self.top_text = Text(
            "TOP",
            font_size=22,
            color=BLUE,
        )

        if self.cells:

            top_group = VGroup(
                self.cells[-1],
                self.values_text[-1],
            )

            self.top_text.next_to(
                top_group,
                RIGHT,
                buff=0.35,
            )

    def _rebuild_group(self):

        self.group = VGroup()

        for cell, value_text in zip(
            self.cells,
            self.values_text,
        ):
            self.group.add(
                cell,
                value_text,
            )

        if self.top_text is not None:
            self.group.add(
                self.top_text
            )

    # -------------------------
    # Getters
    # -------------------------

    def get_group(self):
        return self.group

    def get_cells(self):
        return self.cells

    def get_values(self):
        return self.values_text

    def get_size(self):
        return len(self.values)

    # -------------------------
    # Stack operations
    # -------------------------

    def is_empty(self):
        return len(self.values) == 0

    def peek(self):

        if self.is_empty():
            raise IndexError(
                "Cannot peek from an empty stack."
            )

        return self.values[-1]

    def push(self, value):

        self.values.append(value)

        self._create_stack()

        return self.group

    def pop(self):

        if self.is_empty():
            raise IndexError(
                "Cannot pop from an empty stack."
            )

        value = self.values.pop()

        self._create_stack()

        return value

    # -------------------------
    # Highlighting
    # -------------------------

    def create_highlight(self, index):

        if index < 0 or index >= len(self.values):
            raise IndexError(
                f"Stack index {index} is out of range."
            )

        return SurroundingRectangle(
            self.cells[index],
            color=YELLOW,
            buff=0.08,
            stroke_width=2,
        )

    def highlight(self, index):

        highlight = self.create_highlight(
            index
        )

        self.highlight_object = highlight
        self.highlighted_index = index

        return highlight

    def clear_highlight(self):

        self.highlight_object = None
        self.highlighted_index = None

    def get_highlight(self):

        return self.highlight_object