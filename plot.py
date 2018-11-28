import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import collections  as mc
import pylab as pl

def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l

def performPlot(plotset):
    plotsetplots = plotset[0]
    del plotsetplots[:2]
    lc = mc.LineCollection(plotsetplots, linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.axis('equal')
    ax.autoscale()
    ax.margins(0.1)
    i = 0
    #for key in plotset[0]:
        #[key[0],key[1]]  , [plotset[0][key][0],plotset[0][key][1]]
    newline([0,0],[10,10])
    plt.savefig('koch.png', transparent=True)
    plt.show()
    

