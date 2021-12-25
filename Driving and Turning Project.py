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

##set the GPIO Pin mode

GPIO.setup(pinMotorAON, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBON, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

def StopMotors():
    GPIO.output(pinMotorAON, 0)
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBON, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

def Forwards():
    GPIO.output(pinMotorAON, 1)
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorBON, 1)
    GPIO.output(pinMotorBForwards, 1)
    print("Moving Wheels forward")

def Backwards():
    GPIO.output(pinMotorAON, 1)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBON, 1)
    GPIO.output(pinMotorBBackwards, 1)
    print("Moving Backwards")

def Right():
    GPIO.output(pinMotorAON, 1)
    GPIO.output(pinMotorAForwards, 1)
    print("Turning Right")

def Left():
    GPIO.output(pinMotorBON, 1)
    GPIO.output(pinMotorBForwards, 1)
    print("Turning Left")

Forwards()
time.sleep(2)
StopMotors()

Left()
time.sleep(2)
StopMotors()

Right()
time.sleep(2)
StopMotors()

Backwards()
time.sleep(2)
StopMotors()

StopMotors()

GPIO.cleanup()



