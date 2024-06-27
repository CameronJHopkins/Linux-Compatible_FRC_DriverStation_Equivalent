# src/config/config_manager.py

import configparser

class ConfigManager:
    def __init__(self, config_file_path):
        self.config = configparser.ConfigParser()
        self.config_file_path = config_file_path
        self.load_config()

    def load_config(self):
        self.config.read(self.config_file_path)

    def get_value(self, section, key):
        try:
            return self.config.get(section, key)
        except configparser.Error as e:
            raise ConfigError(f"Error reading config: {e}")

class ConfigError(Exception):
    pass
