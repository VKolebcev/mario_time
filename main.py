#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
import player
import level
import camera


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(camera.DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    # будем использовать как фон
    bg = pygame.image.load(level.BG_DIR)  # Заливаем поверхность сплошным цветом

    hero = player.Player(55, 55)  # создаем героя по (x,y) координатам
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()  # Все объекты
    level_1 = level.Level()
    platforms = level_1.getPlatform()  # то, во что мы будем врезаться или опираться
    for platform in platforms:
        entities.add(platform)
    entities.add(hero)

    # все анимированные объекты, за исключением героя
    animatedEntities = pygame.sprite.Group()
    tp = level.platform.BlockTeleport(128, 512, 800, 64)
    entities.add(tp)
    platforms.append(tp)
    animatedEntities.add(tp)

    # Все передвигающиеся объекты
    monsters = pygame.sprite.Group()
    mn = player.monsters.Monster(190, 200, 2, 3, 150, 15)
    entities.add(mn)
    platforms.append(mn)
    monsters.add(mn)

    level_1.getPrincess(entities, animatedEntities, platforms)

    # Высчитываем фактическую ширину уровня
    total_level_width = len(level_1.load()[0]) * \
                        level.platform.PLATFORM_WIDTH
    # Высчитываем фактическую высоту уровня
    total_level_height = len(level_1.load()) * \
                         level.platform.PLATFORM_HEIGHT
    main_camera = camera.Camera(total_level_width,
                                total_level_height)

    while True:  # Основной цикл программы
        timer.tick(60)
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == pygame.QUIT:
                raise SystemExit(1)
            hero.move(event)


        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        hero.update(platforms)  # передвижение
        #entities.draw(screen)  # отображение всего
        # центризируем камеру относительно персонажа
        main_camera.update(hero)
        for e in entities:
            screen.blit(e.image, main_camera.apply(e))

        pygame.display.update()  # обновление и вывод всех изменений на экран
        animatedEntities.update()  # показываем анимацию
        monsters.update(platforms)  # передвигаем всех монстров

        if hero.winner:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
