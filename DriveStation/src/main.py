# main.py

from gui.dashboard_tab import DashboardTab
from gui.controls_tab import ControlsTab
from input.device_input_manager import DeviceInputManager
from network.network_manager import NetworkManager

def main():
    # Initialize network manager
    network_manager = NetworkManager()

    # Initialize GUI components
    dashboard_tab = DashboardTab(network_manager)
    controls_tab = ControlsTab(network_manager)

    # Initialize device input manager (assuming it interacts with controls)
    device_input_manager = DeviceInputManager()

    # Example: Connecting to FMS and Robot
    fms_ip = '192.168.1.100'
    fms_port = 5000
    robot_ip = '192.168.1.101'
    robot_port = 6000

    network_manager.connect_to_fms(fms_ip, fms_port)
    network_manager.connect_to_robot(robot_ip, robot_port)

    # Example: Sending data from device input to robot
    device_input_data = device_input_manager.get_input_data()
    network_manager.send_data_to_robot(device_input_data)

    # Example: Receiving data from FMS and updating GUI
    fms_data = network_manager.receive_data_from_fms()
    dashboard_tab.update_fms_data(fms_data)

    # Example: Receiving data from robot and updating controls tab
    robot_data = network_manager.receive_data_from_robot()
    controls_tab.update_robot_data(robot_data)

    # Disconnect from FMS and Robot when done
    network_manager.disconnect_from_fms()
    network_manager.disconnect_from_robot()

if __name__ == "__main__":
    main()
