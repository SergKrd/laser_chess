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
    part = int(height / 8)


    # main_1.create_board(screen, (255, 255, 255), width, height)
    # print(main_1.d)
    # print(part)

    menu = main_1.Menu()
    menu.append_option('Играть', main_1.create_board(screen, (255, 255, 255), width, height))
    menu.append_option('Статистика', screen.fill((255, 255, 255)))
    menu.append_option('Выход', quit)

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.KEYDOWN:
                if py.key.get_pressed()[py.K_ESCAPE]:
                    screen.fill((255, 255, 102))
                    menu.draw(screen, part * 4, part * 2, part)
                    py.display.update()
                elif py.key.get_pressed()[py.K_w]:
                    menu.switch(-1)
                elif py.key.get_pressed()[py.K_s]:
                    menu.switch(1)

                elif py.key.get_pressed()[py.K_SPACE]:
                    menu.select()


        screen.fill((255, 255, 102))
        menu.draw(screen, part * 4, part * 2, part)
        py.display.update()

        clock.tick(FPS)
    py.quit()
