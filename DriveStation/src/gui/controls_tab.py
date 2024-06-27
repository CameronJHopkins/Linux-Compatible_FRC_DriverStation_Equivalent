# gui/controls_tab.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QPushButton
from PyQt5.QtCore import Qt

class ControlsTab(QWidget):
    def __init__(self, device_input_manager):
        super().__init__()
        self.device_input_manager = device_input_manager
        self.layout = QVBoxLayout()

        self.joystick_group_boxes = []
        self.bluetooth_data_label = QLabel("Bluetooth Data: ")

        self.init_controls()

        self.setLayout(self.layout)

        # Connect to device input manager signals
        self.device_input_manager.joystick_handler.joystick_data_updated.connect(self.update_joystick_display)
        self.device_input_manager.bluetooth_handler.bluetooth_data_received.connect(self.update_bluetooth_data)
        self.device_input_manager.bluetooth_handler.bluetooth_connected.connect(self.update_bluetooth_status)

    def init_controls(self):
        # Create joystick control group boxes for each joystick
        for i in range(2):  # Assuming support for up to 2 joysticks
            joystick_group_box = QGroupBox(f"Joystick {i + 1} Controls")
            joystick_layout = QVBoxLayout()
            self.joystick1_labels.append(QLabel(f"Joystick {i + 1}: X: 0.0, Y: 0.0"))
            joystick_layout.addWidget(self.joystick1_labels[i])
            self.joystick2_labels.append(QLabel(f"Joystick {i + 1}: X: 0.0, Y: 0.0"))
            joystick_layout.addWidget(self.joystick2_labels[i])

            joystick_group_box.setLayout(joystick_layout)
            self.joystick_group_boxes.append(joystick_group_box)
            self.layout.addWidget(joystick_group_box)

        # Add Bluetooth data display label
        self.layout.addWidget(self.bluetooth_data_label)

        # Group Box for robot controls (if needed)
        robot_control_group_box = QGroupBox("Robot Controls")
        robot_control_layout = QVBoxLayout()
        
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_robot)
        robot_control_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_robot)
        robot_control_layout.addWidget(self.stop_button)

        self.enable_button = QPushButton("Enable")
        self.enable_button.clicked.connect(self.enable_robot)
        robot_control_layout.addWidget(self.enable_button)

        self.disable_button = QPushButton("Disable")
        self.disable_button.clicked.connect(self.disable_robot)
        robot_control_layout.addWidget(self.disable_button)

        robot_control_group_box.setLayout(robot_control_layout)
        self.layout.addWidget(robot_control_group_box)

    def update_joystick_display(self, joystick_id, joystick_data):
        if 0 <= joystick_id < len(self.joystick_group_boxes):
            self.joystick1_labels[joystick_id].setText(f"Joystick {joystick_id + 1}: X: {joystick_data['axis1'][0]}, Y: {joystick_data['axis1'][1]}")
            self.joystick2_labels[joystick_id].setText(f"Joystick {joystick_id + 1}: X: {joystick_data['axis2'][0]}, Y: {joystick_data['axis2'][1]}")

    def update_bluetooth_status(self, connected):
        if connected:
            self.bluetooth_status_label.setText("Bluetooth Status: Connected")
        else:
            self.bluetooth_status_label.setText("Bluetooth Status: Not Connected")

    def update_bluetooth_data(self, data):
        # Display received Bluetooth data
        self.bluetooth_data_label.setText(f"Bluetooth Data: {data}")

    def start_robot(self):
        # Placeholder for start robot functionality
        print("Starting robot...")
        # Simulate starting the robot
        # self.update_status("12.0", "Teleop")

    def stop_robot(self):
        # Placeholder for stop robot functionality
        print("Stopping robot...")
        # Simulate stopping the robot
        # self.update_status("0.0", "Disabled")

    def enable_robot(self):
        # Placeholder for enable robot functionality
        print("Enabling robot...")
        # Simulate enabling the robot
        # self.update_status("12.0", "Teleop")

    def disable_robot(self):
        # Placeholder for disable robot functionality
        print("Disabling robot...")
        # Simulate disabling the robot
        # self.update_status("0.0", "Disabled")
