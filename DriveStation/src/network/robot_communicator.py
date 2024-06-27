# src/network/robot_communicator.py

import socket

class RobotCommunicator:
    def __init__(self):
        self.is_connected = False
        self.robot_socket = None

    def connect_to_robot(self, robot_ip, robot_port):
        try:
            self.robot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.robot_socket.connect((robot_ip, robot_port))
            self.is_connected = True
            print(f"Connected to robot at {robot_ip}:{robot_port}")
        except ConnectionError as e:
            print(f"Error connecting to robot: {e}")

    def disconnect_from_robot(self):
        if self.is_connected:
            self.robot_socket.close()
            self.is_connected = False
            print("Disconnected from robot")

    def send_data(self, data):
        if self.is_connected:
            try:
                self.robot_socket.sendall(data.encode())
                print(f"Sent data to robot: {data}")
            except socket.error as e:
                print(f"Error sending data to robot: {e}")

    def receive_data(self):
        if self.is_connected:
            try:
                received_data = self.robot_socket.recv(1024).decode()
                print(f"Received data from robot: {received_data}")
                return received_data
            except socket.error as e:
                print(f"Error receiving data from robot: {e}")

    def is_connected(self):
        return self.is_connected
