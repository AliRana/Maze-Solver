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

StopMotors()
import sys, termios, tty, os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

PIN_LED = 25
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.output(PIN_LED, 0)
button_delay = 0.2

for x in range(0,3):
    GPIO.output(PIN_LED, 1)
    time.sleep(0.25)
    GPIO.output(PIN_LED, 0)
    time.sleep(0.25)

while True:
    char = getch()

    if(char == "q"):
       StopMotors()
       exit(0)

    if (char == "a"):
        print("Left pressed")
        Left()
        time.sleep(button_delay)

    if (char == "d"):
        print("Right pressed")
        Right()
        time.sleep(button_delay)

    elif (char == "w"):
        print("Up pressed")
        Forwards()
        time.sleep(button_delay)

    elif (char == "s"):
        print("Down pressed")
        Backwards()
        time.sleep(button_delay)

    StopMotors()
