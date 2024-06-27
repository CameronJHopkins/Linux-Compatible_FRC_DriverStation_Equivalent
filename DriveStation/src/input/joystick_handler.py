import pygame

class JoystickHandler:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        self.joystick_count = pygame.joystick.get_count()
        if self.joystick_count > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"Initialized joystick: {self.joystick.get_name()}")

    def get_joystick_axes(self):
        if self.joystick:
            axes = [self.joystick.get_axis(i) for i in range(self.joystick.get_numaxes())]
            return axes
        return []

    def get_joystick_buttons(self):
        if self.joystick:
            buttons = [self.joystick.get_button(i) for i in range(self.joystick.get_numbuttons())]
            return buttons
        return []

    def get_joystick_hat(self):
        if self.joystick:
            hat = self.joystick.get_hat(0)
            return hat
        return (0, 0)

    def quit(self):
        pygame.quit()
