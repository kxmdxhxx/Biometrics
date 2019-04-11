import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)



while True: # Infinite Loop for blink
	GPIO.setup(3, GPIO.OUT)  # Blue LED
	GPIO.output(3, GPIO.HIGH) # Turn on Blue LED

	time.sleep(2) # Sleep for 2 second

	GPIO.output(3, GPIO.LOW) # Turn off Blue LED

	GPIO.setup(5, GPIO.OUT)  # Yellow LED
	GPIO.output(5, GPIO.HIGH) # Turn on Yellow LED

	time.sleep(2) # Sleep for 2 second

	GPIO.output(5, GPIO.LOW) # Turn off Yellow LED

	GPIO.setup(7, GPIO.OUT)  # White LED
	GPIO.output(7, GPIO.HIGH) # Turn on White LED

	time.sleep(2) # Sleep for 2 second

	GPIO.output(7, GPIO.LOW) # Turn off White LED

	time.sleep(1) # Sleep for 1 second

GPIO.cleanup()
