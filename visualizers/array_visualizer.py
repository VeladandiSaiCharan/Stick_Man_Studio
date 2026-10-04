from manim import (
    VGroup,
    Rectangle,
    Text,
    SurroundingRectangle,
    DOWN,
    RIGHT,
    YELLOW,
    Create,
    FadeIn,
    FadeOut,
    AnimationGroup,
)


class ArrayVisualizer:

    def __init__(
        self,
        values,
        cell_width=1.2,
        cell_height=0.9,
        font_size=24
    ):
        self.values = list(values)

        self.cell_width = cell_width
        self.cell_height = cell_height
        self.font_size = font_size

        self.cells = []
        self.values_text = []
        self.indices_text = []

        self.highlight = None
        self.highlighted_index = None

        self.group = VGroup()

        self._create_array()

    # --------------------------------------------------
    # ARRAY CREATION
    # --------------------------------------------------

    def _create_array(self):
        self._rebuild_array()

    def _rebuild_array(self):

        self.cells = []
        self.values_text = []
        self.indices_text = []

        self.group = VGroup()

        for index, value in enumerate(self.values):

            cell = Rectangle(
                width=self.cell_width,
                height=self.cell_height
            )

            value_text = Text(
                str(value),
                font_size=self.font_size
            )

            value_text.move_to(
                cell.get_center()
            )

            index_text = Text(
                str(index),
                font_size=20
            )

            index_text.next_to(
                cell,
                DOWN,
                buff=0.15
            )

            cell_group = VGroup(
                cell,
                value_text,
                index_text
            )

            self.cells.append(cell)
            self.values_text.append(value_text)
            self.indices_text.append(index_text)

            self.group.add(cell_group)

        self.group.arrange(
            RIGHT,
            buff=0
        )

    # --------------------------------------------------
    # ACCESS METHODS
    # --------------------------------------------------

    def get_group(self):
        return self.group

    def get_cells(self):
        return self.cells

    def get_values(self):
        return self.values_text

    def get_indices(self):
        return self.indices_text

    # --------------------------------------------------
    # VALUE ACCESS
    # --------------------------------------------------

    def get_value(self, index):

        if index < 0 or index >= len(self.values):
            raise IndexError(
                f"Array index {index} is out of range."
            )

        return self.values[index]

    # --------------------------------------------------
    # VALUE UPDATE
    # --------------------------------------------------

    def set_value(self, index, value):

        if index < 0 or index >= len(self.values):
            raise IndexError(
                f"Array index {index} is out of range."
            )

        self.values[index] = value

        new_text = Text(
            str(value),
            font_size=self.font_size
        ).move_to(
            self.cells[index].get_center()
        )

        self.values_text[index].become(
            new_text
        )

        return self.values_text[index]

    # --------------------------------------------------
    # ANIMATED VALUE UPDATE
    # --------------------------------------------------

    def animate_set_value(self, index, value):

        if index < 0 or index >= len(self.values):
            raise IndexError(
                f"Array index {index} is out of range."
            )

        new_text = Text(
            str(value),
            font_size=self.font_size
        ).move_to(
            self.cells[index].get_center()
        )

        self.values[index] = value

        return self.values_text[index].animate.become(
            new_text
        )

    # --------------------------------------------------
    # SWAP
    # --------------------------------------------------

    def swap(self, index1, index2):

        if index1 < 0 or index1 >= len(self.values):
            raise IndexError(
                f"Array index {index1} is out of range."
            )

        if index2 < 0 or index2 >= len(self.values):
            raise IndexError(
                f"Array index {index2} is out of range."
            )

        self.values[index1], self.values[index2] = (
            self.values[index2],
            self.values[index1]
        )

        self.values_text[index1].become(
            Text(
                str(self.values[index1]),
                font_size=self.font_size
            ).move_to(
                self.cells[index1].get_center()
            )
        )

        self.values_text[index2].become(
            Text(
                str(self.values[index2]),
                font_size=self.font_size
            ).move_to(
                self.cells[index2].get_center()
            )
        )

        return (
            self.values_text[index1],
            self.values_text[index2]
        )

    # --------------------------------------------------
    # ANIMATED SWAP
    # --------------------------------------------------

    def animate_swap(self, index1, index2):

        if index1 < 0 or index1 >= len(self.values):
            raise IndexError(
                f"Array index {index1} is out of range."
            )

        if index2 < 0 or index2 >= len(self.values):
            raise IndexError(
                f"Array index {index2} is out of range."
            )

        first = self.values_text[index1]
        second = self.values_text[index2]

        first_position = first.get_center()
        second_position = second.get_center()

        self.values[index1], self.values[index2] = (
            self.values[index2],
            self.values[index1]
        )

        return AnimationGroup(
            first.animate.move_to(second_position),
            second.animate.move_to(first_position)
        )

    # --------------------------------------------------
    # INSERT
    # --------------------------------------------------

    def insert(self, index, value):

        if index < 0 or index > len(self.values):
            raise IndexError(
                f"Array index {index} is out of range."
            )

        self.values.insert(
            index,
            value
        )

        self._rebuild_array()

        return self.group

    # --------------------------------------------------
    # REMOVE
    # --------------------------------------------------

    def remove(self, index):

        if index < 0 or index >= len(self.values):
            raise IndexError(
                f"Array index {index} is out of range."
            )

        removed_value = self.values.pop(index)

        self._rebuild_array()

        return removed_value

    # --------------------------------------------------
    # HIGHLIGHT
    # --------------------------------------------------

    def create_highlight(self, index):

        if index < 0 or index >= len(self.cells):
            raise IndexError(
                f"Array index {index} is out of range."
            )

        return SurroundingRectangle(
            self.cells[index],
            color=YELLOW,
            buff=0.08
        )

    def highlight_element(self, index):

        highlight = self.create_highlight(index)

        self.highlight = highlight
        self.highlighted_index = index

        return highlight

    def clear_highlight(self):

        self.highlight = None
        self.highlighted_index = None

    def get_highlight(self):

        return self.highlight

    # --------------------------------------------------
    # ANIMATED HIGHLIGHT MOVEMENT
    # --------------------------------------------------

    def animate_highlight(self, index):

        if index < 0 or index >= len(self.cells):
            raise IndexError(
                f"Array index {index} is out of range."
            )

        new_highlight = self.create_highlight(index)

        if self.highlight is None:

            self.highlight = new_highlight
            self.highlighted_index = index

            return Create(new_highlight)

        animation = self.highlight.animate.move_to(
            new_highlight.get_center()
        )

        self.highlighted_index = index

        return animation