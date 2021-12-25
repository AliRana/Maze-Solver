#
#import RPi.GPIO as GPIO
import time



class Node():

    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.Parent = parent
        self.Position = position
        self.Distance = 0
        self.Heuristic = 0
        self.TotalCost = 0



    def __eq__(self, other):
        return self.Position == other.Position


#init ##############################################
def Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    pinMotorAON = 17
    pinMotorAForwards = 27
    pinMotorABackwards = 22

    pinMotorBON = 24
    pinMotorBForwards = 25
    pinMotorBBackwards = 23

    pinLineFollower = 14
    pinTrigger = 3
    pinEcho = 4

    Frequency = 20
    DutyCycleA = 75
    DutyCycleB = 75
    DiagonalDutyCycleA = 90
    DiagonalDutyCycleB = 90
    Stop = 0

    ##Distance variables
    HowNear = 15.0
    ReverseTime = 0.5
    TurnTime = 0.75
    
    ##Set pins as a output or input
    GPIO.setup(pinEcho, GPIO.IN)
    GPIO.setup(pinLineFollower, GPIO.IN)

    GPIO.setup(pinMotorAON, GPIO.OUT)
    GPIO.setup(pinMotorAForwards, GPIO.OUT)
    GPIO.setup(pinMotorABackwards, GPIO.OUT)
    GPIO.setup(pinMotorBON, GPIO.OUT)
    GPIO.setup(pinMotorBForwards, GPIO.OUT)
    GPIO.setup(pinMotorBBackwards, GPIO.OUT)
    GPIO.setup(pinTrigger, GPIO.OUT)

    ##Set the GPIO to software PWM at "Frequency" Hertz
    pwmMotorAON = GPIO.PWM(pinMotorAON, Frequency)
    pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
    pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
    pwmMotorBON = GPIO.PWM(pinMotorBON, Frequency)
    pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
    pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

    ##Start the software PWM with a Duty cycle of 0(i.e not moving)
    pwmMotorAON.start(Stop)
    pwmMotorBON.start(Stop)
    pwmMotorAForwards.start(Stop)
    pwmMotorABackwards.start(Stop)
    pwmMotorBForwards.start(Stop)
    pwmMotorBBackwards.start(Stop)

##################################################################
## time parameter 
##pwmMotorAON.start(Stop)
##pwmMotorBON.start(Stop)
##pwmMotorAForwards.start(Stop)
##pwmMotorABackwards.start(Stop)
##pwmMotorBForwards.start(Stop)
##pwmMotorBBackwards.start(Stop)

##Turn all motors off
def StopMotors():
    pwmMotorAON.ChangeDutyCycle(Stop)
    pwmMotorBON.ChangeDutyCycle(Stop)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

##Turn all motors on
def North():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving Forwards")

##Turn both motors backwards
def South():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    print("Moving Backwards")

##Turn Right
def East():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    print("Moving Right")

##Turn Left
def West():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving Left")
    

def NorthEast():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DiagonalDutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DiagonalDutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving NorthEast")
    
def NorthWest():
    pwmMotorAON.ChangeDutyCycle(DiagonalDutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DiagonalDutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving NorthWest")

def SouthEast(): ########### Add time delay/ check variables
    pwmMotorAON.ChangeDutyCycle(DiagonalDutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DiagonalDutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving NorthWest")
    
    
## add extra 4 methods ############################################

def DistanceDetector():
    try:
        # Repeat the next indented block forever
        while True:
            # Set trigger to False (Low)
            GPIO.output(pinTrigger, False)

            # Allow module to settle
            time.sleep(0.5)

            # Send 10us pulse to trigger
            GPIO.output(pinTrigger, True)
            time.sleep(0.00001)
            GPIO.output(pinTrigger, False)

            # Start the timer
            StartTime = time.time()

            # The start time is reset until the Echo pin is taken high (==1)
            while GPIO.input(pinEcho)==0:
                StartTime = time.time()

            # Stop when the Echo pin is no longer high - the end time
            while GPIO.input(pinEcho)==1:
                StopTime = time.time()
                # If the sensor is too close to an object, the Pi cannot
                # see the echo quickly enough, so it has to detect that
                # problem and say what has happened
                if StopTime-StartTime >= 0.04:
                    print ("Hold on there! You're too close for me to see")
                    StopTime = StartTime
                    break

            # Calculate pulse length
            ElapsedTime = StopTime - StartTime

            # Distance pulse travelled in that time is
            # time multiplied by the speed of sound (cm/s)
            Distance = ElapsedTime * 34326

            # That was the distance there and back so halve the value
            Distance = Distance / 2

            print("Distance: %.1f cm" % Distance)

            time.sleep(0.5)

    # If you press CTRL+C, cleanup and stop
    except KeyboardInterrupt:
        # Reset GPIO settings
        GPIO.cleanup()
                             
##Take a measurement of the Distance to the nearest object
def Measure():
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    StartTime = time.time()
    StopTime = StartTime

    while GPIO.input(pinEcho)==0:
        StartTime = time.time()
        StopTime = StartTime

    while GPIO.input(pinEcho)==1:
        StopTime = time.time()
##        If the sensor is too close to an object, the Pi cannot
##        see the echo quicky enough, so it has to detect that
##        problem and say what has happened
        if StopTime-StartTime >= 0.04:
            print("Hold on there! You're too close for me to see")
            StopTime = StartTime
            break
    ElapsedTime = StopTime - StartTime
##  The ElapsedTime is equal to the time it takes to
##  send and receive the signal 
    Distance = (ElapsedTime * 34326)/2
##  The variable is returned so that the other routines
##  can use the Distance detected
    return Distance

##Return True if the ultrasonic sensor sees an obstacle

def IsNearObstacle(localHowNear):
    Distance = Measure()

    print("IsNearObstacle: "+str(Distance))
    if Distance < localHowNear:
        return True
    else:
        return False
##Move back a little, and then turn right

def AvoidObstacle():
    print("South")
    South()
    time.sleep(ReverseTime)
    StopMotors()

    print("East")
    East()
    time.sleep(TurnTime)
    StopMotors()

#############################################################
    
##Return True if the line detector is over the black line
def IsOverBlack():
    if GPIO.input(pinLineFollower) == 0:
        return True
    else:
        return False

##Search for the black line
def SeekLine():
    print("Seeking the Line")
    #The direction the robot will turn - True = Left
    Direction = True

    ##Turn for 0.25s
    SeekSize = 0.25
    
    #A count of the times the robot has looked for the line
    SeekCount = 1
    
    #The maximum time to seek for the line in one direction
    MaxSeekCount = 5

#Turn the robot left and right until it finds the line
#or it has searched for long enough
    
    while SeekCount <= MaxSeekCount:
        #Set the seek time
        SeekTime = SeekSize * SeekCount
        #Start the motors turning in a direction
        if Direction:
            print("Looking West")
            West()
        else:
            print("Looking East")
            East()

        #Save the time it is now
        StartTime = time.time()
        #While the robot is turning for SeekTime seconds,
        #check o see whether the line detector is over black
        while time.time()-StartTime <= SeekTime:
            if IsOverBlack():
                StopMotors()
                #Exit the SeekLine() function returning
                #True- the line was found
                return True
         #The robot has not found the black line yet, so stop    
        StopMotors()
         #Increase the seek count
        SeekCount += 1
         #Change Direction
        Direction = not Direction
        #The line wasn't found, so return false
    return False

################################################################

def AStar(Maze, StartPosition, EndPosition):

    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    StartNode = Node(None, StartPosition)
    StartNode.Distance = StartNode.Heuristic = StartNode.TotalCost = 0
    EndNode = Node(None, EndPosition)
    EndNode.Distance = EndNode.Heuristic = EndNode.TotalCost = 0



    # Initialize both open and closed list
    ListOpen = []
    ListClosed = []



    # Add the start node
    ListOpen.append(StartNode)



    # Loop until you find the end
    while len(ListOpen) > 0:

        # Get the current node
        CurrentNode = ListOpen[0]
        CurrentIndex = 0
        for index, item in enumerate(ListOpen):
            if item.TotalCost < CurrentNode.TotalCost:
                CurrentNode = item
                CurrentIndex = index



        # Pop current off open list, add to closed list
        ListOpen.pop(CurrentIndex)
        ListClosed.append(CurrentNode)

        # Found the goal
        if CurrentNode == EndNode:
            Path = []
            Current = CurrentNode
            while Current is not None:
                Path.append(Current.Position)
                Current = Current.Parent
            return Path[::-1] # Return reversed path

        # Generate children
        Children = []
        for NewPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            NodePosition = (CurrentNode.Position[0] + NewPosition[0], CurrentNode.Position[1] + NewPosition[1])

            # Make sure within range
            if NodePosition[0] > (len(Maze) - 1) or NodePosition[0] < 0 or NodePosition[1] > (len(Maze[len(Maze)-1]) -1) or NodePosition[1] < 0:
                continue

            # Make sure walkable terrain
            if Maze[NodePosition[0]][NodePosition[1]] != 0:
                continue

            # Create new node
            NewNode = Node(CurrentNode, NodePosition)

            # Append
            Children.append(NewNode)

        # Loop through children
        for ChildNode in Children:

            # Child is on the closed list
            for ChildNode_Closed in ListClosed:
                if ChildNode == ChildNode_Closed:
                    continue

            # Create the Distance, Heuristic and TotalCost values
            ChildNode.Distance = CurrentNode.Distance + 1
            ChildNode.Heuristic = ((ChildNode.Position[0] - EndNode.Position[0]) ** 2) + ((ChildNode.Position[1] - EndNode.Position[1]) ** 2)
            ChildNode.TotalCost = ChildNode.Distance + ChildNode.Heuristic

            # Child is already in the open list
            for NodeOpen in ListOpen :
                if ChildNode == NodeOpen and ChildNode.Distance > NodeOpen.Distance:
                    continue

            # Add the child to the open list
            ListOpen.append(ChildNode)


##############################################################

def MovingCar(path,StartPosition,EndPosition):
    try:
        print(path)
        print(path[5][0])
        CurrentVector = StartPosition
        PreVector = [StartPosition]
        NextVector = []
        count = 0
        print("Number of Turns needed to get to exit location", len(path)-1)
        for i in path:
            if count < len(path):
                print()
                NextVector = path[count + 1]
                X_coordinate = NextVector[0]
                Y_coordinate = NextVector[1]
                NewNextVector = path[count+2]
                NewX_coordinate = NewNextVector[0]
                NewY_coordinate = NewNextVector[1]
                X_Direction = NewX_coordinate - X_coordinate
                Y_Direction = NewY_coordinate - Y_coordinate
                print("NextVector is", NextVector)
                print("X Co-ordinate of Next Vector is", X_coordinate)
                print("Y Co-ordinate of Next Vector is", Y_coordinate)
                print("NewNextVector is", NewNextVector)
                print("NewX Co-ordinate of New Next Vector is", NewX_coordinate)
                print("NewY Co-ordinate of New Next Vector is", NewY_coordinate)
                print("New X Direction", X_Direction)
                print("New Y Direction", Y_Direction)
                if X_Direction == 1 and Y_Direction == 0:
                    print("Moving North")
                    #North()
                elif X_Direction == 1 and Y_Direction == 1:
                    print("Moving NorthWest")
                    #NorthWest()
                elif X_Direction == 0 and Y_Direction == 1:
                    print("Moving West")
                    #West()
                elif X_Direction ==-1 and Y_Direction == 1:
                    print("Moving SouthWest")
                    #SouthWest()
                elif X_Direction == -1 and Y_Direction == 0:
                    print("Moving South")
                    #South()
                elif X_Direction == -1 and Y_Direction == -1:
                    print("Moving SouthEast")
                    #SouthEast()
                elif X_Direction == 0 and Y_Direction == -1:
                    print("Moving East")
                    #East()
                elif X_Direction == 1 and Y_Direction == -1:
                    print("Moving NorthEast")
                    #NorthEast()
            count +=  1
    except:
        print("Too Big")
    ##    currentPosistion = StartPosition
##    for co_ordinates in path:
##        if currentPosistion == co_ordinates :
##            print("Start Pos")
##            print(currentPosistion)
##        else :
##            currentPosistion = co_ordinates
            
        
        
       # print("full" , co_ordinates)
       # print("x" , co_ordinates[0])
       # print("y", co_ordinates[1])
        
            

#############################################################


def main():
    Choice = input("What file do you want to load?")
    print(Choice)
    ReadFile = open(Choice+".txt", "r")
    print(ReadFile)
##    if ReadFile.mode() == "r":
##        Maze = ReadFile.read()
##        print(Maze)
    
#reading in form a file

##    Maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##
##            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    
    StartPosition = (0, 0)
    EndPosition = (9, 9)
    Path = AStar(Maze, StartPosition, EndPosition)
    #print(Path)
    MovingCar(Path,StartPosition,EndPosition)


if __name__ == '__main__':

    main()



