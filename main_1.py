import pygame as py

py.font.init()
d = {}
ARIAl_50 = py.font.SysFont('arial', 100, 2)


class Menu:
    def __init__(self):
        self.options_surfaces = []
        self.callbacks = []
        self.current_option = 0

    def append_option(self, option, callback):
        self.options_surfaces.append(ARIAl_50.render(option, True, (0, 0, 0)))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.current_option = max(0, min(self.current_option + direction, len(self.options_surfaces) - 1))

    def select(self):
        self.callbacks[self.current_option]()

    def draw(self, surface, x, y, option_y_padding):
        for i, option in enumerate(self.options_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_option:
                py.draw.rect(surface, (0, 100, 0), option_rect)
            surface.blit(option, option_rect)


def create_column(screen, color, x, y, part, count):
    for i in range(8):
        count += 1
        py.draw.rect(screen, color, (x + 5, y + 5, part - 10, part - 10))
        y += part
        d[count] = (x, y)


def create_board(screen, color, width, height):
    part = int(height / 8)
    y = 0
    x = int((width - part * 10) / 2)
    py.draw.rect(screen, color, (x, y, part * 10, height))
    color = (128, 128, 128)
    count = 0
    for i in range(10):
        create_column(screen, color, x, y, part, count)
        count += 8
        x += part
