import RPi.GPIO as GPIO
import time

pinServo = 10
DutyCycle = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinServo, GPIO.OUT)

pwmServo = GPIO.PWM(pinServo, 50)
pwmServo.start(DutyCycle)

try:
    while True:
        DutyCycle = float(input("Enter Duty Cycle(Left = 5 to Right = 10):"))
        pwmServo.ChangeDutyCycle(DutyCycle)

except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
    
