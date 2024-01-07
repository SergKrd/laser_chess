import pygame as py
import main_1

FPS = 60

if __name__ == "__main__":
    py.init()
    size = py.display.Info()
    screen = py.display.set_mode((size.current_w, size.current_h))
    width, height = size.current_w, size.current_h
    clock = py.time.Clock()
    running = True

    part = main_1.create_board(screen, (255, 255, 255), width, height)
    print(main_1.d)
    print(part)
    py.display.update()

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if py.key.get_pressed()[py.K_ESCAPE]:
                    running = False

        clock.tick(FPS)
    py.quit()
