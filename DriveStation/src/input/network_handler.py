import socket

class NetworkHandler:
    def __init__(self, robot_ip, port):
        self.robot_ip = robot_ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_robot(self):
        try:
            self.socket.connect((self.robot_ip, self.port))
            print(f"Connected to robot at {self.robot_ip}:{self.port}")
            return True
        except Exception as e:
            print(f"Failed to connect to robot: {e}")
            return False

    def send_data(self, data):
        try:
            self.socket.sendall(data.encode())
            print(f"Sent data to robot: {data}")
            return True
        except Exception as e:
            print(f"Failed to send data to robot: {e}")
            return False

    def receive_data(self):
        try:
            data = self.socket.recv(1024)
            print(f"Received data from robot: {data.decode()}")
            return data.decode()
        except Exception as e:
            print(f"Failed to receive data from robot: {e}")
            return None

    def disconnect(self):
        self.socket.close()
        print("Disconnected from robot")
