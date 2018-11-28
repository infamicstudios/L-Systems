import turtle
from Vector import vector2

def lsystem(axioms, rules, iterations):
    #    We iterate through our method required numbers of time.
    for _ in range(iterations):
        #    Our newly created axioms from this iteration.
        newAxioms = ''

        #    This is your code, but with renamed variables, for clearer code.
        for axiom in axioms:
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

    for cmd in instructions:
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


def plotLsystem(aTurtle,instructions,angle,distance, scaleFactor = 1):

    commandInverse = False
    Xcoordinates = [0]
    Ycoordinates = [0]
    coordinates = []
    returnedCoordinate = []
	vec = vector2(0,0)


    for cmd in instructions:
        if cmd == 'F':
            returnCoordiantes.append(vec.Foreward(self, distance))
        elif cmd == 'f':
			#put stuff here later
			print("cool")
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '-' and commandInverse == False:
            vec.turnAntiWise(angle)
        elif cmd == '-' and commandInverse == True:
            vec.turnClockwise(angle)
        elif cmd == '+' and commandInverse == False:
            vec.turnClockwise(angle)
        elif cmd == '+' and commandInverse == True:
            vec.turnAntiWise(angle)
        returnedCoordinate.append([(Xcoordinates[-1],Ycoordinates[-1]),(aTurtle.xcor(), aTurtle.ycor())])
        Xcoordinates.append(aTurtle.xcor())
        Ycoordinates.append(aTurtle.ycor())
    aTurtle.reset()
    return (returnedCoordinate, (max(Xcoordinates)-min(Xcoordinates),max(Ycoordinates)-min(Ycoordinates)))

def main(plot):
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()
    t.up()
    t.back(200)
    t.down()
    t.speed(0)

    rules = { "X" : "X+YF++YF-FX--FXFX-YF+", "Y" : "-FX+YFYF++YF+FX--FX-Y" }
    i = 4
    while True:
        instructions = lsystem('XF', rules, i)
        
        if plot:
            from plot import performPlot
            plotset = plotLsystem(t, instructions, 60, 200*(1/3)**i)
            performPlot(plotset)
        
        else:
            print(drawLsystem(t, instructions, 60, 200*(1/3)**i))
        i += 1
    wn.exitonclick()

main(True)