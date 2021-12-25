import RPi.GPIO as GPIO
import time

##set the GPIO Pin mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

##Set variables for the GPIO Motor,Line Follower and Distance Detection pins
pinMotorAON = 17
pinMotorAForwards = 27
pinMotorABackwards = 22

pinMotorBON = 24
pinMotorBForwards = 25
pinMotorBBackwards = 23

pinLineFollower = 14
pinTrigger = 3
pinEcho = 4

##How many times to turn the pin on or off each second
Frequency = 20

##How long the pin stays on each cycle, as a percent
DutyCycleA = 75
DutyCycleB = 75

##Setting the Duty cycle to 0 means the motors will not turn
Stop = 0



##Set the GPIO Pin mode to be output
GPIO.setup(pinMotorAON, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBON, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinTrigger, GPIO.OUT)

##Set pins as a output or input
GPIO.setup(pinEcho, GPIO.IN)
GPIO.setup(pinLineFollower, GPIO.IN)

##Distance variables
HowNear = 15.0
ReverseTime = 0.5
TurnTime = 0.75

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

##Turn all motors off
def StopMotors():
    pwmMotorAON.ChangeDutyCycle(Stop)
    pwmMotorBON.ChangeDutyCycle(Stop)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

##Turn all motors on
def Forwards():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving Forwards")

##Turn both motors backwards
def Backwards():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    print("Moving Backwards")

##Turn Right
def Right():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    print("Moving Right")

##Turn Left
def Left():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving Left")
    
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
            print("Hold on there! You're too closefor me to see")
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
    print("Backwards")
    Backwards()
    time.sleep(ReverseTime)
    StopMotors()

    print("Right")
    Right()
    time.sleep(TurnTime)
    StopMotors()

##This is the code to control the robot
try:
    GPIO.output(pinTrigger, False)
    time.sleep(0.1)
    
    while True:
        Forwards()
        time.sleep(0.1)
        if IsNearObstacle(HowNear):
            StopMotors()
            AvoidObstacle()
            
##If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()

