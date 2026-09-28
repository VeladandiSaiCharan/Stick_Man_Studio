import builtins
import io
import keyword
import token
import tokenize

from manim import (
    VGroup,
    Text,
    BLUE_C,
    GREEN_C,
    YELLOW_C,
    ORANGE,
    GRAY_B,
    PURPLE_C,
    WHITE,
)


class SyntaxHighlighter:
    """
    Python syntax highlighter for StickMan Studio.

    Converts Python source code into colored Manim
    Text objects based on Python token types.
    """

    def __init__(
        self,
        font="DejaVu Sans Mono",
        font_size=24
    ):

        self.font = font
        self.font_size = font_size
        self.line_spacing = 0.45

        # ---------------------------------------------
        # Syntax colors
        # ---------------------------------------------

        self.colors = {
            "keyword": BLUE_C,
            "builtin": GREEN_C,
            "string": YELLOW_C,
            "number": ORANGE,
            "comment": GRAY_B,
            "function": PURPLE_C,
            "default": WHITE,
        }

        # ---------------------------------------------
        # Python built-in names
        # ---------------------------------------------

        self.builtins = set(dir(builtins))

        # ---------------------------------------------
        # Measure one normal space
        # ---------------------------------------------

        sample = Text(
            "M",
            font=self.font,
            font_size=self.font_size
        )

        self.space_width = sample.width

    # --------------------------------------------------
    # Determine token color
    # --------------------------------------------------

    def get_token_color(
        self,
        token_type,
        token_string,
        previous_token=None
    ):

        # Python keyword
        if token_type == token.NAME:

            if keyword.iskeyword(token_string):
                return self.colors["keyword"]

            if hasattr(keyword, "issoftkeyword"):
                if keyword.issoftkeyword(token_string):
                    return self.colors["keyword"]

            # Function or class name
            if previous_token in ("def", "class"):
                return self.colors["function"]

            # Python built-in
            if token_string in self.builtins:
                return self.colors["builtin"]

        # String
        if token_type == token.STRING:
            return self.colors["string"]

        # Number
        if token_type == token.NUMBER:
            return self.colors["number"]

        # Comment
        if token_type == token.COMMENT:
            return self.colors["comment"]

        # Everything else
        return self.colors["default"]

    # --------------------------------------------------
    # Create highlighted code
    # --------------------------------------------------

    def highlight(
        self,
        code,
        start_x=0,
        start_y=0,
        line_spacing=None
    ):
        """
        Convert Python source code into colored
        Manim Text objects.

        Returns:
            list[VGroup]
        """

        if line_spacing is None:
            line_spacing = self.line_spacing

        source_lines = code.split("\n")

        # One VGroup for every source-code line.
        line_groups = [
            VGroup()
            for _ in source_lines
        ]

        # ---------------------------------------------
        # Track horizontal position of each line
        # ---------------------------------------------

        line_x = {}
        line_column = {}

        for row in range(1, len(source_lines) + 1):

            line_x[row] = start_x
            line_column[row] = 0

        # ---------------------------------------------
        # Tokenize Python source
        # ---------------------------------------------

        tokens = tokenize.generate_tokens(
            io.StringIO(code).readline
        )

        previous_token = None

        for current_token in tokens:

            token_type = current_token.type
            token_string = current_token.string

            start_row, start_col = current_token.start
            end_row, end_col = current_token.end

            # -----------------------------------------
            # Ignore structural tokens
            # -----------------------------------------

            if token_type in (
                token.ENCODING,
                token.ENDMARKER,
                token.NEWLINE,
                token.NL,
                token.INDENT,
                token.DEDENT,
            ):
                continue

            color = self.get_token_color(
                token_type,
                token_string,
                previous_token
            )

            # -----------------------------------------
            # Single-line token
            # -----------------------------------------

            if start_row == end_row:

                text = source_lines[start_row - 1][
                    start_col:end_col
                ]

                if text:

                    self._place_token(
                        line_groups[start_row - 1],
                        text,
                        start_col,
                        start_row,
                        line_x,
                        line_column,
                        start_x,
                        start_y,
                        line_spacing,
                        color
                    )

            # -----------------------------------------
            # Multi-line token
            # -----------------------------------------

            else:

                for row in range(
                    start_row,
                    end_row + 1
                ):

                    line_index = row - 1

                    if line_index >= len(source_lines):
                        continue

                    if row == start_row:

                        text = source_lines[
                            line_index
                        ][start_col:]

                        column = start_col

                    elif row == end_row:

                        text = source_lines[
                            line_index
                        ][:end_col]

                        column = 0

                    else:

                        text = source_lines[
                            line_index
                        ]

                        column = 0

                    if text:

                        self._place_token(
                            line_groups[line_index],
                            text,
                            column,
                            row,
                            line_x,
                            line_column,
                            start_x,
                            start_y,
                            line_spacing,
                            color
                        )

            # Remember meaningful token.
            if token_type not in (
                token.NEWLINE,
                token.NL,
                token.INDENT,
                token.DEDENT,
            ):
                previous_token = token_string

        return line_groups

    # --------------------------------------------------
    # Place one token
    # --------------------------------------------------

    def _place_token(
        self,
        line_group,
        text,
        source_column,
        row,
        line_x,
        line_column,
        start_x,
        start_y,
        line_spacing,
        color
    ):

        # ---------------------------------------------
        # Add real source-code whitespace
        # ---------------------------------------------

        current_column = line_column[row]

        whitespace = max(
            0,
            source_column - current_column
        )

        line_x[row] += (
            whitespace * self.space_width
        )

        # ---------------------------------------------
        # Create token
        # ---------------------------------------------

        token_text = Text(
            text,
            font=self.font,
            font_size=self.font_size,
            color=color
        )

        # ---------------------------------------------
        # Calculate position
        # ---------------------------------------------

        x_position = (
            line_x[row]
            + token_text.width / 2
        )

        y_position = (
            start_y
            - ((row - 1) * line_spacing)
        )

        token_text.move_to(
            [
                x_position,
                y_position,
                0
            ]
        )

        # ---------------------------------------------
        # Add token to line
        # ---------------------------------------------

        line_group.add(token_text)

        # ---------------------------------------------
        # Move cursor to the end of token
        # ---------------------------------------------

        line_x[row] += token_text.width

        line_column[row] = (
            source_column
            + len(text)
        )