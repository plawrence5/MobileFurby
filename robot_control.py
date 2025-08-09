import os
from evdev import InputDevice, categorize, ecodes
from adafruit_motorkit import MotorKit

# CHANGE THIS to match your keyboard device
DEVICE_PATH = '/dev/input/by-id/usb-Logitech_USB_Receiver-event-kbd'

# Set up keyboard device
device = InputDevice(DEVICE_PATH)

# Set up motor hat
kit = MotorKit()

def move_forward():
    print("Moving forward")
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = -0.45

def move_backward():
    print("Moving backward")
    kit.motor1.throttle = -0.4
    kit.motor2.throttle = 0.35

def turn_left():
    print("Turning right")
    kit.motor1.throttle = -0.0
    kit.motor2.throttle = -0.4

def turn_right():
    print("Turning left")
    kit.motor1.throttle = 0.4
    kit.motor2.throttle = 0.0

def furby_on():
    print("Furby on")
    kit.motor3.throttle = 0.8

def furby_off():
    print("Furby off")
    kit.motor3.throttle = 0.0

def stop_motors():
    print("Stopping")
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

def shutdown_pi():
    print("Shutting down Pi...")
    stop_motors()
    os.system("sudo shutdown -h now")

# Event loop
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        keycode = key_event.keycode

        if key_event.keystate == key_event.key_down:

            if keycode == 'KEY_W':
                move_forward()
            elif keycode == 'KEY_S':
                move_backward()
            elif keycode == 'KEY_A':
                turn_left()
            elif keycode == 'KEY_D':
                turn_right()
            elif keycode == 'KEY_F':
                furby_on()
            elif keycode == 'KEY_G':
                furby_off()
            elif keycode == 'KEY_X':
                stop_motors()
            elif keycode == 'KEY_Q':
                shutdown_pi()

        if key_event.keystate == key_event.key_up:
            
            stop_motors()
