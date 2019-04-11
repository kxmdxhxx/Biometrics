import time
import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)  # Switch Button
GPIO.setup(3, GPIO.OUT)  # Green LED
GPIO.setup(13, GPIO.OUT)  # Red LED

print ("Kim's Reaction time game!!") 

	
GPIO.output(3, GPIO.HIGH) # Turn on Green LED
GPIO.output(13, GPIO.HIGH) # Turn on Red LED

time.sleep(2) # Sleep for 2 second

GPIO.output(3, GPIO.LOW) # Turn off Green LED
GPIO.output(5, GPIO.LOW) # Turn off Red LED


print ("The green light will stay on for a random amount of time between 1 and 15 seconds")
print ("It will then swap to the red light")
print ("As soon as it changes hit the switch")
print ("We will start in 5 seconds. Get ready!!!!")
time.sleep(5) # Sleep for 5 second

	
GPIO.output(3, GPIO.HIGH) # Turn on Green LED

r = random.randint(1, 15) # Get the random integer r which is between 1 and 15
time.sleep(r) # Sleep for r second

GPIO.output(3, GPIO.LOW) # Turn off Green LED
GPIO.output(13, GPIO.HIGH) # Turn on Red LED

start = time.time() # Store time as start

try:
    while True:
        if(GPIO.input(12)==1): # if button is pressed
            end = time.time() # Store time as end
            print ("You pressed the button!!")
            elapsed = end - start # Get the time gap between start and end
            print ("and it took")
            print (round(elapsed, 2)) # Print reaction time rounded off to 2 decimals
            print ("Try to beat that next time!!")
            GPIO.output(3, GPIO.LOW) # Turn off Green LED
            GPIO.output(13, GPIO.LOW) # Turn off Red LED
            GPIO.cleanup()
            break # break the loop

        else:
            GPIO.output(3, GPIO.LOW) # Turn off Green LED
            GPIO.output(13, GPIO.HIGH) # Turn on Red LED
            

except KeyboardInterrupt:
    print ("Game Over")
