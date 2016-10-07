from swampy.TurtleWorld import *
import time


def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


def draw(t, length, n, angle):
    if n == 0:
        return
    fd(t, length * n)
    lt(t, angle)
    draw(t, length, n - 0.5, angle)
    rt(t, 2 * angle)
    draw(t, length, n - 0.5, angle)
    lt(t, angle)
    bk(t, length * n)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0


move(bob, 200)
rt(bob)
move(bob, 100)

tiempo1 = time.time()

draw(bob, 15, 7, 40)
lt(bob, 30)


tiempo2 = time.time()
segundosdemorados = tiempo2 - tiempo1

print "segundos demorados: ", segundosdemorados

wait_for_user()
