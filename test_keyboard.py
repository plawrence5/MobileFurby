from evdev import InputDevice, categorize, ecodes

device = InputDevice('/dev/input/by-id/usb-Logitech_USB_Receiver-event-kbd')

print("Listening for key presses... (Ctrl+C to stop)")

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        if key_event.keystate == key_event.key_down:
            print(f"Key pressed: {key_event.keycode}")
