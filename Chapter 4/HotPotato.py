from Queue import Queue

def hotPotato(namelist, num):
    circle = Queue()
    for name in namelist:
        circle.enqueue(name)
    while circle.size()>1:
        for i in range(num):
            circle.enqueue(circle.dequeue())

        circle.dequeue()
    return circle.dequeue()
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))