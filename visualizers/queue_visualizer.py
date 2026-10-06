from manim import (
    VGroup,
    Rectangle,
    Text,
    RIGHT,
    UP,
    YELLOW,
    BLUE,
    WHITE,
    SurroundingRectangle,
)


class QueueVisualizer:

    def __init__(
        self,
        values=None,
        cell_width=1.5,
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

        self.front_text = None
        self.rear_text = None

        self.highlight_object = None
        self.highlighted_index = None

        self.group = VGroup()

        self._create_queue()

    # -------------------------------------------------
    # Queue creation
    # -------------------------------------------------

    def _create_queue(self):

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

        self._arrange_queue()
        self._create_indicators()
        self._rebuild_group()

    def _arrange_queue(self):

        if not self.cells:
            return

        queue_group = VGroup()

        for cell, value_text in zip(
            self.cells,
            self.values_text,
        ):
            queue_group.add(
                VGroup(
                    cell,
                    value_text,
                )
            )

        queue_group.arrange(
            RIGHT,
            buff=self.cell_spacing,
        )

    # -------------------------------------------------
    # FRONT / REAR
    # -------------------------------------------------

    def _create_indicators(self):

        self.front_text = Text(
            "FRONT",
            font_size=20,
            color=BLUE,
        )

        self.rear_text = Text(
            "REAR",
            font_size=20,
            color=BLUE,
        )

        if self.cells:

            front_group = VGroup(
                self.cells[0],
                self.values_text[0],
            )

            rear_group = VGroup(
                self.cells[-1],
                self.values_text[-1],
            )

            self.front_text.next_to(
                front_group,
                UP,
                buff=0.25,
            )

            self.rear_text.next_to(
                rear_group,
                UP,
                buff=0.25,
            )

    # -------------------------------------------------
    # Group
    # -------------------------------------------------

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

        if self.front_text is not None:
            self.group.add(
                self.front_text
            )

        if self.rear_text is not None:
            self.group.add(
                self.rear_text
            )

    # -------------------------------------------------
    # Getters
    # -------------------------------------------------

    def get_group(self):
        return self.group

    def get_cells(self):
        return self.cells

    def get_values(self):
        return self.values_text

    def get_size(self):
        return len(self.values)

    # -------------------------------------------------
    # Queue state
    # -------------------------------------------------

    def is_empty(self):

        return len(self.values) == 0

    def peek(self):

        if self.is_empty():
            raise IndexError(
                "Cannot peek from an empty queue."
            )

        return self.values[0]

    # -------------------------------------------------
    # Enqueue
    # -------------------------------------------------

    def enqueue(self, value):

        self.values.append(value)

        self._create_queue()

        return self.group

    # -------------------------------------------------
    # Dequeue
    # -------------------------------------------------

    def dequeue(self):

        if self.is_empty():
            raise IndexError(
                "Cannot dequeue from an empty queue."
            )

        value = self.values.pop(0)

        self._create_queue()

        return value

    # -------------------------------------------------
    # Highlight
    # -------------------------------------------------

    def create_highlight(self, index):

        if index < 0 or index >= len(self.values):
            raise IndexError(
                f"Queue index {index} is out of range."
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