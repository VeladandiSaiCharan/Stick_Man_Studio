from manim import (
    UP,
    DOWN,
    LEFT,
    RIGHT,
    ORIGIN,
    UL,
    UR,
    DL,
    DR,
)

class VideoFormat:
    """Video formats supported by StickMan Studio."""

    YOUTUBE = {
        "name": "youtube",
        "width": 16,
        "height": 9,
        "aspect_ratio": 16 / 9,
    }

    SHORT = {
        "name": "short",
        "width": 9,
        "height": 16,
        "aspect_ratio": 9 / 16,
    }


class Layout:
    """This is used to provide standard positions for the objects in StickMan Studio"""

    @staticmethod
    def center():
        return ORIGIN

    @staticmethod
    def get_format(video_format):
        """Return the selected video format."""

        if video_format == "youtube":
            return VideoFormat.YOUTUBE

        if video_format == "short":
            return VideoFormat.SHORT

        raise ValueError(
            f"Unknown video format: {video_format}"
        )

    @staticmethod
    def format_name(video_format):
        """Return the name of the selected video format."""

        return Layout.get_format(video_format)["name"]

    @staticmethod
    def top():
        return UP * 2

    @staticmethod
    def bottom():
        return DOWN * 2

    @staticmethod
    def left():
        return LEFT * 3

    @staticmethod
    def right():
        return RIGHT * 3

    @staticmethod
    def top_left():
        return UL * 2

    @staticmethod
    def top_right():
        return UR * 2

    @staticmethod
    def bottom_left():
        return DL * 2

    @staticmethod
    def bottom_right():
        return DR * 2

    @staticmethod
    def place(obj, position):
        obj.object.move_to(position)

    @staticmethod
    def shift(obj, direction):
        obj.object.shift(direction) 