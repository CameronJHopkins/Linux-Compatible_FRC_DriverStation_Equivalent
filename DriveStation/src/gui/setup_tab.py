from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QFormLayout

class SetupTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.init_setup()

        self.setLayout(self.layout)

    def init_setup(self):
        # Group Box for team setup
        self.team_group_box = QGroupBox("Team Setup")
        team_layout = QFormLayout()
        
        self.team_number_input = QLineEdit(self)
        team_layout.addRow("Team Number:", self.team_number_input)

        self.robot_ip_input = QLineEdit(self)
        team_layout.addRow("Robot IP Address:", self.robot_ip_input)

        self.save_button = QPushButton("Save Configuration", self)
        self.save_button.clicked.connect(self.save_configuration)
        team_layout.addWidget(self.save_button)

        self.team_group_box.setLayout(team_layout)
        self.layout.addWidget(self.team_group_box)

    def save_configuration(self):
        team_number = self.team_number_input.text()
        robot_ip = self.robot_ip_input.text()
        # Save the team number and robot IP to a configuration file or use as needed
        print(f"Team number {team_number} and Robot IP {robot_ip} saved!")
