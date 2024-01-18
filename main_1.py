import pygame as py

import main

py.font.init()
d = {}
ARIAl_50 = py.font.SysFont('arial', 100, 2)


class Menu:
    def __init__(self):
        self.options_surfaces = []
        self.callbacks = []
        self.current_option = 0
        self.flag = True
        self.difficulty = 0

    def show_difficult(self):
        return self.difficulty

    def game_difficulty(self, difficulty):
        self.difficulty = difficulty

    def flag_menu(self, flag):
        self.flag = flag

    def flag_report(self):
        return self.flag

    def reset_options(self):
        self.current_option = 0

    def append_option(self, option, callback):
        if self.flag:
            self.options_surfaces.append(ARIAl_50.render(option, True, (0, 0, 0)))
            self.callbacks.append(callback)

    def switch(self, direction):
        if self.flag:
            self.current_option = max(0, min(self.current_option + direction, len(self.options_surfaces) - 1))

    def select(self):
        if self.flag:
            for elem in self.callbacks[self.current_option]:
                elem()
            main.py.display.update()

    def draw(self, surface, x, y, option_y_padding):
        if self.flag:
            for i, option in enumerate(self.options_surfaces):
                option_rect = option.get_rect()
                option_rect.topleft = (x, y + i * option_y_padding)
                if i == self.current_option:
                    py.draw.rect(surface, (0, 100, 0), option_rect)
                surface.blit(option, option_rect)


def create_column(screen, color, x, y, part, count):
    for i in range(8):
        global d
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

