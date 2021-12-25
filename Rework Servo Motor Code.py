import RPi.GPIO as GPIO
import time

MIN_DUTY = 3
MAX_DUTY = 11
CENTRE = MIN_DUTY +(MAX_DUTY - MIN_DUTY)/2

pinServo = 10
DutyCycle = CENTRE

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinServo, GPIO.OUT)

pwmServo = GPIO.PWM(pinServo, 50)
pwmServo.start(DutyCycle)

try:
    while True:
        pwmServo.ChangeDutyCycle(MIN_DUTY)
        time.sleep(1)
        pwmServo.ChangeDutyCycle(CENTRE)
        time.sleep(1)
        pwmServo.ChangeDutyCycle(MAX_DUTY)
        time.sleep(1)
        pwmServo.ChangeDutyCycle(CENTRE)
        time.sleep(1)


except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    pwmServo.ChangeDutyCycle(CENTRE)
    time.sleep(0.5)
    GPIO.cleanup()
        
