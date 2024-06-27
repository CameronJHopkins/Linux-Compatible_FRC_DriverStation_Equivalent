import bluetooth # type: ignore

class BluetoothHandler:
    def __init__(self):
        self.server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.client_socket = None
        self.connected = False

    def start_server(self):
        port = 1  # RFCOMM port for Bluetooth
        self.server_socket.bind(("", port))
        self.server_socket.listen(1)

        print("Waiting for Bluetooth connection...")
        self.client_socket, client_info = self.server_socket.accept()
        self.connected = True
        print(f"Connected to {client_info}")

    def receive_data(self):
        if self.connected:
            try:
                data = self.client_socket.recv(1024).decode().strip()
                return data
            except bluetooth.btcommon.BluetoothError as e:
                print(f"Bluetooth connection error: {e}")
                self.connected = False
                self.client_socket.close()
                return None
        return None

    def stop_server(self):
        self.server_socket.close()
        if self.client_socket:
            self.client_socket.close()
        self.connected = False

    def is_connected(self):
        return self.connected

    def quit(self):
        self.stop_server()
