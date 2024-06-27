# gui/dashboard_tab.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QGridLayout
from PyQt5.QtCore import Qt

class DashboardTab(QWidget):
    def __init__(self, device_input_manager):
        super().__init__()
        self.device_input_manager = device_input_manager
        self.layout = QVBoxLayout()

        self.battery_voltage_labels = []
        self.mode_labels = []
        self.gyro_labels = []
        self.accelerometer_labels = []
        self.bluetooth_status_label = QLabel("Bluetooth Status: Not Connected")

        self.init_dashboard()

        self.setLayout(self.layout)

        # Connect to device input manager signals
        self.device_input_manager.joystick_handler.joystick_data_updated.connect(self.update_joystick_display)
        self.device_input_manager.bluetooth_handler.bluetooth_data_received.connect(self.update_bluetooth_data)
        self.device_input_manager.bluetooth_handler.bluetooth_connected.connect(self.update_bluetooth_status)

    def init_dashboard(self):
        self.status_group_boxes = []
        self.sensor_group_boxes = []

        # Create status and sensor group boxes for each joystick
        for i in range(2):  # Assuming support for up to 2 joysticks
            status_group_box = QGroupBox(f"Joystick {i + 1} Status")
            status_layout = QGridLayout()
            status_layout.addWidget(QLabel("Battery Voltage:"), 0, 0)
            self.battery_voltage_labels.append(QLabel("N/A"))
            status_layout.addWidget(self.battery_voltage_labels[i], 0, 1)

            status_layout.addWidget(QLabel("Mode:"), 1, 0)
            self.mode_labels.append(QLabel("N/A"))
            status_layout.addWidget(self.mode_labels[i], 1, 1)

            status_group_box.setLayout(status_layout)
            self.status_group_boxes.append(status_group_box)
            self.layout.addWidget(status_group_box)

            sensor_group_box = QGroupBox(f"Joystick {i + 1} Sensor Data")
            sensor_layout = QGridLayout()
            sensor_layout.addWidget(QLabel("Gyro:"), 0, 0)
            self.gyro_labels.append(QLabel("N/A"))
            sensor_layout.addWidget(self.gyro_labels[i], 0, 1)

            sensor_layout.addWidget(QLabel("Accelerometer:"), 1, 0)
            self.accelerometer_labels.append(QLabel("N/A"))
            sensor_layout.addWidget(self.accelerometer_labels[i], 1, 1)

            sensor_group_box.setLayout(sensor_layout)
            self.sensor_group_boxes.append(sensor_group_box)
            self.layout.addWidget(sensor_group_box)

        # Add Bluetooth status label
        self.layout.addWidget(self.bluetooth_status_label)

        # Group Box for displaying camera feed (if needed)
        camera_group_box = QGroupBox("Camera Feed")
        camera_layout = QVBoxLayout()
        camera_layout.addWidget(QLabel("Camera feed would go here"))  # Placeholder for actual camera feed
        camera_group_box.setLayout(camera_layout)
        self.layout.addWidget(camera_group_box)

    def update_status(self, joystick_id, battery_voltage, mode):
        if 0 <= joystick_id < len(self.status_group_boxes):
            self.battery_voltage_labels[joystick_id].setText(f"{battery_voltage} V")
            self.mode_labels[joystick_id].setText(mode)

    def update_sensors(self, joystick_id, gyro, accelerometer):
        if 0 <= joystick_id < len(self.sensor_group_boxes):
            self.gyro_labels[joystick_id].setText(f"{gyro}°")
            self.accelerometer_labels[joystick_id].setText(f"{accelerometer} m/s²")

    def update_joystick_display(self, joystick_id, joystick_data):
        if 0 <= joystick_id < len(self.status_group_boxes):
            self.update_status(joystick_id, joystick_data['battery_voltage'], joystick_data['mode'])
            self.update_sensors(joystick_id, joystick_data['gyro'], joystick_data['accelerometer'])

    def update_bluetooth_status(self, connected):
        if connected:
            self.bluetooth_status_label.setText("Bluetooth Status: Connected")
        else:
            self.bluetooth_status_label.setText("Bluetooth Status: Not Connected")

    def update_bluetooth_data(self, data):
        # Assuming data is received as a dictionary or string
        self.camera_feed_label.setText(f"Bluetooth Data: {data}")
