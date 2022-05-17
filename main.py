'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random

#########################################################
#                   Your Code Goes Below                #
#########################################################

def drawSquare(myturtle, width, top_left_x, top_left_y):
  """Outlines the dartboard 
  params: myturtle, width, top_left_x, top_left_y"""
  myturtle.penup()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.pendown()
  x = (width/2)
  myturtle.goto(-x, -x)
  myturtle.goto(x, -x)
  myturtle.goto(x, x)
  myturtle.goto(-x, x)
  myturtle.penup()

def drawLine(myturtle, x_start, y_start, x_end, y_end):
  """Draws a single axis
  Params = myturtle, x_start, y_start, x_end, y_end"""
  myturtle.penup()
  myturtle.goto(x_start, y_start)
  myturtle.pendown()
  myturtle.goto(x_end, y_end)
  myturtle.penup()

def drawCircle(myturtle, radius):
  """Draws a circle
  Params = myturtle, radius"""
  myturtle.goto(0, -1)
  myturtle.pendown()
  myturtle.circle(radius)

def  isInCircle(myturtle, circle_center_x, circle_center_y, radius):
  """Returns = True or False depending on if the turtle argument is within 1 unit away from the circle center
  Params = myturtle, circle_center_x, circle_center_y, radius"""
  if radius > myturtle.distance(circle_center_x, circle_center_y):
    return True
  else:
    return False

def throwDart(myturtle):
  """Throws a dart on the dartboard
  params = myturtle"""
  myturtle.penup()
  myturtle.goto(float(random.randrange(-100, 100)/100), float(random.randrange(-100, 100)/100))
  myturtle.pendown()
  if isInCircle(myturtle, 0, 0, 1) == True:
    myturtle.color('green')
  else:
    myturtle.color('red')
  myturtle.dot()

def playDarts(myturtle):
  """Uses a loop to play the rounds, uses accumulators to keep track of players' points,
uses existing throwDart() function
  Params = myturtle"""
  firstScore = 0
  secondScore = 0
  for i in range(10):
    throwDart(myturtle)
    if isInCircle(myturtle, 0, 0, 1) == True:
      firstScore+=1
    throwDart(myturtle)
    if isInCircle(myturtle, 0, 0, 1) == True:
      secondScore+=1
  if firstScore > secondScore:
    print("Player 1 wins", firstScore, "to", secondScore, "!")
  elif secondScore > firstScore:
    print("Player 2 wins", secondScore, "to", firstScore, "!")
  else:
    print("Tie game", firstScore, "to", secondScore, "!")

def montePi(myturtle, num_darts):
  """Simulation algorithm returns the approximation of pi
  Params = myturtle, num_darts
  Return = inside_count*4"""
  inside_count = 0
  for i in range(num_darts):
    throwDart(myturtle)
    if isInCircle(myturtle, 0, 0, 1) == True:
      inside_count+=1
  return inside_count*4

def setUpDartboard(myscreen, myturtle):
  """Sets up the Dart board
  Params: myscreen, myturtle"""
  turtle.setworldcoordinates(-1, -1, 1, 1)
  myturtle.penup()
  myturtle.color('blue')
  myturtle.pendown()
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle, 0, -1, 0, 1)
  drawCircle(myturtle, 1)

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
