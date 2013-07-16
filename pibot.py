# Import the webiopi 
import webiopi

# Retrieve the GPIO lib
GPIO = webiopi.GPIO



#motor GPIOs Definitions
L=17  # GPIO 17 LEFT
R=18 # GPIO 18 RIGHT
F=22 # GPIO 22 FORWARD
B=23 # GPIO 23 REVERSE
S=25 # GPIO 25 STOP

####-Movement of Motors (both right and left)

def left_stop():
    GPIO.output(L, GPIO.LOW)
   
def left_start():
    GPIO.output(L, GPIO.HIGH)

def right_stop():
    GPIO.output(R, GPIO.LOW)

def right_start():
    GPIO.output(R, GPIO.HIGH)

def for_stop():
    GPIO.output(F, GPIO.LOW)

def for_start():
    GPIO.output(F, GPIO.HIGH)

def back_stop():
    GPIO.output(B, GPIO.LOW)

def back_start():
    GPIO.output(B, GPIO.HIGH)	

def stop_on():
    GPIO.output(S, GPIO.HIGH)

def stop_off():
    GPIO.output(S, GPIO.LOW)

## ----- Define Macros
def forward():
    for_start()
    left_stop()
    right_stop()
    back_stop()
    stop_off()

def reverse():
	left_stop()
	right_stop()
	for_stop()
	back_start()
	stop_off()

def left():
	left_start()
	right_stop()
	for_stop()
	back_stop()
	stop_off()

def right():
	left_stop()
	right_start()
	for_stop()
	back_stop()
	stop_off()
def stop():
    left_stop()
    right_stop()
    for_stop()
    back_stop()
    stop_on()	    


# Setup GPIOs
GPIO.setFunction(L, GPIO.OUT)
GPIO.setFunction(R, GPIO.OUT)
GPIO.setFunction(F, GPIO.OUT)

GPIO.setFunction(B, GPIO.OUT)
GPIO.setFunction(S, GPIO.OUT)
stop()

##--- The server

# Instantiate the server on the port 8000 (it can be changed), it starts immediately in its own thread
server = webiopi.Server(port=8000, login="pibot", password="pibot")

# Register the macros so you can call it with Javascript and/or REST API

server.addMacro(forward)
server.addMacro(reverse)
server.addMacro(left)
server.addMacro(right)
server.addMacro(stop)


# Run our loop until CTRL-C is pressed or SIGTERM received
webiopi.runLoop()


# Stop the server
server.stop()

# Reset GPIO functions
GPIO.setFunction(L, GPIO.IN)
GPIO.setFunction(R, GPIO.IN)
GPIO.setFunction(F, GPIO.IN)

GPIO.setFunction(B, GPIO.IN)
GPIO.setFunction(S, GPIO.IN)

