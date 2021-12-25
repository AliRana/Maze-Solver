# CamJam EduKit 3 - Robotics
# Worksheet 5 - Line Detection

import RPi.GPIO as GPIO # Import the GPIO Libary
import time # Import the Time Libary

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO pins
pinLineFollower = 14

pinMotorAON = 17
pinMotorAForwards = 27
pinMotorABackwards = 22

pinMotorBON = 24
pinMotorBForwards = 25
pinMotorBBackwards = 23

##How many times to turn the pins on or off each second
Frequency = 20
##How long the pin stays on each cyle, as a percent
DutyCycleA = 75
DutyCycleB = 75
##Setting the Duty Cycle to 0 means the motors will not turn
Stop = 0

##set the GPIO Pin mode
GPIO.setup(pinMotorAON, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBON, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set pin 14 as an input so its value can be read
GPIO.setup(pinLineFollower, GPIO.IN)

##Set the GPIO to software PWM at "Frequency" Hertz
pwmMotorAON = GPIO.PWM(pinMotorAON, Frequency)
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBON = GPIO.PWM(pinMotorBON, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

##Start the softare PWM with Duty Cycle of O (i.e not moving)
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

##Turn both motors Forwards
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

##Return True if the line detector is over the black line
def IsOverBlack():
    if GPIO.input(pinLineFollower) == 0:
        return True
    else:
        return False

##Search for the black line
def SeekLine():
    print("Seeking the Line")
##    The direction the robot will turn - True = Left
    Direction = True

##Turn for 0.25s
    SeekSize = 0.25
    
##A count of the times the robot has looked for the line
    SeekCount = 1
    
##The maximum time to seek for the line in one direction
    MaxSeekCount = 5

##Turn the robot left and right until it finds the line
##or it has searched for long enough
    while SeekCount <= MaxSeekCount:
##      Set the seek time
        SeekTime = SeekSize * SeekCount
##      Start the motors turning in a direction
        if Direction:
            print("Looking Left")
            Left()
        else:
            print("Looking Right")
            Right()

##      Save the time it is now
        StartTime = time.time()
##      While the robot is turning for SeekTime seconds,
##      check o see whether the line detector is over black
        while time.time()-StartTime <= SeekTime:
            if IsOverBlack():
                StopMotors()
##              Exit the SeekLine() function returning
##              True- the line was found
                return True
##      The robot has not found the black line yet, so stop    
        StopMotors()
##      Increase the seek count
        SeekCount += 1
##      Change Direction
        Direction = not Direction
##      The line wasn't found, so return false
    return False

try:
    # Repeat the next indented block forever
    print("Following the line")
    while True:
        # If the sensor is low (=0), it's above the black line
        if IsOverBlack():
            Forwards()
##      If not (else), print the following
        else:
            StopMotors()
            if SeekLine() == False:
                StopMotors()
                print("The robot has lost the line")
                exit()
            else:
                print("Following the line")
                
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()
