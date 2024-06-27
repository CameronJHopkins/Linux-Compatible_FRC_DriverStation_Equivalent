# Example structure if using pygame for keyboard input
import pygame

class KeyboardHandler:
    def __init__(self):
        pygame.init()

    def get_key_state(self, key):
        keys = pygame.key.get_pressed()
        return keys[key]

    def quit(self):
        pygame.quit()
