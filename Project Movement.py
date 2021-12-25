import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
## Turm all motors off
GPIO.output(17, 0)
GPIO.output(27, 0)
GPIO.output(22, 0)
GPIO.output(23, 0)
GPIO.output(24, 0)
GPIO.output(25, 0)

##Go forwards
GPIO.output(17,1)
GPIO.output(27,1)
GPIO.output(24,1)
GPIO.output(25,1)
print("Moving Wheels")

time.sleep(4)

GPIO.output(17, 0)
GPIO.output(27, 0)
GPIO.output(22, 0)
GPIO.output(23, 0)
GPIO.output(24, 0)
GPIO.output(25, 0)


GPIO.output(17,1)
GPIO.output(27,1)
print("Turn Right")

##GPIO.output(17,1)
##GPIO.output(27, 1)
##GPIO.output(22,1)
##GPIO 22 is negative
##GPIO 27 is positive
##GPIO 17 is power for left side

##GPIO.output(24,1)
##GPIO.output(25,1)
##GPIO.output(23,1)
##GPIO 25 is positive
##GPIO 23 is negative
##GPIO 24 is power for right side

time.sleep(5)

GPIO.output(17, 0)
GPIO.output(27, 0)
GPIO.output(22, 0)
GPIO.output(23, 0)
GPIO.output(24, 0)
GPIO.output(25, 0)

GPIO.output(24,1)
GPIO.output(25,1)
print("Turn Left")

time.sleep(4)
GPIO.cleanup()
