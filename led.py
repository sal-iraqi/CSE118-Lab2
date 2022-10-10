import RPi.GPIO as GPIO
import time

led = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led,100)

GPIO.output(led,GPIO.HIGH)
pwm.start(100)
print("100%")
time.sleep(5)


pwm.ChangeDutyCycle(75)
print("75%")
time.sleep(5)

pwm.ChangeDutyCycle(50)
print("50%")
time.sleep(5)


pwm.ChangeDutyCycle(25)
print("25%")
time.sleep(5)

pwm.stop()

GPIO.cleanup()
