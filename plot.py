import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import collections  as mc
import pylab as pl
from numba import jit

@cuda.jit
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
	return lc