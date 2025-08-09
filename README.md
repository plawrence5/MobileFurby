# MOBILE FURBY
#### Video Demo:  https://youtu.be/mjt7oKEM6tc

[![Watch the video](https://img.youtube.com/vi/mjt7oKEM6tc/maxresdefault.jpg)](https://youtu.be/mjt7oKEM6tc)

#### Description:

Mobile Furby is a two wheeled motor controlled car platform with a skinned Furby mounted on top. The movement of the car and the the furby are controlled by a keyboard that connects to the Furby car via bluetooth.

## Hardware Components

- Skinned Furby
- Raspberry Pi 4B and case
- SD Card
- Motor Hat for Raspberry Pi    https://www.adafruit.com/product/2348
- Adjustable Output BEC    https://www.amazon.com/FainWan-Products-3amp-6-0-25-2v-Adjustable/dp/B09L6Z67Q8
- Robot Chassis:   https://www.adafruit.com/product/3244
- Top Metal Plate for Mini Robot  https://www.adafruit.com/product/2944
- Battery Pack with on / off switch for 2 18650 batteries
- 18650 Batteries (2)
- 2 x 20 (40 Pin) Extra Tall Stacking Header
- 6 inch male to male breadboard jumper cables (2 red, 2 black)
- 4 inch male to male breadboard jumper cables (1 red, 1 black)
- M2.5 20mm risers with screw and bolt for each (5)
- Logitech MX Keys Mini Wireless Keyboard
- Logitech Bolt USB Receiver

## Software Packages

- evdev: Used to capture keystrokes from keyboard.
- adafruit_motorkit: CircuitPython helper library for the DC Motor Hat.
- os: Python's built in os module which provides a way of interacting with the Raspberry Pi's operating system.

## Project Files

### robot.service

**Mobile Furby** is designed to be fully operational as soon as it's powered on. To make this possible, the Raspberry Pi is configured to run the main control script (robot_control.py) as a **background service**. This ensures the robot starts automatically at boot without requiring manual intervention.

**Key details**

-ExecStart points to the robot_control.py script, which handles WASD-based robot control.\
-Restart=always ensures the script is automatically restarted if it crashes or exits unexpectedly.\
-User=root runs the script with elevated privileges, which may be needed for hardware access.\
-After=network.target delays startup until networking is initialized, if needed by the script.\

**What is a Background Service?**

A background service is a program that runs continuously in the background without direct user interaction. On Linux systems like Raspberry Pi OS, these services are typically managed by systemd, the system and service manager.

In this project, robot_control.py is run as a systemd background service to ensure it launches on boot and stays running. This allows the robot to be ready as soon as it is powered on and to recover automatically from unexpected interruptions.y.

🔧 **Setup Instructions**

To enable the background service for robot_control.py on a Raspberry Pi:

1. **Edit the Service File**\
Update the ExecStart line in robot.service to point to the full path of your script. For example:\
ExecStart=/usr/bin/python3 /home/pi/robot_project/robot_control.py

2. **Copy the service file to the systemd directory**\
sudo cp robot.service /etc/systemd/system/

3. **Reload systemd to recognize the new service**\
sudo systemctl daemon-reload

4. **Enable the service to run on boot**\
sudo systemctl enable robot.service

5. **Start the service immediately**\
Start the service immediately**

6. **(Optional) Check the service status**\
sudo systemctl status robot.service

Once enabled, robot_control.py will launch automatically every time the Raspberry Pi boots up.

### robot_control.py

The robot_control.py script enables real-time keyboard control of Mobile Furby. It uses the evdev library to read keyboard input and the Adafruit MotorKit library to drive motors via the Adafruit Motor HAT that is attached to the Raspberry Pi.

🚀 What It Does
- Accepts keyboard input from a specified USB keyboard device.
- Controls two drive motors to move the robot forward, backward, and turn left or right.
- Toggles a third motor (e.g., Furby mechanism) on and off.
- Provides a quick shutdown command for the Raspberry Pi.
- Runs as a continuous loop, making the robot responsive to user commands in real time.

🛠 How It Works
- The script reads keystrokes from a the keyboard.

- Key bindings:
    - W: Move forward
    - S: Move backward
    - A: Turn left
    - D: Turn right
    - F: Turn Furby motor on
    - G: Turn Furby motor off
    - X: Stop all movement
    - Q: Shutdown the Raspberry Pi

- Motor throttles are adjusted individually to account for mechanical differences between the motors, ensuring straight and consistent motion.
- Runs in the foreground and continuously listens for key presses using evdev.
- The line of code os.system("sudo shutdown now") is executed when the user enters Q on the keyboard.  This alows for a graceful shutdown of the Mobile Furby and an alternative to simply turning of the power source.

### test_evdev.py

This script will display all the input devices that evdev is listening for and the path for each device.  It is necessary to run this script to get the path to the usb bluetooth receiver that is paired with the keyboard that will be used to control Mobile Furby.  The path in the following line of code from robot_control.py shows the path that was derived using this script.

DEVICE_PATH = '/dev/input/by-id/usb-Logitech_USB_Receiver-event-kbd'

### test_keyboard.py

This script is used to confirm that the device path selected after executing test_evdev.py is the correct one.  The script text_evdev.py will display a number of inputs and it is not always clear which of the devices listed is in fact the keyboard that will be used to control Mobile Furby.  This script listens to the path that is being tested so that the user can depress keys on the control keyboard and confirm that evdev is receiving the keystrokes. If not the user can go back to test_evdev.py and find another path to test until the correct path is identified.

## Powering Mobile Furby

The project is powered by a battery back that provides 7V of power (2 3.5V  18650 batteries).  This voltage is within the acceptable range for the motors but it too high to power the the Raspberry Pi, which requires 5V.  To work around this the battery output is split with half going directly to Motor Hat to control the motors with the full 7V, and the other half sent to a FainWan RC Products 3amp - 6.0-25.2v Input / 5v/6v Adjustable Output BEC set to output 5V.  The 5V output of the BEC is then connected to the Raspberry Pi to power it.

## Collaboration:

This project was completed in collaboration with Lily Lawrence, a fellow student in CS50.
We worked together on all parts of the project, including:

- Planning and Project Architecture
- Configuring the Raspberry Pi to support the project
- Writing the code to control the Mobile Furby

Each of us is submitting the same codebase and finished Mobile Furby individually, as per the course policy.
