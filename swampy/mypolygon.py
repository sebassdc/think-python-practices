import math
from swampy.TurtleWorld import *


def polyline(t, n, length, angle):
    """Draws n line segments with the given length
    and angle(in degrees) between them.
    t is a turtle"""
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides
    and the given length"""
    angle = 360.0 / n
    polyline(t, n, length, angle)


def square(t, length):
    polygon(t, 4, length)


def arc(t, r, angle):
    """Draws an arc with r radius an
    the given angle"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    """Draws an arc with 360 degrees"""
    print "circle radius:", r
    arc(t, r, 360)
