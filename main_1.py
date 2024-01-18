import pygame as py
import os

import main

py.font.init()
ARIAl_50 = py.font.SysFont('arial', 100, 2)
sprite_group = py.sprite.Group()
laser_group = py.sprite.Group()
size = py.display.Info()
screen = py.display.set_mode((size.current_w, size.current_h))
width, height = size.current_w, size.current_h
part = int(height / 8)


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


def create_column(screen, color, x, y, part):
    for i in range(8):
        py.draw.rect(screen, color, (x + 5, y + 5, part - 10, part - 10))
        y += part


def create_board(screen, color, width, height):
    part = int(height / 8)
    y = 0
    x = int((width - part * 10) / 2)
    py.draw.rect(screen, color, (x, y, part * 10, height))
    color = (128, 128, 128)
    for i in range(10):
        create_column(screen, color, x, y, part)
        x += part


def create_dict():
    global part, width
    d = {}
    y = 0
    x = int((width - part * 10) / 2)
    count = 0
    for i in range(10):
        for j in range(8):
            count += 1
            d[count] = (x, y)
            y += part
        y = 0
        x += part
    return d


def load_image(name, part):
    global sprite_group
    fullname = os.path.join('data', name)
    image = py.image.load(fullname)
    image = py.transform.scale(image, (part, part))
    sprite = py.sprite.Sprite(sprite_group)
    sprite.image = image
    sprite.rect = sprite.image.get_rect()

    return sprite


def load_image_laser():
    global part
    fullname = os.path.join('data', 'laser.png')
    image = py.image.load(fullname)
    image = py.transform.scale(image, (part // 4, part))
    sprite = py.sprite.Sprite(laser_group)
    sprite.image = image
    sprite.rect = sprite.image.get_rect()


class Sprite:
    def __init__(self, part):
        self.king_r = load_image('king_r.png', part)
        self.king_b = load_image('king_b.png', part)

        self.death_star_r = load_image('The_death_star_r.png', part)
        self.death_star_b = load_image('The_death_star_b.png', part)

        self.corner_dl_b = load_image('corner_dl_b.png', part)
        self.corner_dl_r = load_image('corner_dl_r.png', part)

        self.corner_dr_b = load_image('corner_dr_b.png', part)
        self.corner_dr_r = load_image('corner_dr_r.png', part)

        self.corner_ul_b = load_image('corner_ul_b.png', part)
        self.corner_ul_r = load_image('corner_ul_r.png', part)

        self.corner_ur_b = load_image('corner_ur_b.png', part)
        self.corner_ur_r = load_image('corner_ur_r.png', part)

        self.key_l_b = load_image('key_l_b.png', part)
        self.key_l_r = load_image('key_l_r.png', part)

        self.key_r_b = load_image('key_r_b.png', part)
        self.key_r_r = load_image('key_r_r.png', part)

    def laser_sprite(self):
        self.laser = load_image_laser()

    def beginner_start(self, screen):
        d = create_dict()
        self.key_r_r.rect.x = d[70][0]
        self.key_r_r.rect.y = d[70][1]

        self.key_r_b.rect.x = d[11][0]
        self.key_r_b.rect.y = d[11][1]

        self.key_l_r.rect.x = d[47][0]
        self.key_l_r.rect.y = d[47][1]

        self.key_l_b.rect.x = d[34][0]
        self.key_l_b.rect.y = d[34][1]

        self.corner_ur_r.rect.x = d[55][0]
        self.corner_ur_r.rect.y = d[55][1]

        self.corner_ur_b.rect.x = d[19][0]
        self.corner_ur_b.rect.y = d[19][1]

        self.corner_ul_r.rect.x = d[63][0]
        self.corner_ul_r.rect.y = d[63][1]

        self.corner_ul_b.rect.x = d[27][0]
        self.corner_ul_b.rect.y = d[27][1]

        self.corner_dr_r.rect.x = d[54][0]
        self.corner_dr_r.rect.y = d[54][1]

        self.corner_dr_b.rect.x = d[18][0]
        self.corner_dr_b.rect.y = d[18][1]

        self.corner_dl_r.rect.x = d[62][0]
        self.corner_dl_r.rect.y = d[62][1]

        self.corner_dl_b.rect.x = d[26][0]
        self.corner_dl_b.rect.y = d[26][1]

        self.king_b.rect.x = d[10][0]
        self.king_b.rect.y = d[10][1]

        self.king_r.rect.x = d[71][0]
        self.king_r.rect.y = d[71][1]

        self.death_star_b.rect.x = d[1][0]
        self.death_star_b.rect.y = d[1][1]

        self.death_star_r.rect.x = d[80][0]
        self.death_star_r.rect.y = d[80][1]

        sprite_group.draw(screen)

    def amateur_start(self, screen):
        d = create_dict()
        self.key_r_r.rect.x = d[70][0]
        self.key_r_r.rect.y = d[70][1]

        self.key_r_b.rect.x = d[11][0]
        self.key_r_b.rect.y = d[11][1]

        self.key_l_r.rect.x = d[47][0]
        self.key_l_r.rect.y = d[47][1]

        self.key_l_b.rect.x = d[34][0]
        self.key_l_b.rect.y = d[34][1]

        self.corner_ur_r.rect.x = d[55][0]
        self.corner_ur_r.rect.y = d[55][1]

        self.corner_ur_b.rect.x = d[19][0]
        self.corner_ur_b.rect.y = d[19][1]

        self.corner_ul_r.rect.x = d[63][0]
        self.corner_ul_r.rect.y = d[63][1]

        self.corner_ul_b.rect.x = d[27][0]
        self.corner_ul_b.rect.y = d[27][1]

        self.corner_dr_r.rect.x = d[54][0]
        self.corner_dr_r.rect.y = d[54][1]

        self.corner_dr_b.rect.x = d[18][0]
        self.corner_dr_b.rect.y = d[18][1]

        self.corner_dl_r.rect.x = d[62][0]
        self.corner_dl_r.rect.y = d[62][1]

        self.corner_dl_b.rect.x = d[26][0]
        self.corner_dl_b.rect.y = d[26][1]

        self.king_b.rect.x = d[66][0]
        self.king_b.rect.y = d[66][1]

        self.king_r.rect.x = d[15][0]
        self.king_r.rect.y = d[15][1]

        self.death_star_b.rect.x = d[1][0]
        self.death_star_b.rect.y = d[1][1]

        self.death_star_r.rect.x = d[80][0]
        self.death_star_r.rect.y = d[80][1]

        sprite_group.draw(screen)

    def master_start(self, screen):
        d = create_dict()
        self.key_r_r.rect.x = d[23][0]
        self.key_r_r.rect.y = d[23][1]

        self.key_r_b.rect.x = d[34][0]
        self.key_r_b.rect.y = d[34][1]

        self.key_l_r.rect.x = d[47][0]
        self.key_l_r.rect.y = d[47][1]

        self.key_l_b.rect.x = d[67][0]
        self.key_l_b.rect.y = d[67][1]

        self.corner_ur_r.rect.x = d[55][0]
        self.corner_ur_r.rect.y = d[55][1]

        self.corner_ur_b.rect.x = d[20][0]
        self.corner_ur_b.rect.y = d[20][1]

        self.corner_ul_r.rect.x = d[17][0]
        self.corner_ul_r.rect.y = d[17][1]

        self.corner_ul_b.rect.x = d[27][0]
        self.corner_ul_b.rect.y = d[27][1]

        self.corner_dr_r.rect.x = d[53][0]
        self.corner_dr_r.rect.y = d[53][1]

        self.corner_dr_b.rect.x = d[18][0]
        self.corner_dr_b.rect.y = d[18][1]

        self.corner_dl_r.rect.x = d[63][0]
        self.corner_dl_r.rect.y = d[63][1]

        self.corner_dl_b.rect.x = d[26][0]
        self.corner_dl_b.rect.y = d[26][1]

        self.king_b.rect.x = d[66][0]
        self.king_b.rect.y = d[66][1]

        self.king_r.rect.x = d[15][0]
        self.king_r.rect.y = d[15][1]

        self.death_star_b.rect.x = d[1][0]
        self.death_star_b.rect.y = d[1][1]

        self.death_star_r.rect.x = d[80][0]
        self.death_star_r.rect.y = d[80][1]

        sprite_group.draw(screen)
