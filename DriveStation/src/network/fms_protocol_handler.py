# src/network/fms_protocol_handler.py

import socket

class FMSProtocolHandler:
    def __init__(self):
        self.is_connected = False
        self.fms_socket = None

    def connect_to_fms(self, fms_ip, fms_port):
        try:
            self.fms_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.fms_socket.connect((fms_ip, fms_port))
            self.is_connected = True
            print(f"Connected to FMS at {fms_ip}:{fms_port}")
        except ConnectionError as e:
            print(f"Error connecting to FMS: {e}")

    def disconnect_from_fms(self):
        if self.is_connected:
            self.fms_socket.close()
            self.is_connected = False
            print("Disconnected from FMS")

    def send_data_to_fms(self, data):
        if self.is_connected:
            try:
                self.fms_socket.sendall(data.encode())
                print(f"Sent data to FMS: {data}")
            except socket.error as e:
                print(f"Error sending data to FMS: {e}")

    def receive_data_from_fms(self):
        if self.is_connected:
            try:
                received_data = self.fms_socket.recv(1024).decode()
                print(f"Received data from FMS: {received_data}")
                return received_data
            except socket.error as e:
                print(f"Error receiving data from FMS: {e}")

    def is_fms_connected(self):
        return self.is_connected
