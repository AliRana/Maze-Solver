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
    
    MotorAON = 17 
    MotorAForwards = 27 
    MotorABackwards = 22 
    MotorBON = 24 
    MotorBForwards = 25 
    MotorBBackwards = 23 
 
    LineFollower = 14 
    Trigger = 3 
    Echo = 4 

    Frequency = 20 
    DutyCycleA = 75 
    DutyCycleB = 75 
    DiagonalDutyCycleA = 90 
    DiagonalDutyCycleB = 90 
    Stop = 0 

 

    ##Distance variables 
    HowNear = 15.0 
    Reverse_Time = 0.5 
    Turn_Time = 0.75 

     

    ##Set pins as a output or input 
    GPIO.setup(Echo, GPIO.IN) 
    GPIO.setup(LineFollower, GPIO.IN) 

    GPIO.setup(MotorAON, GPIO.OUT) 
    GPIO.setup(MotorAForwards, GPIO.OUT) 
    GPIO.setup(MotorABackwards, GPIO.OUT) 
    GPIO.setup(MotorBON, GPIO.OUT) 
    GPIO.setup(MotorBForwards, GPIO.OUT) 
    GPIO.setup(MotorBBackwards, GPIO.OUT) 
    GPIO.setup(Trigger, GPIO.OUT) 

    ##Set the GPIO to software PWM at "Frequency" Hertz 
    PWM_MotorAON = GPIO.PWM(MotorAON, Frequency) 
    PWM_otorAForwards = GPIO.PWM(MotorAForwards, Frequency) 
    PWM_MotorABackwards = GPIO.PWM(MotorABackwards, Frequency) 
    PWM_MotorBON = GPIO.PWM(MotorBON, Frequency) 
    PWM_MotorBForwards = GPIO.PWM(MotorBForwards, Frequency) 
    PWMMotorBBackwards = GPIO.PWM(MotorBBackwards, Frequency) 

    ##Start the software PWM with a Duty cycle of 0(i.e not moving) 
    PWM_MotorAON.start(Stop) 
    PWM_MotorBON.start(Stop) 
    PWM_MotorAForwards.start(Stop) 
    PWM_MotorABackwards.start(Stop) 
    PWM_MotorBForwards.start(Stop) 
    PWM_MotorBBackwards.start(Stop) 

 

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
    PWM_MotorAON.ChangeDutyCycle(Stop) 
    PWM_MotorBON.ChangeDutyCycle(Stop) 
    PWM_MotorAForwards.ChangeDutyCycle(Stop) 
    PWM_MotorABackwards.ChangeDutyCycle(Stop) 
    PWM_MotorBForwards.ChangeDutyCycle(Stop) 
    PWM_MotorBBackwards.ChangeDutyCycle(Stop) 

 

##Turn all motors on 

def North(): 

    PWM_MotorAON.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorBON.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorAForwards.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorABackwards.ChangeDutyCycle(Stop) 
    PWM_MotorBForwards.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorBBackwards.ChangeDutyCycle(Stop) 
    print("Moving Forwards") 

 

##Turn both motors backwards 

def South():
    
    PWM_MotorAON.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorBON.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorAForwards.ChangeDutyCycle(Stop) 
    PWM_MotorABackwards.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorBForwards.ChangeDutyCycle(Stop) 
    PWM_MotorBBackwards.ChangeDutyCycle(DutyCycleB) 
    print("Moving Backwards") 

 

##Turn Right 

def East(): 

    PWM_MotorAON.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorBON.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorAForwards.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorABackwards.ChangeDutyCycle(Stop) 
    PWM_MotorBForwards.ChangeDutyCycle(Stop) 
    PWM_MotorBBackwards.ChangeDutyCycle(DutyCycleB) 
    print("Moving Right") 

 

##Turn Left 

def West(): 

    PWM_MotorAON.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorBON.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorAForwards.ChangeDutyCycle(Stop) 
    PWM_MotorABackwards.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorBForwards.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorBBackwards.ChangeDutyCycle(Stop) 
    print("Moving Left") 

     

 

def NorthEast(): 

    PWM_MotorAON.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorBON.ChangeDutyCycle(DiagonalDutyCycleB) 
    PWM_MotorAForwards.ChangeDutyCycle(DutyCycleA) 
    PWM_MotorABackwards.ChangeDutyCycle(Stop) 
    PWM_MotorBForwards.ChangeDutyCycle(DiagonalDutyCycleB) 
    PWM_MotorBBackwards.ChangeDutyCycle(Stop) 
    print("Moving NorthEast") 

     

def NorthWest(): 

    PWM_MotorAON.ChangeDutyCycle(DiagonalDutyCycleA) 
    PWM_MotorBON.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorAForwards.ChangeDutyCycle(DiagonalDutyCycleA) 
    PWM_MotorABackwards.ChangeDutyCycle(Stop) 
    PWM_MotorBForwards.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorBBackwards.ChangeDutyCycle(Stop) 
    print("Moving NorthWest") 

 

def SouthEast(): ########### Add time delay/ check variables 

    PWM_MotorAON.ChangeDutyCycle(DiagonalDutyCycleA) 
    PWM_MotorBON.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorAForwards.ChangeDutyCycle(DiagonalDutyCycleA) 
    PWM_MotorABackwards.ChangeDutyCycle(Stop) 
    PWM_MotorBForwards.ChangeDutyCycle(DutyCycleB) 
    PWM_MotorBBackwards.ChangeDutyCycle(Stop) 
    print("Moving NorthWest") 

     

     

## add extra 4 methods ############################################ 

 

def DistanceDetector():
    
    try: 

        # Repeat the next indented block forever 
        while True: 

            # Set trigger to False (Low) 
            GPIO.output(Trigger, False) 

            # Allow module to settle 
            time.sleep(0.5) 

            # Send 10us pulse to trigger
            GPIO.output(Trigger, True) 
            time.sleep(0.00001) 
            GPIO.output(Trigger, False) 

            # Start the timer 
            Start_Time = time.time() 

 
            # The start time is reset until the Echo pin is taken high (==1) 
            while GPIO.input(Echo)==0: 
                Start_Time = time.time() 

            # Stop when the Echo pin is no longer high - the end time 
            while GPIO.input(Echo)==1: 
                Stop_Time = time.time() 
                # If the sensor is too close to an object, the Pi cannot 
                # see the echo quickly enough, so it has to detect that 
                # problem and say what has happened 
                if Stop_Time-Start_Time >= 0.04: 
                    print ("Hold on there! You're too close for me to see") 
                    Stop_Time = Start_Time 
                    break 

 

            # Calculate pulse length 
            TimeElapsed = Stop_Time - Start_Time 

 
            # Distance pulse travelled in that time is 
            # time multiplied by the speed of sound (cm/s) 
            CalculatedDistance = TimeElapsed * 34326 

 

            # That was the distance there and back so halve the value 
            CalculatedDistance = CalculatedDistance / 2 

            print("Distance: %.1f cm" % CalculatedDistance) 

            time.sleep(0.5) 

 
    # If you press CTRL+C, cleanup and stop 
    except KeyboardInterrupt: 
        # Reset GPIO settings 
        GPIO.cleanup() 

                              

##Take a measurement of the Distance to the nearest object 
def Measure(): 
    GPIO.output(Trigger, True) 
    time.sleep(0.00001) 
    GPIO.output(Trigger, False) 
    Start_Time = time.time() 
    Stop_Time = Start_Time 

 

    while GPIO.input(Echo)==0: 
        Start_Time = time.time() 
        Stop_Time = Start_Time 

    while GPIO.input(Echo)==1: 
        Stop_Time = time.time() 
##        If the sensor is too close to an object, the Pi cannot 
##        see the echo quicky enough, so it has to detect that 
##        problem and say what has happened 

        if Stop_Time-Start_Time >= 0.04: 
            print("Hold on there! You're too close for me to see") 
            Stop_Time = Start_Time 
            break 

    TimeElapsed = Stop_Time - Start_Time 
##  The ElapsedTime is equal to the time it takes to 
##  send and receive the signal  
    CalculatedDistance = (TimeElapsed * 34326)/2 
##  The variable is returned so that the other routines 
##  can use the Distance detected 
    return CalculatedDistance 

 

##Return True if the ultrasonic sensor sees an obstacle 

def IsNearObstacle(localHowNear): 
    CalculatedDistance = Measure() 

    print("IsNearObstacle: "+str(CalculatedDistance)) 
    if CalculatedDistance < localHowNear: 
        return True 
    else: 
        return False 
##Move back a little, and then turn right 

def AvoidObstacle(): 

    print("South") 
    South() 
    time.sleep(Reverse_Time) 
    StopMotors() 

    print("East") 
    East() 
    time.sleep(Turn_Time) 
    StopMotors() 

############################################################# 

##Return True if the line detector is over the black line 

def IsOverBlack(): 
    if GPIO.input(LineFollower) == 0: 
        return True 
    else: 
        return False 

##Search for the black line 
def SeekLine(): 
    print("Seeking the Line") 
    #The direction the robot will turn - True = Left 
    Direction_ToMove = True 

    ##Turn for 0.25s 
    Seek_Size = 0.25 

    #A count of the times the robot has looked for the line 
    Seek_Count = 1 

    #The maximum time to seek for the line in one direction 
    MaximumSeek_Count = 5 

#Turn the robot left and right until it finds the line 
#or it has searched for long enough 

    while Seek_Count <= MaximumSeek_Count: 
        #Set the seek time 
        Seek_Time = Seek_Size * Seek_Count 
        #Start the motors turning in a direction 
        if Direction_ToMove: 
            print("Looking West") 
            West() 
        else: 
            print("Looking East") 
            East() 

        #Save the time it is now 
        Start_Time = time.time() 
        #While the robot is turning for SeekTime seconds, 
        #check o see whether the line detector is over black 
        while time.time()-Start_Time <= Seek_Time: 
            if IsOverBlack(): 
                StopMotors() 
                #Exit the SeekLine() function returning 
                #True- the line was found 
                return True 
         #The robot has not found the black line yet, so stop     
        StopMotors() 
         #Increase the seek count 
        Seek_Count += 1 
         #Change Direction 
        Direction_ToMove = not Direction_ToMove 
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

 
        #Pop current off open list, add to closed list 
        ListOpen.pop(CurrentIndex) 
        ListClosed.apend(CurrentNode) 

 

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

 

 

 
