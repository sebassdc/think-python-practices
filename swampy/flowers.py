from mypolygon import *
from swampy.TurtleWorld import *


def petalo(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)


def flor(t, n, r, angle):
    for i in range(n):
        petalo(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.000000000000000000001

move(bob, -100)
flor(bob, 7, 60.0, 60.0)

move(bob, 100)
flor(bob, 10, 40.0, 80.0)

move(bob, 100)
flor(bob, 20, 140.0, 20.0)

die(bob)

# dump the contents of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()
