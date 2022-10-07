import RPi.GPIO as GPIO
import time

led = 40
echo = 33
trigger = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distance():
	GPIO.output(trigger, True)
	time.sleep(0.00001)
	GPIO.output(trigger, False)
	
	startTime = time.time()
	stopTIme = time.time()
	
	while GPIO.input(echo) == 0:
		startTime = time.time()
	while GPIO.input(echo) == 1:
		stopTime = time.time()
	
	return ((stopTime - startTime) * 34300) / 2
	
pwm = GPIO.PWM(led, 100)
pwm.start(100)

if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print("Measured distance = %.1f cm" % dist)
			dc = 100
			if dist >= 30:
				dc = 0.1
				print("Duty cycle: 0")
			else:
				dc = ((30 - dist) / 30) * 100
				print("Duty cycle: %.1f" % dc)

			pwm.ChangeDutyCycle(dc)
			time.sleep(0.1)
	except KeyboardInterrupt:
		print("stop")
		pwm.stop()
		GPIO.cleanup()