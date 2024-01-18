import pygame as py
import main_1
import sprite

py.init()
FPS = 60

if __name__ == "__main__":
    running = True
    size = py.display.Info()
    screen = py.display.set_mode((size.current_w, size.current_h))
    width, height = size.current_w, size.current_h
    part = int(height / 8)


    def draw():
        if menu.flag_report() or game_menu.flag_report():
            screen.fill((255, 255, 102))
            menu.draw(screen, part * 4, part * 2, part)
            game_menu.draw(screen, part * 4, part * 2, part)
            py.display.update()


    menu = main_1.Menu()
    menu.append_option('Играть', (lambda: game_menu.flag_menu(True),))
    menu.append_option('Статистика', (lambda: screen.fill((255, 255, 255)),))
    menu.append_option('Выход', (quit,))

    game_menu = main_1.Menu()
    game_menu.append_option('Выберите сложность:', (lambda: 0,))
    game_menu.append_option('Новичок', (
        lambda: screen.fill((0, 0, 0)), lambda: main_1.create_board(screen, (255, 255, 255), width, height),
        lambda: game_menu.flag_menu(False), lambda: game_menu.game_difficulty(1)))
    game_menu.append_option('Любитель', (
        lambda: screen.fill((0, 0, 0)), lambda: main_1.create_board(screen, (255, 255, 255), width, height),
        lambda: game_menu.flag_menu(False), lambda: game_menu.game_difficulty(2)))
    game_menu.append_option('Профессионал', (
        lambda: screen.fill((0, 0, 0)), lambda: main_1.create_board(screen, (255, 255, 255), width, height),
        lambda: game_menu.flag_menu(False), lambda: game_menu.game_difficulty(3)))
    game_menu.flag_menu(False)

    draw()

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    game_menu.flag_menu(False)
                    game_menu.reset_options()
                    game_menu.game_difficulty(0)
                    menu.flag_menu(True)
                    draw()

                elif event.key == py.K_UP:
                    menu.switch(-1)
                    game_menu.switch(-1)
                    draw()
                elif event.key == py.K_DOWN:
                    menu.switch(1)
                    game_menu.switch(1)
                    draw()
                elif event.key == py.K_SPACE:
                    menu.select()
                    game_menu.select()
                    menu.flag_menu(False)
                    draw()
        if game_menu.show_difficult() == 1:
            start_beginner = main_1.Sprite(part)
            start_beginner.beginner_start(screen)
            py.display.update()

    py.quit()
