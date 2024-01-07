import pygame as py

d = {}


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
    return part
