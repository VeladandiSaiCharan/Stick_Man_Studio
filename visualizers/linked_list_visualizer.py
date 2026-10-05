from manim import (
    VGroup,
    Rectangle,
    Text,
    Arrow,
    RIGHT,
    DOWN,
    YELLOW,
    BLUE,
    WHITE,
    SurroundingRectangle,
    Create,
    FadeIn,
    FadeOut,
)


class LinkedListNode:
    def __init__(
        self,
        value,
        width=1.6,
        height=0.9,
        font_size=24,
    ):
        self.value = value
        self.width = width
        self.height = height
        self.font_size = font_size

        self.box = Rectangle(
            width=self.width,
            height=self.height,
        )

        self.value_text = Text(
            str(value),
            font_size=self.font_size,
        )

        self.value_text.move_to(
            self.box.get_center()
        )

        self.group = VGroup(
            self.box,
            self.value_text,
        )

    def get_group(self):
        return self.group

    def get_box(self):
        return self.box

    def get_value_text(self):
        return self.value_text

    def get_value(self):
        return self.value


class LinkedListVisualizer:
    def __init__(
        self,
        values,
        node_width=1.6,
        node_height=0.9,
        font_size=24,
        node_spacing=1.0,
    ):
        self.values = list(values)

        self.node_width = node_width
        self.node_height = node_height
        self.font_size = font_size
        self.node_spacing = node_spacing

        self.nodes = []
        self.arrows = []
        self.null_text = None
        self.highlight = None
        self.highlighted_index = None

        self.group = VGroup()

        self._create_list()

    def _create_list(self):
        self.nodes = []
        self.arrows = []

        for value in self.values:
            node = LinkedListNode(
                value,
                width=self.node_width,
                height=self.node_height,
                font_size=self.font_size,
            )

            self.nodes.append(node)

        self._arrange_nodes()
        self._create_arrows()
        self._create_null()

        self._rebuild_group()

    def _arrange_nodes(self):
        if not self.nodes:
            return

        node_groups = VGroup(
            *[
                node.get_group()
                for node in self.nodes
            ]
        )

        node_groups.arrange(
            RIGHT,
            buff=self.node_spacing,
        )

    def _create_arrows(self):
        self.arrows = []

        for index in range(len(self.nodes) - 1):
            current_node = self.nodes[index]
            next_node = self.nodes[index + 1]

            start = (
                current_node.get_box().get_right()
                + RIGHT * 0.05
            )

            end = (
                next_node.get_box().get_left()
                - RIGHT * 0.05
            )

            arrow = Arrow(
                start=start,
                end=end,
                buff=0,
                color=BLUE,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.25,
            )

            self.arrows.append(arrow)

    def _create_null(self):
        self.null_text = Text(
            "NULL",
            font_size=22,
        )

        if self.nodes:
            self.null_text.next_to(
                self.nodes[-1].get_group(),
                RIGHT,
                buff=0.25,
            )

    def _rebuild_group(self):
        self.group = VGroup()

        for node in self.nodes:
            self.group.add(
                node.get_group()
            )

        for arrow in self.arrows:
            self.group.add(arrow)

        if self.null_text is not None:
            self.group.add(self.null_text)

    def get_group(self):
        return self.group

    def get_nodes(self):
        return self.nodes

    def get_arrows(self):
        return self.arrows

    def get_node(self, index):
        if index < 0 or index >= len(self.nodes):
            raise IndexError(
                f"Linked list index {index} is out of range."
            )

        return self.nodes[index]

    def get_value(self, index):
        return self.get_node(index).get_value()

    def create_highlight(self, index):
        node = self.get_node(index)

        return SurroundingRectangle(
            node.get_box(),
            color=YELLOW,
            buff=0.08,
            stroke_width=2,
        )

    def highlight_node(self, index):
        highlight = self.create_highlight(index)

        self.highlight = highlight
        self.highlighted_index = index

        return highlight

    def clear_highlight(self):
        self.highlight = None
        self.highlighted_index = None

    def get_highlight(self):
        return self.highlight

    def insert(self, index, value):
        if index < 0 or index > len(self.values):
            raise IndexError(
                f"Linked list index {index} is out of range."
            )

        self.values.insert(index, value)

        self._create_list()

        return self.group

    def remove(self, index):
        if index < 0 or index >= len(self.values):
            raise IndexError(
                f"Linked list index {index} is out of range."
            )

        removed_value = self.values.pop(index)

        self._create_list()

        return removed_value