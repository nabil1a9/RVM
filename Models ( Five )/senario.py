import RPi.GPIO as GPIO
import time
import subprocess

output_file = "test.jpg"
capture_time = "4000"

# build libcamera-jpeg command
cmd = ["libcamera-jpeg", "-o", output_file, "-t", capture_time]

# set GPIO pin numbers
TRIG_PIN = 23
ECHO_PIN = 24

# setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# function to measure distance
def measure_distance():
    # send ultrasonic signal
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    
    # receive ultrasonic echo
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()
    
    # calculate distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance

# continuously measure distance
while True:
    dist = measure_distance()
    print("Distance: {} cm".format(dist))
    if(dist<15):
        subprocess.run(cmd)
    time.sleep(1)
