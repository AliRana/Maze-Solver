import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinMotorAON = 17
pinMotorAForwards = 27
pinMotorABackwards = 22

pinMotorBON = 24
pinMotorBForwards = 25
pinMotorBBackwards = 23

pinLineFollower = 14

Frequency = 20
DutyCycleA = 75
DutyCycleB = 75
Stop = 0

##set the GPIO Pin mode

GPIO.setup(pinLineFollower, GPIO.IN)
GPIO.setup(pinMotorAON, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBON, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

pwmMotorAON = GPIO.PWM(pinMotorAON, Frequency)
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBON = GPIO.PWM(pinMotorBON, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

pwmMotorAON.start(Stop)
pwmMotorBON.start(Stop)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

def StopMotors():
    pwmMotorAON.ChangeDutyCycle(Stop)
    pwmMotorBON.ChangeDutyCycle(Stop)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

def Forwards():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving Forwards")
    
def Backwards():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    print("Moving Backwards")

def Right():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    print("Moving Right")

def Left():
    pwmMotorAON.ChangeDutyCycle(DutyCycleA)
    pwmMotorBON.ChangeDutyCycle(DutyCycleB)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
    print("Moving Left")

def IsOverBlack():
    if GPIO.input(pinLineFollower) == 0:
        return True
    else:
        return False
def SeekLine():
    print("Seeking the Line")
##    The direction the robot will turn - True = Left
    Direction = True

    SeekSize = 0.25
    SeekCount = 1
    MaxSeekCount = 5

    while SeekCount <= MaxSeekCount:
        SeekTime = SeekSize * SeekCount
        if Direction:
            print("Looking Left")
            Left()
        else:
            print("Looking Right")
            Right()

        StartTime = time.time()
        while time.time()-StartTime <= SeekTime:
            if IsOverBlack():
                StopMotors()
                return True
        StopMotors()
        SeekCount += 1
        Direction = not Direction
    return False

try:
    # Repeat the next indented block forever
    print("Following the line")
    while True:
        # If the sensor is low (=0), it's above the black line
        if IsOverBlack():
            Forwards()
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
