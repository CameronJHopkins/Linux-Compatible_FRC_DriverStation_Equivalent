# src/network/network_manager.py

from .fms_protocol_handler import FMSProtocolHandler
from .robot_communicator import RobotCommunicator

class NetworkManager:
    def __init__(self):
        self.fms_protocol_handler = FMSProtocolHandler()
        self.robot_communicator = RobotCommunicator()

    def connect_to_fms(self, fms_ip, fms_port):
        self.fms_protocol_handler.connect_to_fms(fms_ip, fms_port)

    def disconnect_from_fms(self):
        self.fms_protocol_handler.disconnect_from_fms()

    def send_data_to_fms(self, data):
        self.fms_protocol_handler.send_data_to_fms(data)

    def receive_data_from_fms(self):
        return self.fms_protocol_handler.receive_data_from_fms()

    def send_data_to_robot(self, data):
        self.robot_communicator.send_data(data)

    def receive_data_from_robot(self):
        return self.robot_communicator.receive_data()

    def is_fms_connected(self):
        return self.fms_protocol_handler.is_fms_connected()

    def is_robot_connected(self):
        return self.robot_communicator.is_connected()
