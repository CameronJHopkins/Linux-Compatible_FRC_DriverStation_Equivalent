# input/device_input_manager.py

from .joystick_handler import JoystickHandler
from .bluetooth_handler import BluetoothHandler

class DeviceInputManager:
    def __init__(self):
        self.joystick_handler = JoystickHandler()
        self.bluetooth_handler = BluetoothHandler()

    def get_joystick_axes(self, joystick_id):
        return self.joystick_handler.get_axes(joystick_id)

    def get_joystick_buttons(self, joystick_id):
        return self.joystick_handler.get_buttons(joystick_id)

    def get_joystick_hat(self, joystick_id):
        return self.joystick_handler.get_hat(joystick_id)

    def receive_bluetooth_data(self):
        return self.bluetooth_handler.receive_data()

    def is_bluetooth_connected(self):
        return self.bluetooth_handler.is_connected()

    def quit(self):
        self.joystick_handler.quit()
        self.bluetooth_handler.quit()

    # Additional methods as needed
