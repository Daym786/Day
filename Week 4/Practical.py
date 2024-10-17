import math
from math import log2
def preset_functions():
    print(math.sqrt(2401))
    print(log2(1024))

def defining_functions():
    def displayTwice(msg):
        print(msg)
        print(msg)

    displayTwice("Hello World")


#preset_functions()
defining_functions()