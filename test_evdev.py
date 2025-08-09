from evdev import InputDevice, list_devices

# List all input devices
devices = [InputDevice(path) for path in list_devices()]
for dev in devices:
    print(f"{dev.path}: {dev.name}")
