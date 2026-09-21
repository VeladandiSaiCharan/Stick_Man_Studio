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


def move(obj, direction):
    return obj.object.animate.shift(direction)


def scale(obj, factor):
    return obj.object.animate.scale(factor)


def rotate(obj, angle):
    return obj.object.animate.rotate(angle)