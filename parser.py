import turtle
import NoTurtle
import time
import progressbar
import time
from numba import vectorize
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import collections  as mc
import pylab as pl
from numba import cuda

#@vectorize(['int8(int8, int8)'], target='cuda')

def lsystem(axioms, rules, iterations):
	print("Generating instruction set")
	#    We iterate through our method required numbers of time.
	for _ in range(iterations):
		#    Our newly created axioms from this iteration.
		newAxioms = ''

		#    This is your code, but with renamed variables, for clearer code.
		for axiom in progressbar.progressbar(axioms):
			if axiom in rules:
				newAxioms += rules[axiom]
			else:
				newAxioms += axiom
		#    You will need to iterate through your newAxioms next time, so...
		#    We transfer newAxioms, to axioms that is being iterated on, in the for loop.
		axioms = newAxioms
	return axioms


def drawLsystem(aTurtle,instructions,angle,distance, scaleFactor = 1):

	commandInverse = False
	Xcoordinates = [0]
	Ycoordinates = [0]
	coordinates = []

	aTurtle.penup()
	aTurtle.setposition(0, 0)
	aTurtle.pendown()

	print("Performing Math operations")
	for cmd in progressbar.progressbar(instructions):
		if cmd == 'F':
			aTurtle.forward(distance)
		elif cmd == 'f':
			aTurtle.penup()
			aTurtle.forward(distance)
			aTurtle.pendown()
		elif cmd == 'B':
			aTurtle.backward(distance)
		elif cmd == '-' and commandInverse == False:
			aTurtle.right(angle)
		elif cmd == '-' and commandInverse == True:
			aTurtle.left(angle)
		elif cmd == '+' and commandInverse == False:
			aTurtle.left(angle)
		elif cmd == '+' and commandInverse == True:
			aTurtle.right(angle)
		elif cmd == '|':
			aTurtle.left(180)
		elif cmd == '{':
			aTurtle.fill(True)
			aTurtle.begin_poly()

		elif cmd == '}':
			aTurtle.fill(False)
			aTurtle.end_poly()
		elif cmd == '@':
			aTurtle.dot((distance/2),"black")
		elif cmd == '>':
			distance = distance * scaleFactor
		elif cmd == '<':
			distance = distance * scaleFactor
		elif cmd == '&':
			if commandInverse == True:
				commandInverse = False
			else: 
				commandInverse = True
		elif cmd == "[":
			coordinates.append((aTurtle.xcor(),aTurtle.ycor())) 
		elif cmd == "]":
			aTurtle.penup()
			aTurtle.setposition(coordinates[-1][0], coordinates[-1][1])
			coordinates.pop()
			aTurtle.pendown()
		Xcoordinates.append(aTurtle.xcor()) 
		Ycoordinates.append(aTurtle.ycor())
	return (max(Xcoordinates)-min(Xcoordinates),max(Ycoordinates)-min(Ycoordinates))


def plotLsystem(fakeTurtle,instructions,angle,distance, scaleFactor = 1):

	commandInverse = False
	Xcoordinates = [0]
	Ycoordinates = [0]
	coordinates = []
	returnedCoordinate = []
	print("\n Performing Math operations \n")
	for cmd in  progressbar.progressbar(instructions):
		if cmd == 'F':
			fakeTurtle.forward(distance)
		elif cmd == 'B':
			fakeTurtle.backward(distance)
		elif cmd == '-' and commandInverse == False:
			fakeTurtle.right(angle)
		elif cmd == '-' and commandInverse == True:
			fakeTurtle.left(angle)
		elif cmd == '+' and commandInverse == False:
			fakeTurtle.left(angle)
		elif cmd == '+' and commandInverse == True:
			fakeTurtle.right(angle)
		elif cmd == '|':
			fakeTurtle.left(180)
		#elif cmd == '{':
			#fakeTurtle.fill(True)
			#fakeTurtle.begin_poly()

		#elif cmd == '}':
			#fakeTurtle.fill(False)
			#fakeTurtle.end_poly()
		#elif cmd == '@':
			#fakeTurtle.dot((distance/2),"black")
		elif cmd == '>':
			distance = distance * scaleFactor
		elif cmd == '<':
			distance = distance * scaleFactor
		elif cmd == '&':
			if commandInverse == True:
				commandInverse = False
			else: 
				commandInverse = True
		elif cmd == "[":
			coordinates.append((fakeTurtle.xcor(),fakeTurtle.ycor())) 
		elif cmd == "]":
			fakeTurtle.setpos(coordinates[-1][0], coordinates[-1][1])
			coordinates.pop()
		
		returnedCoordinate.append([(Xcoordinates[-1],Ycoordinates[-1]),(fakeTurtle.xcor(), fakeTurtle.ycor())])
		Xcoordinates.append(fakeTurtle.xcor())
		Ycoordinates.append(fakeTurtle.ycor())
	return (returnedCoordinate, (max(Xcoordinates)-min(Xcoordinates),max(Ycoordinates)-min(Ycoordinates)))

def main(plot):
	fakeTurtle = NoTurtle.UndrawnTurtle()            # create the turtle

	rules = {"X" : "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-", "Y" : "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}
	i = 2
	while True:
		instructions = lsystem('-YF', rules, i)
		
		if plot:
			from plot import performPlot
			plotset = plotLsystem(fakeTurtle, instructions, 90, 1000*(1/3)**i)
			print("Generating plot")
			start_time = time.time()
			lc = performPlot(plotset)
			print("--- %s seconds ---" % (time.time() - start_time))
			fig, ax = pl.subplots()
			ax.add_collection(lc)
			ax.axis('equal')
			ax.autoscale()
			ax.margins(0.1)
			plt.savefig('koch.png', transparent=True, dpi= 1000)
			plt.show()


		else:
			print(drawLsystem(fakeTurtle, instructions, 60, 1000*(1/3)**i))
		i += 1

main(True)