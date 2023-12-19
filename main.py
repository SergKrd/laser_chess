from pygame import *

if __name__ == '__main__':
    # создание окна
    init()
    num = [1000, 800]
    size = width, height = num[0], num[1]
    screen = display.set_mode(size)
    display.set_caption('Лазерные шахматы')
    white = Color('white')
    red = (153, 0, 0)
    blue = (0, 0, 153)
    board = (128, 128, 128)
    x, y = 0, 0
    part_1 = 800 // 8

    for i in range(8):
        draw.rect(screen, white, (x, y, x + part_1, y + part_1))
        draw.rect(screen, red, (x + 2, y + 2, x + part_1 - 4, y + part_1 - 4))
        y += part_1

    x += part_1
    y = 0

    for i in range(8):
        if i == 0 or i == 7:
            color = blue
        else:
            color = board
        draw.rect(screen, white, (x, y, x, y + part_1))
        draw.rect(screen, color, (x + 2, y + 2, x - 4, y + part_1 - 4))
        y += part_1

    x += part_1
    y = 0

    for i in range(6):
        for j in range(8):
            draw.rect(screen, white, (x, y, x + part_1, y + part_1))
            draw.rect(screen, board, (x + 2, y + 2, x + part_1 - 4, y + part_1 - 4))
            y += part_1
        x += part_1
        y = 0

    for i in range(8):
        if i == 0 or i == 7:
            color = red
        else:
            color = board
        draw.rect(screen, white, (x, y, x, y + part_1))
        draw.rect(screen, color, (x + 2, y + 2, x - 4, y + part_1 - 4))
        y += part_1
    x += part_1
    y = 0
    print(x)
    for i in range(8):
        draw.rect(screen, white, (x, y, x, y + part_1))
        draw.rect(screen, blue, (x + 2, y + 2, x - 4, y + part_1 - 4))
        y += part_1

    display.flip()
    while event.wait().type != QUIT:
        pass
    quit()
