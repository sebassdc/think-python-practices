
def fourdash():
    print "- - - -",

def linean():
    for i in range(2):
        print "+",
        fourdash()
    print "+"

def lineas():
    print "|\t  |\t    |"

def submain():
    linean()
    for i in range(4):
        lineas()

def square():
    submain()
    submain()
    linean()

square()
