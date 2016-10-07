from swampy.TurtleWorld import *
import time


def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


def koch(t, length):
    if length < 3:
        fd(t, length)
        return
    koch(t, length/3.0)
    lt(t, 59)
    koch(t, length/3.0)
    rt(t, 120)
    koch(t, length/3.0)
    lt(t, 59)
    koch(t, length/3.0)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0
move(bob, 100)
rt(bob)
move(bob, 200)
lt(bob)


tiempo1 = time.time()
#AQui comienza

koch(bob, 500)

#Aqui termina
tiempo2 = time.time()
segundosdemorados = tiempo2 - tiempo1

print "segundos demorados: ", segundosdemorados

wait_for_user()