from manim import (
    Create,
    FadeIn,
    FadeOut,
    Write,
)


def create(obj):
    return Create(obj.object)


def fade_in(obj):
    return FadeIn(obj.object)


def fade_out(obj):
    return FadeOut(obj.object)


def write(obj):
    return Write(obj.object)