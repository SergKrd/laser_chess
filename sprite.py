import pygame as py
import os

import main

py.init()


def load_image(name):
    fullname = os.path.join('data', name)
    image = py.image.load(fullname)
    image = py.transform.scale(image, (180, 180))
    # colorkey = image.get_at((0, 0))
    # image = image.convert()
    # image.set_colorkey(colorkey)
    sprite = py.sprite.Sprite()
    sprite.image = image
    sprite.rect = sprite.image.get_rect()

    return sprite


class Sprite:
    def __init__(self):
        self.king_r = load_image('king_r.png')
        self.king_b = load_image('king_b.png')
        self.death_star_r = load_image('The_death_star_r.png')
        self.death_star_b = load_image('The_death_star_b.png')
