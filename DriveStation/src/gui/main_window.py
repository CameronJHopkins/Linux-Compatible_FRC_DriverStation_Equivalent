from PyQt5.QtWidgets import QMainWindow, QTabWidget
from gui.dashboard_tab import DashboardTab
from gui.controls_tab import ControlsTab
from gui.setup_tab import SetupTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FRC Driver Station')

        self.tabs = QTabWidget()
        self.tabs.addTab(DashboardTab(), "Dashboard")
        self.tabs.addTab(ControlsTab(), "Controls")
        self.tabs.addTab(SetupTab(), "Setup")

        self.setCentralWidget(self.tabs)
        self.setGeometry(100, 100, 800, 600)
