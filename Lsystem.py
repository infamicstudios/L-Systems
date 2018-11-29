import multiprocessing
import NoTurtle
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import collections  as mc
import time
#import tkinter as tk

def fun(f, q_in, q_out):
    while True:
        i, x = q_in.get()
        if i is None:
            break
        q_out.put((i, f(x)))


def parmap(f, X, nprocs=multiprocessing.cpu_count()):
    q_in = multiprocessing.Queue(1)
    q_out = multiprocessing.Queue()

    proc = [multiprocessing.Process(target=fun, args=(f, q_in, q_out))
            for _ in range(nprocs)]
    for p in proc:
        p.daemon = True
        p.start()

    sent = [q_in.put((i, x)) for i, x in enumerate(X)]
    [q_in.put((None, None)) for _ in range(nprocs)]
    res = [q_out.get() for _ in range(len(sent))]

    [p.join() for p in proc]

    return [x for i, x in sorted(res)]


class Lsystem:

    def __init__(self):
        self.instructions = ""
        self.linesetX1 = ""
        self.linesetX2 = ""
        self.linesetY1 = ""
        self.linesetY2 = ""
    """
        Generates instructions for an l system given a axiom, rules and number of iterations 
        axiom is a string
        rules is a dictionary EG rules = {"X" : "FF", "Y" : "FX"}
        interations is an int that dictates how many times generate with iterate.
    """
    def generate(self, axioms, rules, iterations):
        for _ in range(iterations):
            #    Our newly created axioms from this iteration.
            newAxioms = ''
            #    only use progressbar if it can be imported
            for axiom in axioms:
                if axiom in rules:
                    newAxioms += rules[axiom]
                else:
                    newAxioms += axiom
		    #You will need to iterate through your newAxioms next time, so...
		    #We transfer newAxioms, to axioms that is being iterated on, in the for loop.
            axioms = newAxioms
        self.instructions = axioms
    
    def generateVectorArray(self, angle, distance, scaleFactor = 1):

        fakeTurtle = NoTurtle.UndrawnTurtle()

        commandInverse = False
        coordinates = []

        #generate the empty array which will contain data
        np.empty((4,0), dtype=np.float32, order='C')

        for cmd in self.instructions:
            if cmd == 'F':
                fakeTurtle.forward(distance)
            if cmd == 'B':
                fakeTurtle.backward(distance)
            if cmd == '-':
                fakeTurtle.right(angle) if commandInverse else fakeTurtle.left(angle)
            if cmd == '+':
                fakeTurtle.left(angle) if commandInverse else fakeTurtle.right(angle)
            elif cmd == '|':
                fakeTurtle.left(180)
            elif cmd == '>':
                distance = distance * scaleFactor
            elif cmd == '<':
                distance = distance * scaleFactor
            elif cmd == '&':
                commandInverse = not commandInverse
            elif cmd == "[":
                coordinates.append((fakeTurtle.xcor(),fakeTurtle.ycor()))
            elif cmd == "]":
                fakeTurtle.setpos(coordinates[-1][0], coordinates[-1][1])
                coordinates.pop()
        self.linesetX1 = fakeTurtle.linesetX1
        self.linesetY1 = fakeTurtle.linesetY1
        self.linesetX2 = fakeTurtle.linesetX2
        self.linesetY2 = fakeTurtle.linesetY2
        print(self.linesetY2)
        print(self.linesetX2)
        print(self.linesetX1)
        print(self.linesetY1)

    def plotLines(self, x,y):
        plt.plot(x,y)

    def performPlot(self):
        x = [1]
        y = [1]
        for x1, y1, x2, y2 in zip(self.linesetX1, self.linesetY1, self.linesetX2,self.linesetY2):
            x.append(x1)
            x.append(x2)
            x.append(None)
            y.append(y1)
            y.append(y2)
            y.append(None)
        plt.figure()

        for value in (x,y):
            self.plotLines(x,y)
        #np.apply_along_axis( self.newline, axis=1, arr=self.lineset )
        #results = parmap(self.newline, map(lambda x: x, self.lineset))
        #print(results)
        plt.axis('equal')
        plt.autoscale()
        plt.margins(0.1)
        plt.savefig('koch.png', transparent=True, dpi= 200)
        plt.show()

if __name__ == '__main__':
    start_time = time.time()
    simple = Lsystem()
    simple.generate("F+F+F+F", {'F':'F+F-F-FF+F+F-F'}, 5)
    simple.generateVectorArray(90,20)
    print("--- %s seconds ---" % (time.time() - start_time))
    simple.performPlot()
